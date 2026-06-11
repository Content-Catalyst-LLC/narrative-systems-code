from __future__ import annotations

import unittest

from narratology_canvas.models import NarratologyConfig, NarratologyRecord
from narratology_canvas.validation import validate_record
from narratology_canvas.scoring import focalization_complexity, governance_priority_score, governance_risk, interpretation_readiness, narrative_grammar_strength, review_priority, temporal_complexity


class NarratologyCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = NarratologyConfig()
        record = NarratologyRecord(
            "Test",
            "Context",
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.7, 0.7, 0.6, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.4,
            0.3, 0.4, 0.3, 0.4, 0.4, 0.8,
            0.8, 0.7, 0.8,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [narrative_grammar_strength(record), focalization_complexity(record), temporal_complexity(record), governance_risk(record), interpretation_readiness(record), governance_priority_score(record, config)]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
