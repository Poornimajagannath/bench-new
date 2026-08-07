"""Content Bench Content Engine V0 — local compiled content prototype.

Default extract is heuristic (no docetl import). Optional `--discovery docetl`
runs the real DocETL package via code_map. No Tempo/Harbor runner.
"""

from content_bench.content_engine.pipeline import run_content_engine

__all__ = ["run_content_engine"]
