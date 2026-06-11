from __future__ import annotations

import unittest

from serial_narrative_governance_canvas.models import SerialNarrativeGovernanceConfig, SerialNarrativeGovernanceRecord
from serial_narrative_governance_canvas.validation import validate_record
from serial_narrative_governance_canvas.scoring import ai_serial_risk, continuity_burden, ensemble_and_ethics_strength, governance_priority_score, payoff_integrity, review_priority, season_coherence


class SerialNarrativeGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = SerialNarrativeGovernanceConfig()
        record = SerialNarrativeGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.8, 0.8, 0.7, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            season_coherence(record),
            continuity_burden(record),
            payoff_integrity(record),
            ensemble_and_ethics_strength(record),
            ai_serial_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
