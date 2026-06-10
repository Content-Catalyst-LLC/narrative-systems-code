from __future__ import annotations

import unittest

from folktale_morphology_canvas.models import FolktaleMorphologyItem
from folktale_morphology_canvas.scoring import (
    function_coverage,
    sequence_integrity,
    morphology_context_balance,
    reduction_risk,
    governance_priority_score,
    review_priority,
)
from folktale_morphology_canvas.validation import validate_folktale_morphology_item


class FolktaleMorphologyCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = FolktaleMorphologyItem(
            "Test folktale",
            "test",
            0.8, 0.7, 0.6, 0.8, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.2, 0.3, 0.4, 0.3,
            0.5, 0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_folktale_morphology_item(item)
        self.assertGreaterEqual(function_coverage(item), 0)
        self.assertLessEqual(function_coverage(item), 1)
        self.assertGreaterEqual(sequence_integrity(item), 0)
        self.assertLessEqual(sequence_integrity(item), 1)
        self.assertGreaterEqual(morphology_context_balance(item), 0)
        self.assertLessEqual(morphology_context_balance(item), 1)
        self.assertGreaterEqual(reduction_risk(item), 0)
        self.assertLessEqual(reduction_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = FolktaleMorphologyItem(
            "Bad folktale",
            "test",
            1.2, 0.7, 0.6, 0.8, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.2, 0.3, 0.4, 0.3,
            0.5, 0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_folktale_morphology_item(item)


if __name__ == "__main__":
    unittest.main()
