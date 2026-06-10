from __future__ import annotations

import unittest

from aristotelian_plot_canvas.models import PlotItem
from aristotelian_plot_canvas.scoring import plot_unity, formula_risk, governance_score, review_priority
from aristotelian_plot_canvas.validation import validate_plot_item


class AristotelianPlotCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = PlotItem(
            "Test plot",
            "test",
            0.8, 0.7, 0.6, 0.5, 0.8, 0.7,
            0.6, 0.7, 0.5, 0.6, 0.7,
            0.8, 0.7, 0.6, 0.8,
            0.2, 0.3, 0.4, 0.3,
            "test-owner",
            "active",
        )
        validate_plot_item(item)
        self.assertGreaterEqual(plot_unity(item), 0)
        self.assertLessEqual(plot_unity(item), 1)
        self.assertGreaterEqual(formula_risk(item), 0)
        self.assertLessEqual(formula_risk(item), 1)
        self.assertGreaterEqual(governance_score(item), 0)
        self.assertLessEqual(governance_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = PlotItem(
            "Bad plot",
            "test",
            1.2, 0.7, 0.6, 0.5, 0.8, 0.7,
            0.6, 0.7, 0.5, 0.6, 0.7,
            0.8, 0.7, 0.6, 0.8,
            0.2, 0.3, 0.4, 0.3,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_plot_item(item)


if __name__ == "__main__":
    unittest.main()
