from __future__ import annotations

import unittest

from storytelling_value_governance_canvas.models import StorytellingValueGovernanceConfig, StorytellingValueGovernanceRecord
from storytelling_value_governance_canvas.validation import validate_record
from storytelling_value_governance_canvas.scoring import ai_storytelling_governance, governance_priority_score, misuse_risk, narrative_responsibility, review_priority, storytelling_value


class StorytellingValueGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = StorytellingValueGovernanceConfig()
        record = StorytellingValueGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.8, 0.7, 0.8, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.2, 0.2, 0.1, 0.2, 0.3, 0.8,
            0.8, 0.8, 0.8, 0.7, 0.8, 0.8,
            0.8, 0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            storytelling_value(record),
            narrative_responsibility(record),
            misuse_risk(record),
            ai_storytelling_governance(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
