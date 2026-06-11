from __future__ import annotations

import unittest

from oral_storytelling_variation_canvas.models import OralStorytellingVariationItem
from oral_storytelling_variation_canvas.scoring import (
    performance_context,
    memory_support,
    variation_accountability,
    archive_risk,
    governance_priority_score,
    review_priority,
)
from oral_storytelling_variation_canvas.validation import validate_oral_storytelling_variation_item


class OralStorytellingVariationCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = OralStorytellingVariationItem(
            "Test oral story",
            "test context",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_oral_storytelling_variation_item(item)
        self.assertGreaterEqual(performance_context(item), 0)
        self.assertLessEqual(performance_context(item), 1)
        self.assertGreaterEqual(memory_support(item), 0)
        self.assertLessEqual(memory_support(item), 1)
        self.assertGreaterEqual(variation_accountability(item), 0)
        self.assertLessEqual(variation_accountability(item), 1)
        self.assertGreaterEqual(archive_risk(item), 0)
        self.assertLessEqual(archive_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = OralStorytellingVariationItem(
            "Bad oral story",
            "test context",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_oral_storytelling_variation_item(item)


if __name__ == "__main__":
    unittest.main()
