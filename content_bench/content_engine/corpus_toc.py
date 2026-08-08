"""Resumable TOC completeness cross-check for product roots.

TOC walks can run for hours across 171+ families. State is checkpointed per
product so a failure at hour two does not restart at zero. Prefer local
guides cache (cybersource-docs/) before live HTTP fetches.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set

from content_bench.content_engine.product_roots import (
    DEFAULT_BASE,
    cross_check_toc,
    product_id_from_root,
)
from content_bench.content_engine.toc_fetch import url_to_local_name

DEFAULT_UA = "Content-Bench/1.0 (corpus-toc)"


@dataclass
class TocProductResult:
    product_id: str
    root_path: str
    toc_topics: int = 0
    toc_covered: int = 0
    toc_missed: List[str] = field(default_factory=list)
    status: str = "pending"  # pending | done | failed
    error: Optional[str] = None
    cache_hits: int = 0
    live_fetches: int = 0


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _state_path(checkpoint_dir: Path) -> Path:
    return checkpoint_dir / "toc-checkpoint.json"


def load_checkpoint(checkpoint_dir: Path) -> Dict[str, object]:
    p = _state_path(checkpoint_dir)
    if not p.is_file():
        return {"completed": [], "products": {}}
    return json.loads(p.read_text(encoding="utf-8"))


def save_checkpoint(checkpoint_dir: Path, state: Dict[str, object]) -> None:
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = _utc_now()
    _state_path(checkpoint_dir).write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def _resolve_local_guide(
    topic_path: str,
    local_guides_dirs: Sequence[Path],
) -> Optional[Path]:
    name = url_to_local_name(topic_path, strip_prefix="/docs/cybs/")
    for d in local_guides_dirs:
        candidate = d / name
        if candidate.is_file():
            return candidate
    return None


def cross_check_toc_resumable(
    products: Sequence[Dict[str, str]],
    *,
    base_url: str = DEFAULT_BASE,
    checkpoint_dir: Path,
    local_guides_dirs: Optional[Sequence[Path]] = None,
    raw_dir: Optional[Path] = None,
    sleep_s: float = 0.08,
    user_agent: str = DEFAULT_UA,
    limit: Optional[int] = None,
) -> Dict[str, object]:
    """Run TOC cross-check with per-product checkpointing.

    ``products`` is a list of ``{root_path, local_path?, text?}`` for fetched roots.
    """
    state = load_checkpoint(checkpoint_dir)
    completed: Set[str] = set(state.get("completed") or [])
    product_state: Dict[str, dict] = dict(state.get("products") or {})
    guides = list(local_guides_dirs or [])

    # Also treat cybersource-docs at repo root as cache
    results: List[TocProductResult] = []

    for prod in products:
        root_path = prod["root_path"]
        pid = product_id_from_root(root_path)

        if pid in completed:
            prev = product_state.get(pid, {})
            results.append(
                TocProductResult(
                    product_id=pid,
                    root_path=root_path,
                    toc_topics=prev.get("toc_topics", 0),
                    toc_covered=prev.get("toc_covered", 0),
                    toc_missed=prev.get("toc_missed", []),
                    status="done",
                    cache_hits=prev.get("cache_hits", 0),
                    live_fetches=prev.get("live_fetches", 0),
                )
            )
            continue

        # Load root text from raw file or inline
        root_text = prod.get("text")
        if root_text is None and raw_dir and prod.get("local_path"):
            raw_file = raw_dir / prod["local_path"]
            if raw_file.is_file():
                root_text = raw_file.read_text(encoding="utf-8", errors="replace")
        if not root_text:
            tr = TocProductResult(
                product_id=pid,
                root_path=root_path,
                status="failed",
                error="no root text available",
            )
            results.append(tr)
            continue

        # Pick best local cache dir for this product
        local_dir: Optional[Path] = None
        for d in guides:
            if d.is_dir():
                local_dir = d
                break

        try:
            toc_topics, toc_covered, missed = cross_check_toc(
                root_path,
                root_text,
                base_url=base_url,
                user_agent=user_agent,
                sleep_s=sleep_s,
                local_guides_dir=local_dir,
                limit=limit,
            )
            tr = TocProductResult(
                product_id=pid,
                root_path=root_path,
                toc_topics=toc_topics,
                toc_covered=toc_covered,
                toc_missed=missed,
                status="done",
            )
        except Exception as e:  # noqa: BLE001
            tr = TocProductResult(
                product_id=pid,
                root_path=root_path,
                status="failed",
                error=str(e),
            )

        results.append(tr)
        if tr.status == "done":
            completed.add(pid)
            product_state[pid] = {
                "root_path": root_path,
                "toc_topics": tr.toc_topics,
                "toc_covered": tr.toc_covered,
                "toc_missed": tr.toc_missed,
                "cache_hits": tr.cache_hits,
                "live_fetches": tr.live_fetches,
            }
            state["completed"] = sorted(completed)
            state["products"] = product_state
            save_checkpoint(checkpoint_dir, state)
        time.sleep(sleep_s)

    totals = {
        "products": len(results),
        "done": sum(1 for r in results if r.status == "done"),
        "failed": sum(1 for r in results if r.status == "failed"),
        "toc_topics": sum(r.toc_topics for r in results),
        "toc_covered": sum(r.toc_covered for r in results),
        "toc_missed": sum(len(r.toc_missed) for r in results),
    }

    return {
        "generated_at": _utc_now(),
        "denominator_source": "site_html_toc_per_family",
        "totals": totals,
        "products": [asdict(r) for r in results],
        "checkpoint_dir": str(checkpoint_dir),
    }
