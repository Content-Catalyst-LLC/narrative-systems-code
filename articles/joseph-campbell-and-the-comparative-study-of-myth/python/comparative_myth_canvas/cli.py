from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import ComparativeMythClaim
from .validation import validate_comparative_myth_claim
from .scoring import (
    comparative_pattern,
    cultural_specificity,
    generalization_risk,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_claims(path: Path) -> list[ComparativeMythClaim]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        claims: list[ComparativeMythClaim] = []

        for row in rows:
            claim = ComparativeMythClaim(
                item=row["item"],
                claim_context=row["claim_context"],
                departure_pattern=float(row["departure_pattern"]),
                threshold_crossing=float(row["threshold_crossing"]),
                ordeal_or_trial=float(row["ordeal_or_trial"]),
                helper_presence=float(row["helper_presence"]),
                return_pattern=float(row["return_pattern"]),
                boon_or_renewal=float(row["boon_or_renewal"]),
                language_notes=float(row["language_notes"]),
                ritual_context=float(row["ritual_context"]),
                historical_context=float(row["historical_context"]),
                community_authority=float(row["community_authority"]),
                source_tradition=float(row["source_tradition"]),
                performance_or_oral_context=float(row["performance_or_oral_context"]),
                universal_claim_strength=float(row["universal_claim_strength"]),
                selective_evidence=float(row["selective_evidence"]),
                context_loss=float(row["context_loss"]),
                formula_reduction=float(row["formula_reduction"]),
                ethical_risk=float(row["ethical_risk"]),
                counterexample_inclusion=float(row["counterexample_inclusion"]),
                method_limits=float(row["method_limits"]),
                ritual_verification=float(row["ritual_verification"]),
                ethics_governance=float(row["ethics_governance"]),
                uncertainty_marking=float(row["uncertainty_marking"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_comparative_myth_claim(claim)
            claims.append(claim)

    return claims


def claim_to_row(claim: ComparativeMythClaim) -> dict[str, object]:
    row = {
        "item": claim.item,
        "claim_context": claim.claim_context,
        "comparative_pattern": round(comparative_pattern(claim), 3),
        "cultural_specificity": round(cultural_specificity(claim), 3),
        "generalization_risk": round(generalization_risk(claim), 3),
        "interpretation_readiness": round(interpretation_readiness(claim), 3),
        "governance_priority_score": round(governance_priority_score(claim), 3),
        "review_priority": review_priority(claim),
        "owner": claim.owner,
        "status": claim.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "comparative_myth_claims.csv"
    outputs = article_root / "outputs"
    tables = outputs / "tables"
    json_dir = outputs / "json"
    markdown = outputs / "markdown"
    canvas = article_root / "canvas"

    claims = load_claims(data_path)
    rows = [claim_to_row(claim) for claim in claims]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(
        rows,
        key=lambda row: (
            priority_order.get(str(row["review_priority"]), 0),
            float(row["generalization_risk"])
        ),
        reverse=True,
    )

    governance_queue = [row for row in rows if row["review_priority"] != "standard"]

    write_csv(tables / "comparative_myth_claim_audit.csv", rows)
    write_csv(tables / "comparative_myth_claim_governance_queue.csv", governance_queue)

    write_json(json_dir / "comparative_myth_claim_canvas_cards.json", rows)
    write_json(json_dir / "comparative_myth_claim_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "comparative_myth_claim_governance_queue.md", governance_queue)

    print("Comparative myth Canvas audit complete.")
    print(tables / "comparative_myth_claim_audit.csv")
    print(json_dir / "comparative_myth_claim_canvas_cards.json")
    print(markdown / "comparative_myth_claim_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run comparative myth Canvas audit.")
    parser.add_argument(
        "--article-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Path to article root directory.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    run(args.article_root.resolve())


if __name__ == "__main__":
    main()
