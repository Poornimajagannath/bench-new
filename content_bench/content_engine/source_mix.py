"""Classify docs as OpenAPI-regenerable vs prose-only (Milestone 0)."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OPENAPI = ROOT / "data" / "content_engine" / "specs" / "payments-core.openapi.json"
DEFAULT_DOCS_DIR = ROOT / "gateway-docs"

_SPEC_HINTS = (
    "endpoint",
    "request",
    "response",
    "parameter",
    "status code",
    "http",
    "authorization",
    "jwt",
    "api key",
    "bearer",
    "header",
    "path",
    "query",
    "body",
    "schema",
    "field",
    "error code",
)

_PROSE_HINTS = (
    "before you begin",
    "prerequisite",
    "gotcha",
    "common mistake",
    "sequence",
    "then",
    "first",
    "next",
    "finally",
    "business rule",
    "must not",
    "should not",
    "recommended",
    "best practice",
    "sandbox does not",
    "known gap",
    "workaround",
    "integration tip",
    "go-live",
    "checklist",
)


@dataclass
class GuideMix:
    guide: str
    path: str
    spec_backed_share: float
    prose_only_share: float
    spec_hits: int
    prose_hits: int
    notes: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProseSection:
    guide: str
    section: str
    why_it_matters: str
    score: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def load_openapi_tokens(openapi_path: Path) -> Set[str]:
    data = json.loads(openapi_path.read_text(encoding="utf-8"))
    tokens: Set[str] = set()
    for path, methods in (data.get("paths") or {}).items():
        tokens.add(path.lower())
        for part in path.strip("/").split("/"):
            if part and not part.startswith("{"):
                tokens.add(part.lower())
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if method.startswith("x-") or not isinstance(op, dict):
                continue
            tokens.add(method.lower())
            op_id = op.get("operationId")
            if op_id:
                tokens.add(str(op_id).lower())
            for param in op.get("parameters") or []:
                name = param.get("name")
                if name:
                    tokens.add(str(name).lower())
            for code in (op.get("responses") or {}):
                tokens.add(str(code).lower())
    for scheme in (data.get("components") or {}).get("securitySchemes") or {}:
        tokens.add(str(scheme).lower())
        tokens.add("jwt")
        tokens.add("http signature")
    return {t for t in tokens if len(t) >= 3}


def _count_hits(text: str, needles: Iterable[str]) -> int:
    lower = text.lower()
    return sum(1 for n in needles if n in lower)


def _split_sections(text: str) -> List[Tuple[str, str]]:
    parts = re.split(r"(?m)^(#{1,3}\s+.+)$", text)
    if len(parts) == 1:
        return [("Document", text)]
    sections: List[Tuple[str, str]] = []
    if parts[0].strip():
        sections.append(("Preamble", parts[0]))
    for i in range(1, len(parts), 2):
        heading = re.sub(r"^#{1,3}\s+", "", parts[i]).strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append((heading, body))
    return sections


def score_guide(
    path: Path,
    *,
    openapi_tokens: Set[str],
    rel_root: Optional[Path] = None,
) -> Tuple[GuideMix, List[ProseSection]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    root = rel_root or path.parent
    try:
        rel = str(path.relative_to(root))
    except ValueError:
        rel = path.name

    token_hits = _count_hits(text, openapi_tokens)
    hint_hits = _count_hits(text, _SPEC_HINTS)
    spec_hits = token_hits + hint_hits
    prose_hits = _count_hits(text, _PROSE_HINTS)

    # Index / toc pages are mostly navigation — treat as low signal.
    index_like = bool(
        re.search(r"\b(table of contents|index|revision history)\b", text, re.I)
    ) or path.name.endswith("home-merch.md.md")
    if index_like:
        prose_hits = max(prose_hits, 3)
        notes = "index-like; mostly navigation / revision surface"
    else:
        notes = ""

    total = spec_hits + prose_hits
    if total == 0:
        spec_share = 0.0
        prose_share = 1.0
        notes = (notes + "; " if notes else "") + "no classifiable signals"
    else:
        spec_share = round(spec_hits / total, 3)
        prose_share = round(1.0 - spec_share, 3)

    guide = GuideMix(
        guide=path.stem.replace(".md", ""),
        path=rel,
        spec_backed_share=spec_share,
        prose_only_share=prose_share,
        spec_hits=spec_hits,
        prose_hits=prose_hits,
        notes=notes,
    )

    prose_sections: List[ProseSection] = []
    for heading, body in _split_sections(text):
        p = _count_hits(body, _PROSE_HINTS)
        s = _count_hits(body, openapi_tokens) + _count_hits(body, _SPEC_HINTS)
        if p <= s or p == 0:
            continue
        score = float(p - s) + min(len(body) / 4000.0, 2.0)
        why = "sequencing / prerequisites / gotchas not recoverable from OpenAPI alone"
        if re.search(r"auth|jwt|signature|credential", heading + body, re.I):
            why = "auth sequencing and credential handling advice"
            score += 2.0
        if re.search(r"sandbox|test card|go-live|checklist", heading + body, re.I):
            why = "sandbox behavior and go-live checklist guidance"
            score += 1.5
        prose_sections.append(
            ProseSection(
                guide=guide.guide,
                section=heading,
                why_it_matters=why,
                score=round(score, 2),
            )
        )
    return guide, prose_sections


def select_sample(docs_dir: Path, limit: int = 40) -> List[Path]:
    if not docs_dir.is_dir():
        return []
    files = sorted(
        p
        for p in docs_dir.iterdir()
        if p.is_file() and p.suffix == ".md" and not p.name.startswith("_")
    )
    if len(files) <= limit:
        return files

    keywords = (
        "auth",
        "jwt",
        "http-signature",
        "payment",
        "quickstart",
        "getting-started",
        "microform",
        "payer",
        "sandbox",
        "credential",
        "token",
        "error",
    )
    preferred = [p for p in files if any(k in p.name.lower() for k in keywords)]
    remainder = [p for p in files if p not in preferred]
    out = preferred[: max(limit // 2, 1)]
    step = max(len(remainder) // max(limit - len(out), 1), 1)
    out.extend(remainder[::step][: limit - len(out)])
    return out[:limit]


def analyze_source_mix(
    *,
    openapi_path: Path = DEFAULT_OPENAPI,
    docs_dir: Path = DEFAULT_DOCS_DIR,
    extra_paths: Optional[Sequence[Path]] = None,
    sample_limit: int = 40,
) -> Dict[str, Any]:
    tokens = load_openapi_tokens(openapi_path)
    paths = list(select_sample(docs_dir, limit=sample_limit))
    if extra_paths:
        paths.extend(Path(p) for p in extra_paths)

    guides: List[GuideMix] = []
    prose_sections: List[ProseSection] = []
    for path in paths:
        if not path.is_file():
            continue
        g, sections = score_guide(path, openapi_tokens=tokens, rel_root=ROOT)
        guides.append(g)
        prose_sections.extend(sections)

    if guides:
        overall_spec = round(sum(g.spec_backed_share for g in guides) / len(guides), 3)
    else:
        overall_spec = 0.0
    overall_prose = round(1.0 - overall_spec, 3)

    top_prose = sorted(prose_sections, key=lambda s: s.score, reverse=True)[:10]
    decision = (
        "spec-primary: generate endpoint pages from OpenAPI; DocETL mines prose only for gaps"
        if overall_spec >= 0.70
        else "prose-first-class: DocETL extraction of legacy prose is a first-class source; every claim needs a source pointer"
    )

    return {
        "openapi_path": str(openapi_path.relative_to(ROOT)) if openapi_path.is_relative_to(ROOT) else str(openapi_path),
        "docs_sampled": len(guides),
        "overall_spec_backed_share": overall_spec,
        "overall_prose_only_share": overall_prose,
        "decision_rule": decision,
        "guides": [g.to_dict() for g in guides],
        "top_prose_sections": [s.to_dict() for s in top_prose],
    }


def render_source_mix_markdown(result: Dict[str, Any]) -> str:
    lines = [
        "# Source mix report",
        "",
        "Milestone 0 inventory: what fraction of each guide's facts could be regenerated from the local OpenAPI fixture versus facts that exist only in prose.",
        "",
        f"- OpenAPI: `{result['openapi_path']}`",
        f"- Guides sampled: {result['docs_sampled']}",
        f"- Overall spec-backed share: **{result['overall_spec_backed_share']:.1%}**",
        f"- Overall prose-only share: **{result['overall_prose_only_share']:.1%}**",
        f"- Decision rule outcome: {result['decision_rule']}",
        "",
        "## Per-guide table",
        "",
        "| Guide | Spec-backed | Prose-only | Spec hits | Prose hits | Notes |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for g in result["guides"]:
        lines.append(
            f"| {g['guide']} | {g['spec_backed_share']:.1%} | {g['prose_only_share']:.1%} | "
            f"{g['spec_hits']} | {g['prose_hits']} | {g['notes'] or '—'} |"
        )
    lines.extend(
        [
            "",
            "## Top 10 prose-only sections for a first integration",
            "",
        ]
    )
    if not result["top_prose_sections"]:
        lines.append("_No prose-dominant sections found in the sample._")
    else:
        for i, s in enumerate(result["top_prose_sections"], 1):
            lines.append(
                f"{i}. **{s['guide']} — {s['section']}** (score {s['score']}): {s['why_it_matters']}"
            )
    lines.append("")
    return "\n".join(lines)
