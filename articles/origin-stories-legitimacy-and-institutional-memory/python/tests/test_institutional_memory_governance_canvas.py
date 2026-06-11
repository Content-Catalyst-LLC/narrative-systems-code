from __future__ import annotations

import unittest

from institutional_memory_governance_canvas.models import InstitutionalMemoryGovernanceConfig, InstitutionalMemoryGovernanceRecord
from institutional_memory_governance_canvas.validation import validate_record
from institutional_memory_governance_canvas.scoring import ai_memory_distortion_risk, governance_priority_score, institutional_memory_strength, legitimacy_alignment, origin_myth_risk, reform_credibility, review_priority


class InstitutionalMemoryGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = InstitutionalMemoryGovernanceConfig()
        record = InstitutionalMemoryGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.4, 0.4, 0.4, 0.4, 0.4, 0.8,
            0.8, 0.8, 0.8, 0.7, 0.8, 0.7,
            0.7, 0.7, 0.7, 0.6, 0.7, 0.7,
            0.4, 0.4, 0.4, 0.8, 0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            legitimacy_alignment(record),
            origin_myth_risk(record),
            institutional_memory_strength(record),
            reform_credibility(record),
            ai_memory_distortion_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
