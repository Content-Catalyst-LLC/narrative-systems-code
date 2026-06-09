from __future__ import annotations

import unittest

from storytelling_canvas.models import StoryItem
from storytelling_canvas.scoring import coherence_score, governance_risk, review_priority
from storytelling_canvas.validation import validate_story_item


class StorytellingCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = StoryItem(
            "Test narrative",
            "test",
            "A test item.",
            0.8, 0.7, 0.6, 0.5, 0.9, 0.4, 0.8,
            0.7, 0.6, 0.5, 0.6,
            "test-owner",
            "active",
        )
        validate_story_item(item)
        self.assertGreaterEqual(coherence_score(item), 0)
        self.assertLessEqual(coherence_score(item), 1)
        self.assertGreaterEqual(governance_risk(item), 0)
        self.assertLessEqual(governance_risk(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = StoryItem(
            "Bad narrative",
            "test",
            "Invalid score.",
            1.2, 0.7, 0.6, 0.5, 0.9, 0.4, 0.8,
            0.7, 0.6, 0.5, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_story_item(item)


if __name__ == "__main__":
    unittest.main()
