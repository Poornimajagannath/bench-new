"""Relay Content Engine V0 — local compiled content prototype.

Honest label: DocETL-style extraction only. No live fetch, no docetl import,
no Tempo/Harbor runner, no production Relay edits.
"""

from relay_bench.content_engine.pipeline import run_content_engine

__all__ = ["run_content_engine"]
