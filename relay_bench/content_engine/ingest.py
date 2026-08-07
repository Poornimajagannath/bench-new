"""Ingestion snapshot: immutable raw/<date>/ + schema-gated normalized/ (M0.5)."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DOCS_DIR = ROOT / "cybersource-docs"
DEFAULT_RAW_ROOT = ROOT / "raw"
DEFAULT_NORMALIZED_ROOT = ROOT / "normalized"
DEFAULT_OPENAPI = ROOT / "data" / "content_engine" / "specs" / "cybersource-payments-core.openapi.json"

CLAIM_SCHEMAS = (
    "quickstart_step",
    "endpoint_fact",
    "error_case",
    "prose_claim",
)

_DROP_PATTERNS = (
    (re.compile(r"\brevision history\b", re.I), "revision_history"),
    (re.compile(r"\btable of contents\b", re.I), "index_page"),
    (re.compile(r"\bhome[- ]merch\b", re.I), "index_page"),
    (re.compile(r"^\s*#+\s*index\s*$", re.I | re.M), "index_page"),
)


@dataclass
class RawMeta:
    source_url: str
    fetched_at: str
    content_hash: str
    relative_path: str
    bytes: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class NormalizedClaim:
    claim_id: str
    schema: str
    text: str
    source_pointer: str
    title: str = ""
    extras: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DropRecord:
    path: str
    reason: str
    detail: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reconstruct_source_url(filename: str) -> str:
    """Best-effort URL reconstruction from download-cybersource-docs naming."""
    name = filename
    if name.endswith(".md.md"):
        name = name[:-3]
    if not name.endswith(".md"):
        name = name + ".md"
    # Common prefixes from the downloader.
    if name.startswith("en-us_"):
        return f"https://developer.example.com/docs/gateway/{name.replace('_', '/', 1)}"
    return f"https://developer.example.com/docs/gateway/{name}"


def stamp_copy_to_raw(
    sources: Sequence[Path],
    *,
    raw_root: Path = DEFAULT_RAW_ROOT,
    stamp_date: Optional[str] = None,
    source_url_for: Optional[Any] = None,
) -> Tuple[Path, List[RawMeta], List[DropRecord]]:
    """Copy sources into raw/<date>/ with sidecar meta. Never overwrite existing files."""
    day = stamp_date or date.today().isoformat()
    dest_dir = raw_root / day
    dest_dir.mkdir(parents=True, exist_ok=True)
    metas: List[RawMeta] = []
    drops: List[DropRecord] = []
    fetched_at = _utc_now()

    for src in sources:
        if not src.is_file():
            drops.append(DropRecord(path=str(src), reason="missing_source"))
            continue
        rel_name = src.name
        dest = dest_dir / rel_name
        data = src.read_bytes()
        digest = _hash_bytes(data)
        if dest.exists():
            existing = dest.read_bytes()
            if _hash_bytes(existing) != digest:
                drops.append(
                    DropRecord(
                        path=str(dest.relative_to(raw_root)),
                        reason="raw_immutable_conflict",
                        detail="refusing to overwrite differing raw file",
                    )
                )
            # still record meta if sidecar missing
        else:
            dest.write_bytes(data)

        url = (
            source_url_for(src)
            if source_url_for
            else reconstruct_source_url(src.name)
        )
        meta = RawMeta(
            source_url=url,
            fetched_at=fetched_at,
            content_hash=digest,
            relative_path=f"{day}/{rel_name}",
            bytes=len(data),
        )
        meta_path = dest.with_suffix(dest.suffix + ".meta.json")
        if not meta_path.exists():
            meta_path.write_text(json.dumps(meta.to_dict(), indent=2) + "\n", encoding="utf-8")
        metas.append(meta)
    return dest_dir, metas, drops


def _should_drop_doc(text: str, path: Path) -> Optional[str]:
    for pattern, reason in _DROP_PATTERNS:
        if pattern.search(text) or pattern.search(path.name):
            return reason
    # Near-empty
    if len(text.strip()) < 40:
        return "empty_or_stub"
    return None


def _extract_claims_from_text(
    text: str,
    *,
    source_pointer: str,
    doc_stem: str,
) -> Tuple[List[NormalizedClaim], List[DropRecord]]:
    claims: List[NormalizedClaim] = []
    drops: List[DropRecord] = []
    drop_reason = _should_drop_doc(text, Path(doc_stem))
    if drop_reason:
        drops.append(DropRecord(path=source_pointer, reason=drop_reason))
        return claims, drops

    # Quickstart steps: numbered headings or numbered lists
    step_pat = re.compile(
        r"(?m)^(?:#{2,4}\s*)?(?:Step\s*)?(\d+)[.:)\s]+(.+?)(?:\n|$)"
    )
    for match in step_pat.finditer(text):
        n, title = match.group(1), match.group(2).strip()
        if len(title) < 3:
            continue
        claims.append(
            NormalizedClaim(
                claim_id=f"{doc_stem}:step:{n}",
                schema="quickstart_step",
                title=title[:120],
                text=title,
                source_pointer=source_pointer,
                extras={"sequence": int(n)},
            )
        )

    # Endpoint facts: HTTP verbs + paths
    for match in re.finditer(
        r"\b(GET|POST|PUT|PATCH|DELETE)\s+(/[A-Za-z0-9_{}/.-]+)",
        text,
    ):
        claims.append(
            NormalizedClaim(
                claim_id=f"{doc_stem}:endpoint:{match.group(1).lower()}:{hashlib.sha1(match.group(0).encode()).hexdigest()[:8]}",
                schema="endpoint_fact",
                title=f"{match.group(1)} {match.group(2)}",
                text=match.group(0),
                source_pointer=source_pointer,
                extras={"method": match.group(1), "path": match.group(2)},
            )
        )

    # Error cases
    for match in re.finditer(
        r"(?i)\b(error|fault)\b[^\n]{0,80}\b(\d{3}|[A-Z][A-Z0-9_]{2,})\b",
        text,
    ):
        snippet = match.group(0).strip()
        claims.append(
            NormalizedClaim(
                claim_id=f"{doc_stem}:error:{hashlib.sha1(snippet.encode()).hexdigest()[:8]}",
                schema="error_case",
                title=snippet[:80],
                text=snippet,
                source_pointer=source_pointer,
            )
        )

    # Prose claims: imperative / guidance sentences with a pointer
    for match in re.finditer(
        r"(?m)^(?:[-*]\s+|(?:You|Developers?|Merchants?)\s+)(.{20,220}[.!?])\s*$",
        text,
    ):
        sentence = match.group(0).strip()
        if re.search(r"revision history|table of contents", sentence, re.I):
            drops.append(
                DropRecord(
                    path=source_pointer,
                    reason="no_schema_match",
                    detail="navigation/history sentence",
                )
            )
            continue
        claims.append(
            NormalizedClaim(
                claim_id=f"{doc_stem}:prose:{hashlib.sha1(sentence.encode()).hexdigest()[:8]}",
                schema="prose_claim",
                title=sentence[:80],
                text=sentence,
                source_pointer=source_pointer,
            )
        )

    if not claims:
        drops.append(
            DropRecord(
                path=source_pointer,
                reason="no_schema_match",
                detail="no quickstart/endpoint/error/prose claim extracted",
            )
        )
    return claims, drops


def extract_openapi_endpoint_facts(
    openapi_path: Path,
    *,
    source_pointer: str,
) -> List[NormalizedClaim]:
    data = json.loads(openapi_path.read_text(encoding="utf-8"))
    claims: List[NormalizedClaim] = []
    for path, methods in (data.get("paths") or {}).items():
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if method.startswith("x-") or not isinstance(op, dict):
                continue
            op_id = op.get("operationId") or f"{method}_{path}"
            params = [
                {
                    "name": p.get("name"),
                    "in": p.get("in"),
                    "required": bool(p.get("required")),
                    "type": (p.get("schema") or {}).get("type"),
                }
                for p in (op.get("parameters") or [])
                if isinstance(p, dict)
            ]
            codes = sorted(str(c) for c in (op.get("responses") or {}))
            claims.append(
                NormalizedClaim(
                    claim_id=f"openapi:{op_id}",
                    schema="endpoint_fact",
                    title=f"{method.upper()} {path}",
                    text=op.get("summary") or op.get("description") or f"{method.upper()} {path}",
                    source_pointer=source_pointer,
                    extras={
                        "method": method.upper(),
                        "path": path,
                        "operation_id": op_id,
                        "parameters": params,
                        "status_codes": codes,
                        "security": op.get("security") or data.get("security") or [],
                    },
                )
            )
    return claims


def normalize_raw_dir(
    raw_dir: Path,
    *,
    normalized_root: Path = DEFAULT_NORMALIZED_ROOT,
    openapi_path: Optional[Path] = DEFAULT_OPENAPI,
) -> Tuple[List[NormalizedClaim], List[DropRecord]]:
    normalized_root.mkdir(parents=True, exist_ok=True)
    all_claims: List[NormalizedClaim] = []
    all_drops: List[DropRecord] = []

    for path in sorted(raw_dir.iterdir()):
        if not path.is_file() or path.name.endswith(".meta.json"):
            continue
        if path.suffix not in {".md", ".txt", ".json"}:
            all_drops.append(
                DropRecord(
                    path=str(path.relative_to(raw_dir.parent)),
                    reason="no_schema_match",
                    detail=f"unsupported extension {path.suffix}",
                )
            )
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        pointer = str(path.relative_to(raw_dir.parent))
        claims, drops = _extract_claims_from_text(
            text,
            source_pointer=pointer,
            doc_stem=path.stem.replace(".md", ""),
        )
        all_claims.extend(claims)
        all_drops.extend(drops)

    if openapi_path and openapi_path.is_file():
        # Stamp OpenAPI into the same raw day if not already present.
        day = raw_dir.name
        openapi_raw = raw_dir / openapi_path.name
        if not openapi_raw.exists():
            openapi_raw.write_bytes(openapi_path.read_bytes())
            meta = RawMeta(
                source_url=f"local://{openapi_path.as_posix()}",
                fetched_at=_utc_now(),
                content_hash=_hash_bytes(openapi_path.read_bytes()),
                relative_path=f"{day}/{openapi_path.name}",
                bytes=openapi_path.stat().st_size,
            )
            openapi_raw.with_suffix(openapi_raw.suffix + ".meta.json").write_text(
                json.dumps(meta.to_dict(), indent=2) + "\n",
                encoding="utf-8",
            )
        all_claims.extend(
            extract_openapi_endpoint_facts(
                openapi_path,
                source_pointer=f"{day}/{openapi_path.name}",
            )
        )

    out_path = normalized_root / f"{raw_dir.name}.claims.json"
    payload = {
        "generated_at": _utc_now(),
        "raw_dir": str(raw_dir.relative_to(ROOT)) if raw_dir.is_relative_to(ROOT) else str(raw_dir),
        "claim_count": len(all_claims),
        "schemas": sorted({c.schema for c in all_claims}),
        "claims": [c.to_dict() for c in all_claims],
        "read_contract": {
            "portal": ["normalized/", "content/"],
            "mcp": ["normalized/", "content/"],
            "humanizer": ["normalized/", "content/"],
            "evals": ["normalized/", "content/"],
            "forbidden": ["raw/"],
        },
    }
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return all_claims, all_drops


def select_ingest_sources(docs_dir: Path, limit: int = 60) -> List[Path]:
    files = sorted(
        p
        for p in docs_dir.iterdir()
        if p.is_file() and p.suffix == ".md" and not p.name.startswith("_")
    )
    if len(files) <= limit:
        return files
    keywords = ("auth", "payment", "getting-started", "microform", "sandbox", "token", "error")
    preferred = [p for p in files if any(k in p.name.lower() for k in keywords)]
    rest = [p for p in files if p not in preferred]
    out = preferred[: limit // 2]
    step = max(len(rest) // max(limit - len(out), 1), 1)
    out.extend(rest[::step][: limit - len(out)])
    return out[:limit]


def run_ingestion_snapshot(
    *,
    docs_dir: Path = DEFAULT_DOCS_DIR,
    raw_root: Path = DEFAULT_RAW_ROOT,
    normalized_root: Path = DEFAULT_NORMALIZED_ROOT,
    openapi_path: Path = DEFAULT_OPENAPI,
    stamp_date: Optional[str] = None,
    sample_limit: int = 60,
    sources: Optional[Sequence[Path]] = None,
) -> Dict[str, Any]:
    srcs = list(sources) if sources is not None else select_ingest_sources(docs_dir, limit=sample_limit)
    raw_dir, metas, copy_drops = stamp_copy_to_raw(
        srcs,
        raw_root=raw_root,
        stamp_date=stamp_date,
    )
    claims, extract_drops = normalize_raw_dir(
        raw_dir,
        normalized_root=normalized_root,
        openapi_path=openapi_path if openapi_path.is_file() else None,
    )
    drops = copy_drops + extract_drops
    report = {
        "stamp_date": raw_dir.name,
        "docs_fetched": len(metas),
        "claims_extracted": len(claims),
        "claims_by_schema": {
            schema: sum(1 for c in claims if c.schema == schema)
            for schema in CLAIM_SCHEMAS
        },
        "drop_count": len(drops),
        "drops": [d.to_dict() for d in drops],
        "raw_dir": str(raw_dir.relative_to(ROOT)) if raw_dir.is_relative_to(ROOT) else str(raw_dir),
        "normalized_file": f"normalized/{raw_dir.name}.claims.json",
        "read_contract": ["normalized/", "content/"],
        "forbidden_reads": ["raw/"],
    }
    return report


def render_ingestion_report(report: Dict[str, Any]) -> str:
    lines = [
        "# Ingestion report",
        "",
        "Milestone 0.5: corpus cleaned at the door. `raw/` is immutable evidence; serve layers read only `normalized/` and `content/`.",
        "",
        f"- Stamp date: `{report['stamp_date']}`",
        f"- Docs fetched into raw: {report['docs_fetched']}",
        f"- Claims extracted: {report['claims_extracted']}",
        f"- Raw dir: `{report['raw_dir']}`",
        f"- Normalized file: `{report['normalized_file']}`",
        f"- Read contract: {', '.join(report['read_contract'])}",
        f"- Forbidden: {', '.join(report['forbidden_reads'])}",
        "",
        "## Claims by schema",
        "",
        "| Schema | Count |",
        "| --- | ---: |",
    ]
    for schema, count in report["claims_by_schema"].items():
        lines.append(f"| {schema} | {count} |")
    lines.extend(["", "## Drop log", ""])
    if not report["drops"]:
        lines.append("_No drops._")
    else:
        lines.append("| Path | Reason | Detail |")
        lines.append("| --- | --- | --- |")
        for d in report["drops"][:200]:
            lines.append(f"| {d['path']} | {d['reason']} | {d.get('detail') or '—'} |")
        if len(report["drops"]) > 200:
            lines.append(f"| … | … | {len(report['drops']) - 200} more |")
    lines.append("")
    return "\n".join(lines)
