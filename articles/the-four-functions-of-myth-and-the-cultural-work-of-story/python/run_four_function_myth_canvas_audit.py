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

from four_function_myth_canvas.scoring import (  # noqa: E402
    MythFunctionClaim,
    function_balance,
    cultural_work,
    sociological_risk,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)


def load_claims(path: Path) -> list[MythFunctionClaim]:
    claims: list[MythFunctionClaim] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            claims.append(MythFunctionClaim(
                item=row["item"],
                claim_context=row["claim_context"],
                mystical_function=float(row["mystical_function"]),
                cosmological_function=float(row["cosmological_function"]),
                sociological_function=float(row["sociological_function"]),
                pedagogical_function=float(row["pedagogical_function"]),
                ritual_memory=float(row["ritual_memory"]),
                authority_clarity=float(row["authority_clarity"]),
                hierarchy_protection=float(row["hierarchy_protection"]),
                exclusion_risk=float(row["exclusion_risk"]),
                coercive_compliance=float(row["coercive_compliance"]),
                omission_risk=float(row["omission_risk"]),
                power_invisibility=float(row["power_invisibility"]),
                accountability_marking=float(row["accountability_marking"]),
                source_context=float(row["source_context"]),
                counterexample_inclusion=float(row["counterexample_inclusion"]),
                method_limits=float(row["method_limits"]),
                ethics_governance=float(row["ethics_governance"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            ))
    return claims


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
        "# Four-Function Myth Governance Queue",
        "",
        "| Item | Context | Cultural work | Balance | Sociological risk | Readiness | Priority |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['item']} | {row['claim_context']} | {row['cultural_work']} | "
            f"{row['function_balance']} | {row['sociological_risk']} | "
            f"{row['interpretation_readiness']} | {row['review_priority']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    claims = load_claims(ARTICLE_ROOT / "data" / "four_function_myth_claims.csv")
    rows: list[dict[str, object]] = []

    for claim in claims:
        rows.append({
            "item": claim.item,
            "claim_context": claim.claim_context,
            "mystical_function": round(claim.mystical_function, 3),
            "cosmological_function": round(claim.cosmological_function, 3),
            "sociological_function": round(claim.sociological_function, 3),
            "pedagogical_function": round(claim.pedagogical_function, 3),
            "function_balance": round(function_balance(claim), 3),
            "cultural_work": round(cultural_work(claim), 3),
            "sociological_risk": round(sociological_risk(claim), 3),
            "interpretation_readiness": round(interpretation_readiness(claim), 3),
            "governance_priority_score": round(governance_priority_score(claim), 3),
            "review_priority": review_priority(claim),
            "owner": claim.owner,
            "status": claim.status,
        })

    priority = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority[str(row["review_priority"])], float(row["sociological_risk"])), reverse=True)
    queue = [row for row in rows if row["review_priority"] != "standard"]

    write_csv(ARTICLE_ROOT / "outputs" / "tables" / "four_function_myth_audit.csv", rows)
    write_csv(ARTICLE_ROOT / "outputs" / "tables" / "four_function_myth_governance_queue.csv", queue)
    write_json(ARTICLE_ROOT / "outputs" / "json" / "four_function_myth_canvas_cards.json", rows)
    write_json(ARTICLE_ROOT / "outputs" / "json" / "four_function_myth_governance_queue.json", queue)
    write_json(ARTICLE_ROOT / "canvas" / "canvas_cards.json", rows)
    write_json(ARTICLE_ROOT / "canvas" / "governance_queue.json", queue)
    write_markdown_queue(ARTICLE_ROOT / "outputs" / "markdown" / "four_function_myth_governance_queue.md", queue)

    print("Four-function myth Canvas audit complete.")
    print(ARTICLE_ROOT / "outputs" / "tables" / "four_function_myth_audit.csv")


if __name__ == "__main__":
    main()
