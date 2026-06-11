from __future__ import annotations

import unittest

from traditional_narrative_forms_canvas.models import TraditionalNarrativeItem
from traditional_narrative_forms_canvas.scoring import (
    form_classification,
    narrative_distinction,
    cultural_memory_function,
    adaptation_risk,
    governance_priority_score,
    review_priority,
)
from traditional_narrative_forms_canvas.validation import validate_traditional_narrative_item


class TraditionalNarrativeFormsCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = TraditionalNarrativeItem(
            "Test narrative", "myth",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner", "active"
        )
        validate_traditional_narrative_item(item)
        self.assertGreaterEqual(form_classification(item), 0)
        self.assertLessEqual(form_classification(item), 1)
        self.assertGreaterEqual(narrative_distinction(item), 0)
        self.assertLessEqual(narrative_distinction(item), 1)
        self.assertGreaterEqual(cultural_memory_function(item), 0)
        self.assertLessEqual(cultural_memory_function(item), 1)
        self.assertGreaterEqual(adaptation_risk(item), 0)
        self.assertLessEqual(adaptation_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = TraditionalNarrativeItem(
            "Bad narrative", "legend",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner", "active"
        )
        with self.assertRaises(ValueError):
            validate_traditional_narrative_item(item)


if __name__ == "__main__":
    unittest.main()
