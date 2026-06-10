from __future__ import annotations

import unittest

from plot_coherence_canvas.models import PlotCoherenceItem
from plot_coherence_canvas.scoring import (
    plot_coherence,
    action_dependency,
    coherence_risk,
    governance_priority_score,
    review_priority,
)
from plot_coherence_canvas.validation import validate_plot_coherence_item


class PlotCoherenceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = PlotCoherenceItem(
            "Test story",
            "test",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.6, 0.5, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.8,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_plot_coherence_item(item)
        self.assertGreaterEqual(plot_coherence(item), 0)
        self.assertLessEqual(plot_coherence(item), 1)
        self.assertGreaterEqual(action_dependency(item), 0)
        self.assertLessEqual(action_dependency(item), 1)
        self.assertGreaterEqual(coherence_risk(item), 0)
        self.assertLessEqual(coherence_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = PlotCoherenceItem(
            "Bad story",
            "test",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.6, 0.5, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.8,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_plot_coherence_item(item)


if __name__ == "__main__":
    unittest.main()
