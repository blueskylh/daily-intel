from __future__ import annotations

from datetime import date


def summarize_day(day: date, index: int, notes: list[str] | None = None) -> str:
    notes = notes or ["daily update recorded"]
    lines = [
        f"# Daily Update {day.isoformat()}",
        "",
        f"- update index: {index}",
        "- dataset refreshed: yes",
    ]
    for note in notes:
        lines.append(f"- {note}")
    return "\n".join(lines) + "\n"
