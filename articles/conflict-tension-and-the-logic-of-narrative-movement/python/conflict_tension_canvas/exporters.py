from __future__ import annotations

from pathlib import Path
import csv
import json


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_markdown_queue(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Conflict and Tension Governance Queue",
        "",
        "| Item | Type | Conflict clarity | Tension durability | Movement | Risk | Priority | Owner |",
        "|---|---|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['item']} | {row['story_type']} | "
            f"{row['conflict_clarity']} | {row['tension_durability']} | "
            f"{row['narrative_movement']} | {row['conflict_risk']} | "
            f"{row['review_priority']} | {row['owner']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
