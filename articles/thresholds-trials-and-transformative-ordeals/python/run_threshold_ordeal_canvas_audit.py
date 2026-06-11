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

from threshold_ordeal_canvas.scoring import (  # noqa: E402
    ThresholdOrdealClaim,
    ethical_risk,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)


def load_claims(path: Path) -> list[ThresholdOrdealClaim]:
    rows: list[ThresholdOrdealClaim] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows.append(ThresholdOrdealClaim(
                item=row["item"],
                claim_context=row["claim_context"],
                threshold_strength=float(row["threshold_strength"]),
                trial_depth=float(row["trial_depth"]),
                ordeal_transformation=float(row["ordeal_transformation"]),
                harm_romanticization=float(row["harm_romanticization"]),
                suffering_spectacle=float(row["suffering_spectacle"]),
                forced_closure=float(row["forced_closure"]),
                context_loss=float(row["context_loss"]),
                power_hiding=float(row["power_hiding"]),
                unresolved_marking=float(row["unresolved_marking"]),
                specificity_preservation=float(row["specificity_preservation"]),
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
        "# Threshold and Ordeal Governance Queue",
        "",
        "| Item | Context | Threshold | Trial depth | Ordeal transformation | Ethical risk | Readiness | Priority |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['item']} | {row['claim_context']} | {row['threshold_strength']} | "
            f"{row['trial_depth']} | {row['ordeal_transformation']} | "
            f"{row['ethical_risk']} | {row['interpretation_readiness']} | {row['review_priority']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    claims = load_claims(ARTICLE_ROOT / "data" / "threshold_ordeal_claims.csv")
    rows: list[dict[str, object]] = []

    for claim in claims:
        rows.append({
            "item": claim.item,
            "claim_context": claim.claim_context,
            "threshold_strength": round(claim.threshold_strength, 3),
            "trial_depth": round(claim.trial_depth, 3),
            "ordeal_transformation": round(claim.ordeal_transformation, 3),
            "ethical_risk": round(ethical_risk(claim), 3),
            "interpretation_readiness": round(interpretation_readiness(claim), 3),
            "governance_priority_score": round(governance_priority_score(claim), 3),
            "review_priority": review_priority(claim),
            "owner": claim.owner,
            "status": claim.status,
        })

    priority = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority[str(row["review_priority"])], float(row["ethical_risk"])), reverse=True)
    queue = [row for row in rows if row["review_priority"] != "standard"]

    write_csv(ARTICLE_ROOT / "outputs" / "tables" / "threshold_ordeal_audit.csv", rows)
    write_csv(ARTICLE_ROOT / "outputs" / "tables" / "threshold_ordeal_governance_queue.csv", queue)
    write_json(ARTICLE_ROOT / "outputs" / "json" / "threshold_ordeal_canvas_cards.json", rows)
    write_json(ARTICLE_ROOT / "outputs" / "json" / "threshold_ordeal_governance_queue.json", queue)
    write_json(ARTICLE_ROOT / "canvas" / "canvas_cards.json", rows)
    write_json(ARTICLE_ROOT / "canvas" / "governance_queue.json", queue)
    write_markdown_queue(ARTICLE_ROOT / "outputs" / "markdown" / "threshold_ordeal_governance_queue.md", queue)

    print("Threshold and ordeal Canvas audit complete.")
    print(ARTICLE_ROOT / "outputs" / "tables" / "threshold_ordeal_audit.csv")


if __name__ == "__main__":
    main()
