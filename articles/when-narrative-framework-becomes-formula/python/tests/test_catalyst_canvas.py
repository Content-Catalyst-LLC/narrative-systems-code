from __future__ import annotations
import unittest
from catalyst_canvas.cli import weighted_average

class CatalystCanvasTests(unittest.TestCase):
    def test_weighted_average_is_bounded(self) -> None:
        self.assertAlmostEqual(weighted_average({"a": 1.0, "b": 0.0}, {"a": 1.0, "b": 1.0}), 0.5)

if __name__ == "__main__":
    unittest.main()
