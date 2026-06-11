from __future__ import annotations

import unittest

from comparative_story_governance_canvas.models import ComparativeStoryGovernanceConfig, ComparativeStoryGovernanceRecord
from comparative_story_governance_canvas.validation import validate_record
from comparative_story_governance_canvas.scoring import ai_comparative_risk, comparative_integrity, contextual_grounding, flattening_risk, governance_priority_score, review_priority, transmission_uncertainty


class ComparativeStoryGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = ComparativeStoryGovernanceConfig()
        record = ComparativeStoryGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.8, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3,
            0.4, 0.3, 0.4, 0.3, 0.2, 0.8,
            0.8, 0.8, 0.7, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            comparative_integrity(record),
            flattening_risk(record),
            transmission_uncertainty(record),
            contextual_grounding(record),
            ai_comparative_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
