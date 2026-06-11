from __future__ import annotations

import unittest

from legal_narrative_responsibility_canvas.models import LegalNarrativeResponsibilityConfig, LegalNarrativeResponsibilityRecord
from legal_narrative_responsibility_canvas.validation import validate_record
from legal_narrative_responsibility_canvas.scoring import ai_legal_narrative_risk, evidence_support, governance_priority_score, narrative_overreach_risk, procedural_voice, review_priority, testimony_responsibility


class LegalNarrativeResponsibilityCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = LegalNarrativeResponsibilityConfig()
        record = LegalNarrativeResponsibilityRecord(
            "Test", "Context",
            0.8, 0.8, 0.8, 0.7, 0.8, 0.7,
            0.4, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.7, 0.8, 0.7, 0.8, 0.8,
            0.8, 0.8, 0.8, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            evidence_support(record),
            narrative_overreach_risk(record),
            procedural_voice(record),
            testimony_responsibility(record),
            ai_legal_narrative_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
