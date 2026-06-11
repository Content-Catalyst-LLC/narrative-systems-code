from __future__ import annotations

import unittest

from life_writing_canvas.models import LifeWritingConfig, LifeWritingRecord
from life_writing_canvas.validation import validate_record
from life_writing_canvas.scoring import ethical_risk, governance_priority_score, interpretation_readiness, life_writing_coherence, review_priority, truth_practice


class LifeWritingCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = LifeWritingConfig()
        record = LifeWritingRecord(
            "Test",
            "Context",
            0.8, 0.8, 0.7, 0.8, 0.8, 0.7,
            0.8, 0.7, 0.8, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.8, 0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            life_writing_coherence(record),
            truth_practice(record),
            ethical_risk(record),
            interpretation_readiness(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
