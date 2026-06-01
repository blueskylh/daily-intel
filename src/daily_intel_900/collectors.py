from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class MetricSnapshot:
    source: str
    metric_name: str
    value: float
    captured_at: str


def build_snapshot(now: datetime | None = None) -> MetricSnapshot:
    now = now or datetime.now(timezone.utc)
    return MetricSnapshot(source="local-sensor", metric_name="stability_index", value=1.0, captured_at=now.isoformat())
