from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CanvasConfig:
    article_title: str
    article_slug: str
    metric_weights: dict[str, float]
    risk_weights: dict[str, float]
    readiness_weights: dict[str, float]
    thresholds: dict[str, float]


def weighted_average(values: dict[str, float], weights: dict[str, float]) -> float:
    denominator = sum(weights.values())
    if denominator <= 0:
        return 0.0
    numerator = sum(values.get(k, 0.0) * w for k, w in weights.items())
    return max(0.0, min(1.0, numerator / denominator))


def read_config(path: Path) -> CanvasConfig:
    data = json.loads(path.read_text(encoding="utf-8"))
    return CanvasConfig(
        article_title=data["article_title"],
        article_slug=data["article_slug"],
        metric_weights={k: float(v) for k, v in data["metric_weights"].items()},
        risk_weights={k: float(v) for k, v in data["risk_weights"].items()},
        readiness_weights={k: float(v) for k, v in data["readiness_weights"].items()},
        thresholds={k: float(v) for k, v in data["thresholds"].items()},
    )


def numeric_prefixed(row: dict[str, str], prefix: str) -> dict[str, float]:
    out: dict[str, float] = {}
    for key, value in row.items():
        if key.startswith(prefix) and value != "":
            out[key.removeprefix(prefix)] = float(value)
    return out


def priority(score: float, thresholds: dict[str, float]) -> str:
    if score >= thresholds["high"]:
        return "high"
    if score >= thresholds["medium"]:
        return "medium"
    return "standard"


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write: {path}")
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run(article_root: Path, strict: bool = False) -> None:
    config = read_config(article_root / "canvas" / "catalyst_canvas_config.json")
    rows: list[dict[str, Any]] = []
    cards: list[dict[str, Any]] = []
    with (article_root / "data" / "catalyst_canvas_assessment.csv").open("r", encoding="utf-8", newline="") as handle:
        for source in csv.DictReader(handle):
            metrics = numeric_prefixed(source, "metric_")
            risks = numeric_prefixed(source, "risk_")
            readiness = numeric_prefixed(source, "readiness_")
            if strict:
                for required, actual in [(config.metric_weights, metrics), (config.risk_weights, risks), (config.readiness_weights, readiness)]:
                    missing = set(required) - set(actual)
                    if missing:
                        raise ValueError(f"Missing strict fields: {sorted(missing)}")
            domain_strength = weighted_average(metrics, config.metric_weights)
            risk_score = weighted_average(risks, config.risk_weights)
            readiness_score = weighted_average(readiness, config.readiness_weights)
            governance_score = min(1.0, risk_score * 0.45 + (1 - readiness_score) * 0.35 + (1 - domain_strength) * 0.20)
            if source.get("status") == "review":
                governance_score = max(governance_score, config.thresholds["medium"])
            if source.get("status") == "revise":
                governance_score = max(governance_score, config.thresholds["high"])
            row = {
                "article_title": config.article_title,
                "article_slug": config.article_slug,
                "item": source["item"],
                "claim_context": source["claim_context"],
                "domain_strength": round(domain_strength, 4),
                "risk_score": round(risk_score, 4),
                "interpretation_readiness": round(readiness_score, 4),
                "governance_priority_score": round(governance_score, 4),
                "review_priority": priority(governance_score, config.thresholds),
                "owner": source.get("owner", "editorial"),
                "status": source.get("status", "active"),
                "governance_note": source.get("notes", ""),
            }
            rows.append(row)
            cards.append({
                "schema_version": "1.0.0",
                "card_type": "catalyst_canvas_article_governance",
                "article_title": config.article_title,
                "article_slug": config.article_slug,
                "item": row["item"],
                "scores": {
                    "domain_strength": row["domain_strength"],
                    "risk_score": row["risk_score"],
                    "interpretation_readiness": row["interpretation_readiness"],
                    "governance_priority_score": row["governance_priority_score"],
                },
                "review": {
                    "priority": row["review_priority"],
                    "owner": row["owner"],
                    "status": row["status"],
                    "governance_note": row["governance_note"],
                },
            })
    rows.sort(key=lambda r: r["governance_priority_score"], reverse=True)
    queue = [row for row in rows if row["review_priority"] != "standard"] or rows[:1]
    write_csv(article_root / "outputs" / "tables" / "catalyst_canvas_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "catalyst_canvas_governance_queue.csv", queue)
    write_json(article_root / "outputs" / "json" / "catalyst_canvas_cards.json", cards)
    write_json(article_root / "outputs" / "json" / "catalyst_canvas_governance_queue.json", [card for card in cards if card["review"]["priority"] != "standard"])
    write_json(article_root / "canvas" / "catalyst_canvas_cards.json", cards)
    write_json(article_root / "canvas" / "catalyst_canvas_governance_queue.json", [card for card in cards if card["review"]["priority"] != "standard"])
    markdown = ["# Catalyst Canvas Governance Queue", "", "| Item | Priority | Owner |", "|---|---|---|"]
    markdown += [f"| {row['item']} | {row['review_priority']} | {row['owner']} |" for row in queue]
    (article_root / "outputs" / "markdown").mkdir(parents=True, exist_ok=True)
    (article_root / "outputs" / "markdown" / "catalyst_canvas_governance_queue.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")
    print(f"Catalyst Canvas audit complete for {config.article_slug}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    run(args.article_root.resolve(), strict=args.strict)


if __name__ == "__main__":
    main()
