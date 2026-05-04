"""
Storytelling: Narrative Arc Model

Educational workflow for modeling narrative tension, conflict intensity,
transformation pressure, and resolution pressure across story stages.
"""

from __future__ import annotations

import pandas as pd


def identify_peak_moments(arc: pd.DataFrame) -> pd.DataFrame:
    """Identify the peak stage for each narrative dimension."""
    dimensions = [
        "tension",
        "conflict_intensity",
        "transformation_pressure",
        "resolution_pressure"
    ]

    rows = []

    for dimension in dimensions:
        peak_row = arc.loc[arc[dimension].idxmax()]
        rows.append({
            "dimension": dimension,
            "peak_stage": peak_row["stage"],
            "peak_value": peak_row[dimension]
        })

    return pd.DataFrame(rows)


def main() -> None:
    arc = pd.read_csv("../data/story_arc.csv")
    peaks = identify_peak_moments(arc)

    print(arc)
    print(peaks)

    arc.to_csv("../outputs/narrative_arc.csv", index=False)
    peaks.to_csv("../outputs/narrative_peak_moments.csv", index=False)


if __name__ == "__main__":
    main()
