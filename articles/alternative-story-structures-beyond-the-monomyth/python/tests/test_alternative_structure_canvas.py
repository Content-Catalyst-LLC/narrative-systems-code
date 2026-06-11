from __future__ import annotations

import unittest

from alternative_structure_canvas.models import AlternativeStructureConfig, AlternativeStructureRecord
from alternative_structure_canvas.validation import validate_record
from alternative_structure_canvas.scoring import alternative_readiness, governance_priority_score, medium_fit, monomyth_overfit_risk, review_priority, structural_plurality


class AlternativeStructureCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = AlternativeStructureConfig()
        record = AlternativeStructureRecord(
            "Test",
            "Context",
            0.5, 0.6, 0.5, 0.6, 0.4, 0.7, 0.5,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
            0.7, 0.6, 0.7, 0.7, 0.4, 0.8,
            0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            structural_plurality(record),
            monomyth_overfit_risk(record),
            alternative_readiness(record),
            medium_fit(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
