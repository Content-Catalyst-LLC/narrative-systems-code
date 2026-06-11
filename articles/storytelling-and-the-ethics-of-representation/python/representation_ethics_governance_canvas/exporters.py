from __future__ import annotations

from pathlib import Path
import csv
import json
from typing import Any


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write: {path}")

    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_markdown_queue(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Representation Ethics Governance Queue",
        "",
        "| Item | Context | Integrity | Risk | Consent | AI risk | Priority | Owner |",
        "|---|---|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['item']} | {row['representation_context']} | "
            f"{row['representation_integrity']} | {row['representation_risk']} | "
            f"{row['consent_adequacy']} | {row['ai_representation_risk']} | "
            f"{row['review_priority']} | {row['owner']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
