from __future__ import annotations

import unittest

from public_story_rhetoric_canvas.models import PublicStoryItem
from public_story_rhetoric_canvas.scoring import (
    rhetorical_balance,
    persuasion_force,
    public_story_risk,
    governance_priority_score,
    review_priority,
)
from public_story_rhetoric_canvas.validation import validate_public_story_item


class PublicStoryRhetoricCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = PublicStoryItem(
            "Test story",
            "test",
            0.8, 0.7, 0.6, 0.8, 0.7,
            0.6, 0.7, 0.6, 0.5, 0.7,
            0.8, 0.2, 0.3, 0.4, 0.3,
            0.8, 0.7,
            "test-owner",
            "active",
        )
        validate_public_story_item(item)
        self.assertGreaterEqual(rhetorical_balance(item), 0)
        self.assertLessEqual(rhetorical_balance(item), 1)
        self.assertGreaterEqual(persuasion_force(item), 0)
        self.assertLessEqual(persuasion_force(item), 1)
        self.assertGreaterEqual(public_story_risk(item), 0)
        self.assertLessEqual(public_story_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = PublicStoryItem(
            "Bad story",
            "test",
            1.2, 0.7, 0.6, 0.8, 0.7,
            0.6, 0.7, 0.6, 0.5, 0.7,
            0.8, 0.2, 0.3, 0.4, 0.3,
            0.8, 0.7,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_public_story_item(item)


if __name__ == "__main__":
    unittest.main()
