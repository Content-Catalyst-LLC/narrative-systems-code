from __future__ import annotations

import unittest

from representation_ethics_governance_canvas.models import RepresentationEthicsGovernanceConfig, RepresentationEthicsGovernanceRecord
from representation_ethics_governance_canvas.validation import validate_record
from representation_ethics_governance_canvas.scoring import ai_representation_risk, consent_adequacy, cultural_and_visual_strength, governance_priority_score, representation_integrity, representation_risk, review_priority


class RepresentationEthicsGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = RepresentationEthicsGovernanceConfig()
        record = RepresentationEthicsGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            representation_integrity(record),
            representation_risk(record),
            consent_adequacy(record),
            cultural_and_visual_strength(record),
            ai_representation_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
