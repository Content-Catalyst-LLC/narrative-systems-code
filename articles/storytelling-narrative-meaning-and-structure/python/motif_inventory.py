"""
Storytelling: Motif Inventory

Educational workflow for organizing motifs by symbolic function and recurrence.
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    motifs = pd.read_csv("../data/motifs.csv")

    motifs["relative_frequency"] = motifs["frequency"] / motifs["frequency"].sum()
    motifs = motifs.sort_values("frequency", ascending=False)

    print(motifs)

    motifs.to_csv("../outputs/motif_inventory_scored.csv", index=False)


if __name__ == "__main__":
    main()
