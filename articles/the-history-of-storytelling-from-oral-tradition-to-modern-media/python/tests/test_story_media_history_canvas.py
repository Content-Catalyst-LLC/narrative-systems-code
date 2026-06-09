from __future__ import annotations

import unittest

from story_media_history_canvas.models import StoryMedium
from story_media_history_canvas.scoring import transmission_strength, preservation_risk, review_priority, transition_score
from story_media_history_canvas.validation import validate_story_medium


class StoryMediaHistoryCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = StoryMedium(
            "Test medium",
            "test period",
            0.8, 0.7, 0.6, 0.5, 0.4, 0.9, 0.8, 0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_story_medium(item)
        self.assertGreaterEqual(transmission_strength(item), 0)
        self.assertLessEqual(transmission_strength(item), 1)
        self.assertGreaterEqual(preservation_risk(item), 0)
        self.assertLessEqual(preservation_risk(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_transition_score_is_bounded(self) -> None:
        first = StoryMedium("A", "one", 0.2, 0.3, 0.4, 0.5, 0.6, 0.5, 0.6, 0.7, 0.8, "owner", "active")
        second = StoryMedium("B", "two", 0.8, 0.7, 0.6, 0.5, 0.4, 0.5, 0.6, 0.7, 0.8, "owner", "active")
        score = transition_score(first, second)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)

    def test_invalid_score_raises(self) -> None:
        item = StoryMedium(
            "Bad medium",
            "test period",
            1.2, 0.7, 0.6, 0.5, 0.4, 0.9, 0.8, 0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_story_medium(item)


if __name__ == "__main__":
    unittest.main()
