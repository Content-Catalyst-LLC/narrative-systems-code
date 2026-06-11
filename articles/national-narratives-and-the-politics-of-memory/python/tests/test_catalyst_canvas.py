from __future__ import annotations

import unittest

from catalyst_canvas.models import CanvasConfig, CanvasRecord
from catalyst_canvas.validation import validate_config, validate_record
from catalyst_canvas.scoring import domain_strength, governance_priority_score, interpretation_readiness, review_priority, risk_score


class CatalystCanvasAdvancedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = CanvasConfig(
            article_title="National Narratives and the Politics of Memory",
            article_slug="national-narratives-and-the-politics-of-memory",
            module_name="catalyst_canvas",
            metric_weights={"source_context": 1.0, "conceptual_depth": 1.0, "ethical_framing": 1.0},
            risk_weights={"context_loss": 1.0, "overgeneralization": 1.0, "power_blindness": 1.0},
            readiness_weights={"method_limits": 1.0, "counterexamples": 1.0, "uncertainty_notes": 1.0},
            thresholds={"medium": 0.45, "high": 0.62},
        )
        validate_config(self.config)

    def test_scores_are_bounded(self) -> None:
        record = CanvasRecord(
            item="Claim",
            claim_context="Context",
            article_title="National Narratives and the Politics of Memory",
            article_slug="national-narratives-and-the-politics-of-memory",
            metrics={"source_context": 0.8, "conceptual_depth": 0.7, "ethical_framing": 0.6},
            risk_signals={"context_loss": 0.2, "overgeneralization": 0.4, "power_blindness": 0.3},
            readiness_signals={"method_limits": 0.8, "counterexamples": 0.7, "uncertainty_notes": 0.6},
            owner="editorial",
            status="active",
        )
        validate_record(record, self.config)
        for value in [
            domain_strength(record, self.config),
            risk_score(record, self.config),
            interpretation_readiness(record, self.config),
            governance_priority_score(record, self.config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, self.config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
