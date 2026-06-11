from __future__ import annotations

from pathlib import Path
import argparse
import csv
import json
from typing import Any

from .models import CanvasConfig, CanvasRecord
from .validation import validate_config, validate_record
from .scoring import (
    confidence_band,
    domain_strength,
    governance_priority_score,
    interpretation_readiness,
    review_priority,
    risk_score,
)
from .governance import build_canvas_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def _numeric_prefixed(row: dict[str, str], prefix: str) -> dict[str, float]:
    output: dict[str, float] = {}
    for key, value in row.items():
        if key.startswith(prefix):
            clean_key = key.removeprefix(prefix)
            if value == '':
                continue
            output[clean_key] = float(value)
    return output


def load_config(path: Path) -> CanvasConfig:
    payload = json.loads(path.read_text(encoding='utf-8'))
    config = CanvasConfig(
        article_title=payload['article_title'],
        article_slug=payload['article_slug'],
        module_name=payload.get('module_name', 'catalyst_canvas'),
        metric_weights={k: float(v) for k, v in payload['metric_weights'].items()},
        risk_weights={k: float(v) for k, v in payload['risk_weights'].items()},
        readiness_weights={k: float(v) for k, v in payload['readiness_weights'].items()},
        thresholds={k: float(v) for k, v in payload.get('thresholds', {'medium': 0.45, 'high': 0.62}).items()},
    )
    validate_config(config)
    return config


def load_records(path: Path, config: CanvasConfig, strict: bool) -> list[CanvasRecord]:
    records: list[CanvasRecord] = []
    with path.open('r', encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            record = CanvasRecord(
                item=row.get('item', '').strip(),
                claim_context=row.get('claim_context', '').strip(),
                article_title=row.get('article_title', config.article_title).strip() or config.article_title,
                article_slug=row.get('article_slug', config.article_slug).strip() or config.article_slug,
                metrics=_numeric_prefixed(row, 'metric_'),
                risk_signals=_numeric_prefixed(row, 'risk_'),
                readiness_signals=_numeric_prefixed(row, 'readiness_'),
                owner=row.get('owner', 'editorial').strip() or 'editorial',
                status=row.get('status', 'active').strip() or 'active',
                notes=row.get('notes', '').strip(),
            )
            validate_record(record, config, strict=strict)
            records.append(record)
    if not records:
        raise ValueError(f'No records found in {path}')
    return records


def build_rows(records: list[CanvasRecord], config: CanvasConfig) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for record in records:
        rows.append({
            'article_title': config.article_title,
            'article_slug': config.article_slug,
            'item': record.item,
            'claim_context': record.claim_context,
            'domain_strength': round(domain_strength(record, config), 4),
            'risk_score': round(risk_score(record, config), 4),
            'interpretation_readiness': round(interpretation_readiness(record, config), 4),
            'governance_priority_score': round(governance_priority_score(record, config), 4),
            'review_priority': review_priority(record, config),
            'confidence_band': confidence_band(record, config),
            'owner': record.owner,
            'status': record.status,
            'governance_note': governance_note(record, config),
        })
    priority_order = {'high': 3, 'medium': 2, 'standard': 1}
    return sorted(
        rows,
        key=lambda row: (
            priority_order.get(str(row['review_priority']), 0),
            float(row['governance_priority_score']),
        ),
        reverse=True,
    )


def run(
    article_root: Path,
    input_path: Path | None = None,
    config_path: Path | None = None,
    output_dir: Path | None = None,
    strict: bool = False,
) -> None:
    article_root = article_root.resolve()
    config_path = config_path or article_root / 'canvas' / 'catalyst_canvas_config.json'
    input_path = input_path or article_root / 'data' / 'catalyst_canvas_assessment.csv'
    output_dir = output_dir or article_root / 'outputs'

    config = load_config(config_path)
    records = load_records(input_path, config, strict=strict)
    rows = build_rows(records, config)
    cards = [build_canvas_card(record, config) for record in records]

    queue = [row for row in rows if row['review_priority'] != 'standard']
    queue_cards = [card for card in cards if card['review']['priority'] != 'standard']

    write_csv(output_dir / 'tables' / 'catalyst_canvas_audit.csv', rows)
    write_csv(output_dir / 'tables' / 'catalyst_canvas_governance_queue.csv', queue or rows[:1])
    write_json(output_dir / 'json' / 'catalyst_canvas_cards.json', cards)
    write_json(output_dir / 'json' / 'catalyst_canvas_governance_queue.json', queue_cards)
    write_markdown_queue(output_dir / 'markdown' / 'catalyst_canvas_governance_queue.md', queue or rows[:1])

    write_json(article_root / 'canvas' / 'catalyst_canvas_cards.json', cards)
    write_json(article_root / 'canvas' / 'catalyst_canvas_governance_queue.json', queue_cards)

    print(f'Catalyst Canvas audit complete for {config.article_slug}')
    print(output_dir / 'tables' / 'catalyst_canvas_audit.csv')


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run advanced Catalyst Canvas audit for an article.')
    parser.add_argument('--article-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--input', type=Path, default=None)
    parser.add_argument('--config', type=Path, default=None)
    parser.add_argument('--output-dir', type=Path, default=None)
    parser.add_argument('--strict', action='store_true')
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(
        article_root=args.article_root,
        input_path=args.input,
        config_path=args.config,
        output_dir=args.output_dir,
        strict=args.strict,
    )


if __name__ == '__main__':
    main()
