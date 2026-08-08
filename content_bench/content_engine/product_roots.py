"""Product-root corpus fetch — the product root is the source of truth.

Deep module: interface = docs.md product list -> derived roots -> verbatim
raw/ files + section index + TOC cross-check report.

Why this exists: per-page TOC fetch walked past endpoints, required-field
lists, and JSON examples that live only in the family mega-guide root
(boarding.md ≈ 4880 lines / 116 fenced blocks; same shape on payments.md
and tms.md). The root is the denominator; the site TOC is a cross-check
that reports pages whose content does not appear in the root.

Derivation: docs.md links point at intro *subtopics*, not roots. The root
is the guide directory promoted to a sibling ``.md`` file — which is the
family name repeated when the guide folder matches the family
(``…/boarding/developer/all/rest/boarding.md``). When the guide folder is
named differently (``echeck-user-guide``, ``mass-transit``, …), that folder
name is used. Strict family-name-repeat is tried first and recorded; the
guide-dir form is the resolving fallback.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple
from urllib.parse import urljoin

from content_bench.content_engine.toc_fetch import (
    extract_toc_topics,
    http_get,
    looks_like_markdown,
    url_to_local_name,
)

DEFAULT_UA = "Content-Bench/1.0 (product-roots)"
DEFAULT_DOCS_MD = "https://developer.cybersource.com/docs.md"
DEFAULT_BASE = "https://developer.cybersource.com"

# Underline (DITA) or ATX heading carrying a {#anchor}.
_ANCHORED_HEADING = re.compile(
    r"(?m)^(?:"
    r"(#{1,6})\s+(.+?)\s*\{#([^}]+)\}\s*$"
    r"|"
    r"(.+?)\s*\{#([^}]+)\}\s*\n(=+|-+)\s*$"
    r")"
)


@dataclass
class ProductLink:
    title: str
    intro_path: str


@dataclass
class RootDerivation:
    title: str
    intro_path: str
    family: Optional[str]
    family_repeat_root: Optional[str]
    guide_dir_root: Optional[str]
    chosen_root: Optional[str]
    derivation: str  # family_repeat | guide_dir | already_root | not_md | unresolved
    http_status: Optional[int] = None
    bytes: int = 0
    resolves: bool = False


@dataclass
class Section:
    anchor: str
    title: str
    byte_start: int
    byte_end: int
    deep_link: str
    heading_level: int


@dataclass
class ProductRootReport:
    product_id: str
    title: str
    intro_path: str
    root_path: str
    root_url: str
    derivation: str
    http_status: int
    bytes: int
    local_path: Optional[str]
    sections_split: int
    toc_topics: int
    toc_covered: int
    toc_uncovered: List[str] = field(default_factory=list)
    code_fences: int = 0
    error: Optional[str] = None


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def family_from_path(path: str) -> Optional[str]:
    parts = path.strip("/").split("/")
    try:
        i = parts.index("en-us")
    except ValueError:
        return None
    if i + 1 >= len(parts):
        return None
    return parts[i + 1]


def derive_family_repeat_root(intro_path: str) -> Optional[str]:
    """…/{family}/…/{family}/{leaf}.md → …/{family}/…/{family}.md"""
    if not intro_path.endswith(".md") or intro_path.startswith("/content/"):
        return None
    parts = intro_path.strip("/").split("/")
    family = family_from_path(intro_path)
    if not family:
        return None
    if parts[-1] == f"{family}.md":
        return "/" + "/".join(parts)
    idxs = [j for j, p in enumerate(parts) if p == family]
    if len(idxs) < 2:
        return None
    last = idxs[-1]
    if last != len(parts) - 2:
        return None
    return "/" + "/".join(parts[:last] + [f"{family}.md"])


def derive_guide_dir_root(intro_path: str) -> Optional[str]:
    """…/{guide_dir}/{leaf}.md → …/{guide_dir}.md (general form of family-repeat)."""
    if not intro_path.endswith(".md") or intro_path.startswith("/content/"):
        return None
    parts = intro_path.strip("/").split("/")
    if len(parts) < 2:
        return None
    guide_dir = parts[-2]
    if parts[-1] == f"{guide_dir}.md":
        return "/" + "/".join(parts)
    return "/" + "/".join(parts[:-2] + [f"{guide_dir}.md"])


def derive_product_root(intro_path: str) -> Tuple[Optional[str], str, Optional[str], Optional[str]]:
    """Return (chosen_root, derivation, family_repeat_root, guide_dir_root)."""
    if not intro_path.endswith(".md"):
        return None, "not_md", None, None
    if intro_path.startswith("/content/"):
        return None, "not_md", None, None
    family_repeat = derive_family_repeat_root(intro_path)
    guide_dir = derive_guide_dir_root(intro_path)
    parts = intro_path.strip("/").split("/")
    family = family_from_path(intro_path)
    if family and parts[-1] == f"{family}.md":
        return intro_path if intro_path.startswith("/") else "/" + intro_path, "already_root", family_repeat, guide_dir
    if family_repeat:
        return family_repeat, "family_repeat", family_repeat, guide_dir
    if guide_dir:
        return guide_dir, "guide_dir", family_repeat, guide_dir
    return None, "unresolved", family_repeat, guide_dir


def parse_docs_md_products(text: str) -> List[ProductLink]:
    """Unique product cards from docs.md (title + intro href)."""
    pairs: List[ProductLink] = []
    seen = set()
    for m in re.finditer(
        r"\[(?:<br />\s*)?\n?([^\n<\]]+)\n([^\]]*?)(?:<br />\s*)*\]"
        r"\((/docs/[^)]+\.md|/content/[^)]+)\)",
        text,
    ):
        title = m.group(1).strip()
        href = m.group(3)
        if href in seen:
            continue
        seen.add(href)
        pairs.append(ProductLink(title=title, intro_path=href))
    return pairs


def fetch_docs_md(
    *,
    docs_md_url: str = DEFAULT_DOCS_MD,
    user_agent: str = DEFAULT_UA,
) -> str:
    code, body, _ = http_get(docs_md_url, user_agent=user_agent)
    if code != 200 or not body:
        raise RuntimeError(f"docs.md fetch failed: HTTP {code}")
    return body.decode("utf-8", errors="replace")


def probe_root(
    root_path: str,
    *,
    base_url: str = DEFAULT_BASE,
    user_agent: str = DEFAULT_UA,
) -> Tuple[int, int]:
    code, body, _ = http_get(urljoin(base_url, root_path), user_agent=user_agent)
    if code == 200 and body and looks_like_markdown(body.decode("utf-8", errors="replace")):
        return code, len(body)
    return code, len(body) if body else 0


def resolve_products(
    products: Sequence[ProductLink],
    *,
    base_url: str = DEFAULT_BASE,
    user_agent: str = DEFAULT_UA,
    sleep_s: float = 0.05,
    probe: bool = True,
) -> List[RootDerivation]:
    """Derive roots; optionally HTTP-probe. Family-repeat first; guide-dir fallback on miss."""
    out: List[RootDerivation] = []
    for p in products:
        chosen, how, fam_r, guide_r = derive_product_root(p.intro_path)
        d = RootDerivation(
            title=p.title,
            intro_path=p.intro_path,
            family=family_from_path(p.intro_path),
            family_repeat_root=fam_r,
            guide_dir_root=guide_r,
            chosen_root=chosen,
            derivation=how,
        )
        if chosen is None:
            out.append(d)
            continue
        if not probe:
            d.resolves = True
            out.append(d)
            continue
        status, nbytes = probe_root(chosen, base_url=base_url, user_agent=user_agent)
        d.http_status = status
        d.bytes = nbytes
        if status == 200 and nbytes > 0:
            d.resolves = True
        elif guide_r and guide_r != chosen:
            # Family-repeat 404/empty — fall back to guide-dir form.
            status2, nbytes2 = probe_root(guide_r, base_url=base_url, user_agent=user_agent)
            time.sleep(sleep_s)
            if status2 == 200 and nbytes2 > 0:
                d.chosen_root = guide_r
                d.derivation = "guide_dir_fallback"
                d.http_status = status2
                d.bytes = nbytes2
                d.resolves = True
            else:
                d.derivation = "unresolved"
                d.chosen_root = None
                d.resolves = False
        else:
            d.derivation = "unresolved"
            d.resolves = False
        time.sleep(sleep_s)
        out.append(d)
    return out


def split_root_sections(
    text: str,
    *,
    root_path: str,
    base_url: str = DEFAULT_BASE,
) -> List[Section]:
    """Split a product root into addressable documents by heading {#anchor}s."""
    raw = text.encode("utf-8")
    # Work in text space but record byte offsets via encode of prefixes.
    matches = list(_ANCHORED_HEADING.finditer(text))
    if not matches:
        return []

    live_base = root_path
    if live_base.endswith(".md"):
        live_base = live_base[:-3] + ".html"

    sections: List[Section] = []
    for i, m in enumerate(matches):
        if m.group(1) is not None:
            level = len(m.group(1))
            title = m.group(2).strip()
            anchor = m.group(3).strip()
        else:
            title = m.group(4).strip()
            anchor = m.group(5).strip()
            underline = m.group(6) or "="
            level = 1 if underline.startswith("=") else 2

        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        byte_start = len(text[:start].encode("utf-8"))
        byte_end = len(text[:end].encode("utf-8"))
        # Prefer exact end on the final section = full file bytes.
        if i + 1 == len(matches):
            byte_end = len(raw)

        deep_link = f"{base_url.rstrip('/')}{live_base}#{anchor}"
        sections.append(
            Section(
                anchor=anchor,
                title=title,
                byte_start=byte_start,
                byte_end=byte_end,
                deep_link=deep_link,
                heading_level=level,
            )
        )
    return sections


def _normalize_for_containment(text: str) -> str:
    t = re.sub(r"\{#[^}]+\}", " ", text)
    t = re.sub(r"(?m)^[=-]{3,}\s*$", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def toc_page_covered_by_root(page_text: str, root_text: str, root_anchors: set) -> bool:
    """True when the TOC page's anchors or distinctive prose appear in the root."""
    page_anchors = set(re.findall(r"\{#([^}]+)\}", page_text))
    if page_anchors & root_anchors:
        return True
    page_n = _normalize_for_containment(page_text)
    root_n = _normalize_for_containment(root_text)
    if len(page_n) < 40:
        # Tiny stub — treat title match as coverage if present.
        m = re.search(r"(?m)^(?:#{1,6}\s+)?(.+?)\s*\{#", page_text)
        return bool(m and m.group(1).strip() in root_text)
    # Distinctive window from the page body.
    start = min(40, max(0, len(page_n) // 10))
    snippet = page_n[start : start + 80]
    if len(snippet) >= 40 and snippet in root_n:
        return True
    # Fallback: first heading title.
    m = re.search(r"(?m)^(?:#{1,6}\s+)?(.+?)\s*\{#", page_text)
    if m and m.group(1).strip() and m.group(1).strip() in root_text:
        return True
    return False


def product_id_from_root(root_path: str) -> str:
    name = Path(root_path).stem
    return name


def fetch_product_root(
    root_path: str,
    *,
    base_url: str,
    out_dir: Path,
    root: Path,
    strip_prefix: str = "/docs/cybs/",
    user_agent: str = DEFAULT_UA,
) -> Tuple[int, bytes, Optional[str], Optional[str]]:
    """Fetch one root verbatim into raw/. Returns status, body, local_path, error."""
    url = urljoin(base_url, root_path)
    try:
        code, body, _ = http_get(url, user_agent=user_agent)
    except Exception as e:  # noqa: BLE001
        return 0, b"", None, str(e)
    if code != 200 or not body:
        return code, body or b"", None, f"HTTP {code}"
    text = body.decode("utf-8", errors="replace")
    if not looks_like_markdown(text):
        return code, body, None, "not markdown"
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / url_to_local_name(root_path[:-3] if root_path.endswith(".md") else root_path, strip_prefix=strip_prefix)
    # Roots keep the product filename; url_to_local_name adds .md.md — fine, matches corpus.
    if not text.endswith("\n"):
        text = text + "\n"
        body = text.encode("utf-8")
    dest.write_text(text, encoding="utf-8")
    local = str(dest.relative_to(root) if dest.is_relative_to(root) else dest)
    return code, body, local, None


def cross_check_toc(
    root_path: str,
    root_text: str,
    *,
    base_url: str,
    user_agent: str = DEFAULT_UA,
    sleep_s: float = 0.05,
    local_guides_dir: Optional[Path] = None,
    limit: Optional[int] = None,
) -> Tuple[int, int, List[str]]:
    """TOC is a cross-check only. Return (toc_topics, covered, uncovered_paths)."""
    html_path = root_path[:-3] + ".html" if root_path.endswith(".md") else root_path + ".html"
    # path filter: the directory that contains the guide (parent of root file stem)
    # e.g. /docs/.../rest/boarding.md -> must contain /docs/.../rest/boarding
    stem_path = root_path[:-3] if root_path.endswith(".md") else root_path
    code, body, _ = http_get(urljoin(base_url, html_path), user_agent=user_agent)
    if code != 200 or not body:
        return 0, 0, [f"<<toc_seed_failed HTTP {code}>>"]
    topics = extract_toc_topics(body.decode("utf-8", errors="replace"), base_url, stem_path)
    # Exclude the root itself from the TOC page list.
    topics = [t for t in topics if t.rstrip("/") != stem_path.rstrip("/")]
    if limit is not None:
        topics = topics[:limit]

    root_anchors = set(re.findall(r"\{#([^}]+)\}", root_text))
    uncovered: List[str] = []
    covered = 0

    for topic in topics:
        page_text: Optional[str] = None
        if local_guides_dir is not None:
            local_name = url_to_local_name(topic, strip_prefix="/docs/cybs/")
            local_file = local_guides_dir / local_name
            if local_file.is_file():
                page_text = local_file.read_text(encoding="utf-8", errors="replace")
        if page_text is None:
            md_url = urljoin(base_url, topic + ".md")
            try:
                c, b, _ = http_get(md_url, user_agent=user_agent)
                if c == 200 and b and looks_like_markdown(b.decode("utf-8", errors="replace")):
                    page_text = b.decode("utf-8", errors="replace")
            except Exception:  # noqa: BLE001
                page_text = None
            time.sleep(sleep_s)
        if page_text is None:
            uncovered.append(topic)
            continue
        if toc_page_covered_by_root(page_text, root_text, root_anchors):
            covered += 1
        else:
            uncovered.append(topic)
    return len(topics), covered, uncovered


def fetch_product_roots(
    products: Sequence[ProductLink],
    *,
    base_url: str = DEFAULT_BASE,
    out_dir: Path,
    root: Path,
    sections_dir: Path,
    strip_prefix: str = "/docs/cybs/",
    sleep_s: float = 0.08,
    user_agent: str = DEFAULT_UA,
    cross_check: bool = True,
    local_guides_dirs: Optional[Dict[str, Path]] = None,
    toc_limit: Optional[int] = None,
    extra_products: Optional[Sequence[ProductLink]] = None,
) -> Dict[str, object]:
    """Fetch each product root into raw/, split sections, TOC cross-check."""
    all_products = list(products)
    if extra_products:
        seen = {p.intro_path for p in all_products}
        for p in extra_products:
            if p.intro_path not in seen:
                all_products.append(p)

    derivations = resolve_products(
        all_products, base_url=base_url, user_agent=user_agent, sleep_s=sleep_s, probe=True
    )
    reports: List[ProductRootReport] = []
    sections_dir.mkdir(parents=True, exist_ok=True)

    for d in derivations:
        pid_guess = product_id_from_root(d.chosen_root) if d.chosen_root else (d.family or "unknown")
        if not d.resolves or not d.chosen_root:
            reports.append(
                ProductRootReport(
                    product_id=pid_guess,
                    title=d.title,
                    intro_path=d.intro_path,
                    root_path=d.chosen_root or "",
                    root_url="",
                    derivation=d.derivation,
                    http_status=d.http_status or 0,
                    bytes=0,
                    local_path=None,
                    sections_split=0,
                    toc_topics=0,
                    toc_covered=0,
                    toc_uncovered=[],
                    error="root does not resolve" if d.derivation != "not_md" else "not an .md product link",
                )
            )
            continue

        code, body, local, err = fetch_product_root(
            d.chosen_root,
            base_url=base_url,
            out_dir=out_dir,
            root=root,
            strip_prefix=strip_prefix,
            user_agent=user_agent,
        )
        time.sleep(sleep_s)
        text = body.decode("utf-8", errors="replace") if body else ""
        sections = split_root_sections(text, root_path=d.chosen_root, base_url=base_url) if text else []
        pid = product_id_from_root(d.chosen_root)
        sec_path = sections_dir / f"{pid}.sections.json"
        sec_path.write_text(
            json.dumps(
                {
                    "product_id": pid,
                    "root_path": d.chosen_root,
                    "root_url": urljoin(base_url, d.chosen_root),
                    "bytes": len(body),
                    "sections": [asdict(s) for s in sections],
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        toc_topics = toc_covered = 0
        uncovered: List[str] = []
        if cross_check and not err:
            guides = None
            if local_guides_dirs:
                guides = local_guides_dirs.get(pid)
            toc_topics, toc_covered, uncovered = cross_check_toc(
                d.chosen_root,
                text,
                base_url=base_url,
                user_agent=user_agent,
                sleep_s=sleep_s,
                local_guides_dir=guides,
                limit=toc_limit,
            )

        fences = len(re.findall(r"(?m)^```", text)) // 2
        reports.append(
            ProductRootReport(
                product_id=pid,
                title=d.title,
                intro_path=d.intro_path,
                root_path=d.chosen_root,
                root_url=urljoin(base_url, d.chosen_root),
                derivation=d.derivation,
                http_status=code,
                bytes=len(body),
                local_path=local,
                sections_split=len(sections),
                toc_topics=toc_topics,
                toc_covered=toc_covered,
                toc_uncovered=uncovered,
                code_fences=fences,
                error=err,
            )
        )

    return {
        "generated_at": _utc_now(),
        "denominator_rule": (
            "Coverage denominator is the product root mega-guide fetched "
            "verbatim from the vendor site. The family HTML TOC is a "
            "cross-check only: report TOC pages whose content does not "
            "appear in the root."
        ),
        "denominator_source": "product_root",
        "docs_md_url": DEFAULT_DOCS_MD,
        "derivations": [asdict(d) for d in derivations],
        "totals": {
            "products_listed": len(all_products),
            "roots_resolved": sum(1 for d in derivations if d.resolves),
            "roots_fetched": sum(1 for r in reports if r.local_path),
            "bytes": sum(r.bytes for r in reports),
            "sections_split": sum(r.sections_split for r in reports),
            "toc_topics": sum(r.toc_topics for r in reports),
            "toc_covered": sum(r.toc_covered for r in reports),
            "toc_uncovered": sum(len(r.toc_uncovered) for r in reports),
        },
        "products": [asdict(r) for r in reports],
        "out_dir": str(out_dir),
        "sections_dir": str(sections_dir),
    }


def render_report_md(report: Dict[str, object]) -> str:
    lines = [
        "# Product-root corpus report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"Denominator source: `{report['denominator_source']}`",
        "",
        report["denominator_rule"],  # type: ignore[index]
        "",
        "## Derivation probe",
        "",
        "docs.md links point at intro subtopics. Root = guide directory as "
        "`.md` at its parent (family name repeated when guide folder == family).",
        "",
        "| Product | Derivation | Root | HTTP | Bytes | Resolves |",
        "|---|---|---|---:|---:|---|",
    ]
    for d in report["derivations"]:  # type: ignore[index]
        root = d.get("chosen_root") or d.get("family_repeat_root") or "—"
        lines.append(
            f"| {d['title']} | {d['derivation']} | `{root}` | "
            f"{d.get('http_status') or '—'} | {d.get('bytes') or 0} | "
            f"{'yes' if d.get('resolves') else 'no'} |"
        )

    unresolved = [d for d in report["derivations"] if not d.get("resolves")]  # type: ignore[index]
    lines += ["", f"Unresolved: **{len(unresolved)}** / {len(report['derivations'])}"]  # type: ignore[index]
    for d in unresolved:
        lines.append(
            f"- {d['title']}: intro `{d['intro_path']}` "
            f"(family_repeat=`{d.get('family_repeat_root')}`, "
            f"guide_dir=`{d.get('guide_dir_root')}`, how={d['derivation']})"
        )

    lines += [
        "",
        "## Per product",
        "",
        "| Product | Root fetched | Bytes | Sections | Code fences | TOC topics | TOC covered | TOC gaps |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in report["products"]:  # type: ignore[index]
        lines.append(
            f"| {r['title']} | `{r['root_path'] or '—'}` | {r['bytes']} | "
            f"{r['sections_split']} | {r['code_fences']} | {r['toc_topics']} | "
            f"{r['toc_covered']} | {len(r['toc_uncovered'])} |"
        )

    lines += ["", "## TOC pages not covered by root (real gaps)", ""]
    any_gap = False
    for r in report["products"]:  # type: ignore[index]
        if not r["toc_uncovered"]:
            continue
        any_gap = True
        lines.append(f"### {r['title']} (`{r['product_id']}`)")
        lines.append("")
        for t in r["toc_uncovered"]:
            lines.append(f"- `{t}`")
        lines.append("")
    if not any_gap:
        lines.append("None — every fetched TOC page's content appears in its product root.")
        lines.append("")

    totals = report["totals"]  # type: ignore[index]
    lines += [
        "## Totals",
        "",
        f"- Products listed: {totals['products_listed']}",
        f"- Roots resolved: {totals['roots_resolved']}",
        f"- Roots fetched: {totals['roots_fetched']}",
        f"- Bytes: {totals['bytes']}",
        f"- Sections split: {totals['sections_split']}",
        f"- TOC topics checked: {totals['toc_topics']} "
        f"(covered {totals['toc_covered']}, gaps {totals['toc_uncovered']})",
        "",
    ]
    return "\n".join(lines)


def write_reports(report: Dict[str, object], report_dir: Path, *, stem: str = "product-roots-report") -> Tuple[Path, Path]:
    report_dir.mkdir(parents=True, exist_ok=True)
    jp = report_dir / f"{stem}.json"
    mp = report_dir / f"{stem}.md"
    jp.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    mp.write_text(render_report_md(report), encoding="utf-8")
    return jp, mp
