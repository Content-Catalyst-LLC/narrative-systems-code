from __future__ import annotations

import unittest

from cross_media_story_governance_canvas.models import CrossMediaStoryGovernanceConfig, CrossMediaStoryGovernanceRecord
from cross_media_story_governance_canvas.validation import validate_record
from cross_media_story_governance_canvas.scoring import ai_cross_media_risk, consent_and_context_strength, governance_priority_score, media_transfer_risk, medium_affordance_fit, multimodal_coherence, review_priority


class CrossMediaStoryGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = CrossMediaStoryGovernanceConfig()
        record = CrossMediaStoryGovernanceRecord(
            "Test", "Context",
            0.8, 0.7, 0.8, 0.7, 0.8, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.8, 0.8, 0.7, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            medium_affordance_fit(record),
            media_transfer_risk(record),
            multimodal_coherence(record),
            consent_and_context_strength(record),
            ai_cross_media_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
