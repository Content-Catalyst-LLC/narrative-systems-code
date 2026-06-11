from __future__ import annotations

import unittest

from universal_story_model_canvas.models import UniversalStoryModelConfig, UniversalStoryModelRecord
from universal_story_model_canvas.validation import validate_record
from universal_story_model_canvas.scoring import alternative_structure_signal, critique_readiness, governance_priority_score, review_priority, universal_model_fit, universalism_risk


class UniversalStoryModelCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = UniversalStoryModelConfig()
        record = UniversalStoryModelRecord(
            "Test",
            "Context",
            0.8, 0.7, 0.8, 0.7, 0.7, 0.8,
            0.4, 0.5, 0.4, 0.4, 0.5, 0.8,
            0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
            0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            universal_model_fit(record),
            universalism_risk(record),
            critique_readiness(record),
            alternative_structure_signal(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
