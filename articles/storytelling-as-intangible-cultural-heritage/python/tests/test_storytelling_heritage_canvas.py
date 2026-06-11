from __future__ import annotations

import unittest

from storytelling_heritage_canvas.models import StorytellingHeritageItem
from storytelling_heritage_canvas.scoring import (
    living_continuity,
    safeguarding_readiness,
    heritage_context_preservation,
    archive_risk,
    governance_priority_score,
    review_priority,
)
from storytelling_heritage_canvas.validation import validate_storytelling_heritage_item


class StorytellingHeritageCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = StorytellingHeritageItem(
            "Test heritage item",
            "test heritage context",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_storytelling_heritage_item(item)
        self.assertGreaterEqual(living_continuity(item), 0)
        self.assertLessEqual(living_continuity(item), 1)
        self.assertGreaterEqual(safeguarding_readiness(item), 0)
        self.assertLessEqual(safeguarding_readiness(item), 1)
        self.assertGreaterEqual(heritage_context_preservation(item), 0)
        self.assertLessEqual(heritage_context_preservation(item), 1)
        self.assertGreaterEqual(archive_risk(item), 0)
        self.assertLessEqual(archive_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = StorytellingHeritageItem(
            "Bad heritage item",
            "test heritage context",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_storytelling_heritage_item(item)


if __name__ == "__main__":
    unittest.main()
