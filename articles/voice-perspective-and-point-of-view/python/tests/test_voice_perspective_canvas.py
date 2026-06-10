from __future__ import annotations

import unittest

from voice_perspective_canvas.models import VoicePerspectiveItem
from voice_perspective_canvas.scoring import (
    voice_consistency,
    perspective_access,
    reliability_risk,
    governance_priority_score,
    review_priority,
)
from voice_perspective_canvas.validation import validate_voice_perspective_item


class VoicePerspectiveCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = VoicePerspectiveItem(
            "Test voice",
            "test",
            0.8, 0.7, 0.6, 0.8, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.2, 0.3, 0.4, 0.3, 0.5,
            0.7, 0.6, 0.3, 0.2,
            "test-owner",
            "active",
        )
        validate_voice_perspective_item(item)
        self.assertGreaterEqual(voice_consistency(item), 0)
        self.assertLessEqual(voice_consistency(item), 1)
        self.assertGreaterEqual(perspective_access(item), 0)
        self.assertLessEqual(perspective_access(item), 1)
        self.assertGreaterEqual(reliability_risk(item), 0)
        self.assertLessEqual(reliability_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = VoicePerspectiveItem(
            "Bad voice",
            "test",
            1.2, 0.7, 0.6, 0.8, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.2, 0.3, 0.4, 0.3, 0.5,
            0.7, 0.6, 0.3, 0.2,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_voice_perspective_item(item)


if __name__ == "__main__":
    unittest.main()
