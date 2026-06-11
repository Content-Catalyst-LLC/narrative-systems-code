from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import MonomythClaim
from .validation import validate_monomyth_claim
from .scoring import (
    monomyth_pattern,
    specificity_preservation,
    formula_drift,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_claims(path: Path) -> list[MonomythClaim]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        claims: list[MonomythClaim] = []

        for row in rows:
            claim = MonomythClaim(
                item=row["item"],
                claim_context=row["claim_context"],
                departure_pattern=float(row["departure_pattern"]),
                threshold_crossing=float(row["threshold_crossing"]),
                initiation_trial=float(row["initiation_trial"]),
                descent_symbolic_death=float(row["descent_symbolic_death"]),
                boon=float(row["boon"]),
                return_pattern=float(row["return_pattern"]),
                language_notes=float(row["language_notes"]),
                cultural_tradition=float(row["cultural_tradition"]),
                ritual_context=float(row["ritual_context"]),
                historical_context=float(row["historical_context"]),
                oral_performance_context=float(row["oral_performance_context"]),
                authority_notes=float(row["authority_notes"]),
                stage_literalism=float(row["stage_literalism"]),
                beat_matching=float(row["beat_matching"]),
                context_loss=float(row["context_loss"]),
                overfitting=float(row["overfitting"]),
                universal_claim_strength=float(row["universal_claim_strength"]),
                counterexample_inclusion=float(row["counterexample_inclusion"]),
                method_limits=float(row["method_limits"]),
                ethics_governance=float(row["ethics_governance"]),
                ritual_verification=float(row["ritual_verification"]),
                uncertainty_marking=float(row["uncertainty_marking"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_monomyth_claim(claim)
            claims.append(claim)

    return claims


def claim_to_row(claim: MonomythClaim) -> dict[str, object]:
    row = {
        "item": claim.item,
        "claim_context": claim.claim_context,
        "monomyth_pattern": round(monomyth_pattern(claim), 3),
        "specificity_preservation": round(specificity_preservation(claim), 3),
        "formula_drift": round(formula_drift(claim), 3),
        "interpretation_readiness": round(interpretation_readiness(claim), 3),
        "governance_priority_score": round(governance_priority_score(claim), 3),
        "review_priority": review_priority(claim),
        "owner": claim.owner,
        "status": claim.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "monomyth_claims.csv"
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
            float(row["formula_drift"])
        ),
        reverse=True,
    )

    governance_queue = [row for row in rows if row["review_priority"] != "standard"]

    write_csv(tables / "monomyth_claim_audit.csv", rows)
    write_csv(tables / "monomyth_claim_governance_queue.csv", governance_queue)

    write_json(json_dir / "monomyth_claim_canvas_cards.json", rows)
    write_json(json_dir / "monomyth_claim_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "monomyth_claim_governance_queue.md", governance_queue)

    print("Monomyth Canvas audit complete.")
    print(tables / "monomyth_claim_audit.csv")
    print(json_dir / "monomyth_claim_canvas_cards.json")
    print(markdown / "monomyth_claim_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run monomyth Canvas audit.")
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
