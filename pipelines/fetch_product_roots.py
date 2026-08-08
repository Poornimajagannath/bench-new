#!/usr/bin/env python3
"""Fetch CyberSource product roots — thin CLI over product_roots.

The product root mega-guide is the corpus source of truth and coverage
denominator. docs.md supplies the product list (intro links); roots are
derived, fetched verbatim into raw/, split by section anchors, and checked
against each family's HTML TOC.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.product_roots import (  # noqa: E402
    DEFAULT_BASE,
    DEFAULT_DOCS_MD,
    ProductLink,
    fetch_docs_md,
    fetch_product_roots,
    parse_docs_md_products,
    write_reports,
)

UA = "CyberSource-Relay/1.0 (product-roots-fetch)"

# Boarding is the motivating evidence case but is not on the docs.md hub card
# list (hub links popular payments products). Include it explicitly.
BOARDING_EXTRA = ProductLink(
    title="Boarding REST",
    intro_path="/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro.md",
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "raw" / "product-roots",
        help="Directory for verbatim root files (under raw/)",
    )
    ap.add_argument(
        "--sections-dir",
        type=Path,
        default=ROOT / "artifacts" / "content_engine" / "product_roots" / "sections",
        help="Directory for per-root section index JSON",
    )
    ap.add_argument(
        "--report-dir",
        type=Path,
        default=ROOT / "artifacts" / "content_engine" / "product_roots",
        help="Directory for JSON + markdown reports",
    )
    ap.add_argument("--docs-md-url", default=DEFAULT_DOCS_MD)
    ap.add_argument("--base-url", default=DEFAULT_BASE)
    ap.add_argument("--sleep", type=float, default=0.08)
    ap.add_argument("--no-cross-check", action="store_true")
    ap.add_argument(
        "--toc-limit",
        type=int,
        default=None,
        help="Optional cap on TOC pages checked per product (debug)",
    )
    ap.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Optional product-id filter (root stem), e.g. boarding payments tms",
    )
    args = ap.parse_args()

    docs_text = fetch_docs_md(docs_md_url=args.docs_md_url, user_agent=UA)
    products = parse_docs_md_products(docs_text)
    extras = [BOARDING_EXTRA]

    if args.only:
        only = set(args.only)

        def _wanted(p: ProductLink) -> bool:
            from content_bench.content_engine.product_roots import derive_product_root

            chosen, _, _, _ = derive_product_root(p.intro_path)
            if not chosen:
                return p.title.lower().replace(" ", "-") in only
            return Path(chosen).stem in only

        products = [p for p in products if _wanted(p)]
        extras = [p for p in extras if _wanted(p)]

    local_guides = {
        "boarding": ROOT / "data" / "products" / "boarding" / "guides",
        "payments": ROOT / "data" / "products" / "payments" / "guides",
    }

    report = fetch_product_roots(
        products,
        base_url=args.base_url,
        out_dir=args.out_dir,
        root=ROOT,
        sections_dir=args.sections_dir,
        sleep_s=args.sleep,
        user_agent=UA,
        cross_check=not args.no_cross_check,
        local_guides_dirs=local_guides,
        toc_limit=args.toc_limit,
        extra_products=extras,
    )

    jp, mp = write_reports(report, args.report_dir)
    print(f"wrote {jp}")
    print(f"wrote {mp}")
    print(
        f"fetched {report['totals']['roots_fetched']} roots, "
        f"{report['totals']['bytes']} bytes, "
        f"{report['totals']['sections_split']} sections; "
        f"TOC gaps {report['totals']['toc_uncovered']}/"
        f"{report['totals']['toc_topics']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
