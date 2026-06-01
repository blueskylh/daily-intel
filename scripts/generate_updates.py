from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

from daily_intel_900.summarizer import summarize_day

TARGET = 900


def main(start_index: int = 1) -> int:
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"
    data_dir.mkdir(exist_ok=True)

    start_date = date.today() - timedelta(days=TARGET - 1)
    for i in range(start_index, TARGET + 1):
        day = start_date + timedelta(days=i - 1)
        path = data_dir / f"{day.isoformat()}.md"
        path.write_text(summarize_day(day, i), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 1))
