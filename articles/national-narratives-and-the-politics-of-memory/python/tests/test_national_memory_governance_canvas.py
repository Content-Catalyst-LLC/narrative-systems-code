from __future__ import annotations

import unittest

from national_memory_governance_canvas.models import NationalMemoryGovernanceConfig, NationalMemoryGovernanceRecord
from national_memory_governance_canvas.validation import validate_record
from national_memory_governance_canvas.scoring import ai_memory_risk, governance_priority_score, memory_accountability, memory_plurality, national_myth_risk, public_memory_infrastructure, review_priority


class NationalMemoryGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = NationalMemoryGovernanceConfig()
        record = NationalMemoryGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.7, 0.8, 0.7,
            0.4, 0.4, 0.4, 0.3, 0.3, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.6,
            0.8, 0.7, 0.7,
            0.4, 0.3, 0.4, 0.3, 0.4, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            memory_plurality(record),
            national_myth_risk(record),
            memory_accountability(record),
            public_memory_infrastructure(record),
            ai_memory_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
