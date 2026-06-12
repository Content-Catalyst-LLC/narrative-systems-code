from __future__ import annotations

import unittest

from narrative_risk_governance_canvas.models import NarrativeRiskGovernanceConfig, NarrativeRiskGovernanceRecord
from narrative_risk_governance_canvas.validation import validate_record
from narrative_risk_governance_canvas.scoring import ai_narrative_risk, evidence_integrity, governance_priority_score, narrative_risk, platform_amplification_risk, review_priority, trust_repair_priority


class NarrativeRiskGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = NarrativeRiskGovernanceConfig()
        record = NarrativeRiskGovernanceRecord(
            "Test", "Context",
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.7, 0.7, 0.7, 0.8, 0.8,
            0.5, 0.4, 0.5, 0.7, 0.4, 0.6,
            0.3, 0.4, 0.3, 0.3,
            0.2, 0.3, 0.2, 0.2, 0.2, 0.8,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            narrative_risk(record),
            evidence_integrity(record),
            trust_repair_priority(record),
            platform_amplification_risk(record),
            ai_narrative_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
