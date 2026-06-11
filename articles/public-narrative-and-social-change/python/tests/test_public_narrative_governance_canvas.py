from __future__ import annotations

import unittest

from public_narrative_governance_canvas.models import PublicNarrativeGovernanceConfig, PublicNarrativeGovernanceRecord
from public_narrative_governance_canvas.validation import validate_record
from public_narrative_governance_canvas.scoring import ai_public_narrative_risk, governance_priority_score, mobilization_readiness, public_narrative_coherence, public_voice_integrity, review_priority, testimony_extraction_risk


class PublicNarrativeGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = PublicNarrativeGovernanceConfig()
        record = PublicNarrativeGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.8, 0.7, 0.8, 0.7,
            0.8, 0.7, 0.8, 0.7, 0.8, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.8, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            public_narrative_coherence(record),
            mobilization_readiness(record),
            testimony_extraction_risk(record),
            public_voice_integrity(record),
            ai_public_narrative_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
