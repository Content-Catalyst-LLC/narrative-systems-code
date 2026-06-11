#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
import json
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_ROOT = ARTICLE_ROOT / "python"
if str(PYTHON_ROOT) not in sys.path:
    sys.path.insert(0, str(PYTHON_ROOT))

from heros_journey_canvas.scoring import (  # noqa: E402
    HerosJourneyClaim,
    journey_structure,
    formula_drift,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)


def load_claims(path: Path) -> list[HerosJourneyClaim]:
    rows: list[HerosJourneyClaim] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows.append(HerosJourneyClaim(
                item=row["item"],
                claim_context=row["claim_context"],
                departure_pattern=float(row["departure_pattern"]),
                threshold_crossing=float(row["threshold_crossing"]),
                initiation_trial=float(row["initiation_trial"]),
                descent_symbolic_death=float(row["descent_symbolic_death"]),
                boon=float(row["boon"]),
                return_pattern=float(row["return_pattern"]),
                transformation_depth=float(row["transformation_depth"]),
                return_responsibility=float(row["return_responsibility"]),
                specificity_preservation=float(row["specificity_preservation"]),
                stage_literalism=float(row["stage_literalism"]),
                beat_matching=float(row["beat_matching"]),
                context_loss=float(row["context_loss"]),
                overfitting=float(row["overfitting"]),
                universal_claim_strength=float(row["universal_claim_strength"]),
                counterexample_inclusion=float(row["counterexample_inclusion"]),
                method_limits=float(row["method_limits"]),
                ethics_governance=float(row["ethics_governance"]),
                uncertainty_marking=float(row["uncertainty_marking"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            ))
    return rows


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
        "# Hero's Journey Governance Queue",
        "",
        "| Item | Context | Journey | Transformation | Return responsibility | Formula drift | Readiness | Priority |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['item']} | {row['claim_context']} | {row['journey_structure']} | "
            f"{row['transformation_depth']} | {row['return_responsibility']} | "
            f"{row['formula_drift']} | {row['interpretation_readiness']} | {row['review_priority']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    claims = load_claims(ARTICLE_ROOT / "data" / "heros_journey_claims.csv")
    rows: list[dict[str, object]] = []

    for claim in claims:
        rows.append({
            "item": claim.item,
            "claim_context": claim.claim_context,
            "journey_structure": round(journey_structure(claim), 3),
            "transformation_depth": round(claim.transformation_depth, 3),
            "return_responsibility": round(claim.return_responsibility, 3),
            "specificity_preservation": round(claim.specificity_preservation, 3),
            "formula_drift": round(formula_drift(claim), 3),
            "interpretation_readiness": round(interpretation_readiness(claim), 3),
            "governance_priority_score": round(governance_priority_score(claim), 3),
            "review_priority": review_priority(claim),
            "owner": claim.owner,
            "status": claim.status,
        })

    priority = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority[str(row["review_priority"])], float(row["formula_drift"])), reverse=True)
    queue = [row for row in rows if row["review_priority"] != "standard"]

    write_csv(ARTICLE_ROOT / "outputs" / "tables" / "heros_journey_audit.csv", rows)
    write_csv(ARTICLE_ROOT / "outputs" / "tables" / "heros_journey_governance_queue.csv", queue)
    write_json(ARTICLE_ROOT / "outputs" / "json" / "heros_journey_canvas_cards.json", rows)
    write_json(ARTICLE_ROOT / "outputs" / "json" / "heros_journey_governance_queue.json", queue)
    write_json(ARTICLE_ROOT / "canvas" / "canvas_cards.json", rows)
    write_json(ARTICLE_ROOT / "canvas" / "governance_queue.json", queue)
    write_markdown_queue(ARTICLE_ROOT / "outputs" / "markdown" / "heros_journey_governance_queue.md", queue)

    print("Hero's Journey Canvas audit complete.")
    print(ARTICLE_ROOT / "outputs" / "tables" / "heros_journey_audit.csv")


if __name__ == "__main__":
    main()
