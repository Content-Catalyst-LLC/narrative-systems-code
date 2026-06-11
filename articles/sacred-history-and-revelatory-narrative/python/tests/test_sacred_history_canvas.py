from __future__ import annotations

import unittest
from sacred_history_canvas.models import SacredHistoryConfig, SacredHistoryRecord
from sacred_history_canvas.validation import validate_record
from sacred_history_canvas.scoring import governance_priority_score, interpretation_readiness, revelatory_claim_strength, review_priority, sacred_authority_risk, sacred_history_integration


class SacredHistoryCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = SacredHistoryConfig()
        record = SacredHistoryRecord("Test", "Context", 0.8, 0.8, 0.7, 0.7, 0.8, 0.8, 0.7, 0.7, 0.6, 0.7, 0.8, 0.8, 0.3, 0.4, 0.3, 0.4, 0.4, 0.8, 0.8, 0.7, 0.7, 0.8, "editorial", "active", "")
        validate_record(record, config)
        for value in [revelatory_claim_strength(record), sacred_history_integration(record), sacred_authority_risk(record), interpretation_readiness(record), governance_priority_score(record, config)]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
