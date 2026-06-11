from __future__ import annotations

import unittest

from adaptation_governance_canvas.models import AdaptationGovernanceConfig, AdaptationGovernanceRecord
from adaptation_governance_canvas.validation import validate_record
from adaptation_governance_canvas.scoring import adaptation_integrity, ai_adaptation_risk, consent_and_context_strength, franchise_drift, governance_priority_score, review_priority, transfer_loss


class AdaptationGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = AdaptationGovernanceConfig()
        record = AdaptationGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.3, 0.3, 0.4, 0.3, 0.4, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.8,
            0.8, 0.8, 0.7, 0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            adaptation_integrity(record),
            transfer_loss(record),
            franchise_drift(record),
            ai_adaptation_risk(record),
            consent_and_context_strength(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
