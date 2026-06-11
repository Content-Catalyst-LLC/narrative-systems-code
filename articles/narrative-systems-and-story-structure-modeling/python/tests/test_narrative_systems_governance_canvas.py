from __future__ import annotations

import unittest

from narrative_systems_governance_canvas.models import NarrativeSystemsGovernanceConfig, NarrativeSystemsGovernanceRecord
from narrative_systems_governance_canvas.validation import validate_record
from narrative_systems_governance_canvas.scoring import ai_story_structure_risk, formula_drift_risk, governance_priority_score, narrative_coherence, network_system_strength, responsibility_balance, review_priority


class NarrativeSystemsGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = NarrativeSystemsGovernanceConfig()
        record = NarrativeSystemsGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7, 0.8,
            0.8, 0.8, 0.7, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            narrative_coherence(record),
            formula_drift_risk(record),
            responsibility_balance(record),
            network_system_strength(record),
            ai_story_structure_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
