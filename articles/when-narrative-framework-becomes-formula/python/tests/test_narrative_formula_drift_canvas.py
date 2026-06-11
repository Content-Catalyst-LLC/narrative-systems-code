from __future__ import annotations
import unittest
from narrative_formula_drift_canvas.models import NarrativeFormulaDriftConfig, NarrativeFormulaDriftRecord
from narrative_formula_drift_canvas.validation import validate_record
from narrative_formula_drift_canvas.scoring import ai_template_risk, formula_drift, framework_health, governance_priority_score, narrative_specificity, review_priority

class NarrativeFormulaDriftCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = NarrativeFormulaDriftConfig()
        record = NarrativeFormulaDriftRecord(
            "Test", "Context", 0.6, 0.5, 0.6, 0.5, 0.4, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.8, 0.7, 0.7, 0.8, 0.7, 0.8,
            0.4, 0.5, 0.5, 0.4, 0.5, 0.7,
            0.7, "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [formula_drift(record), framework_health(record), narrative_specificity(record), ai_template_risk(record), governance_priority_score(record, config)]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})

if __name__ == "__main__":
    unittest.main()
