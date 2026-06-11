from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativeTimeConfig:
    article_title: str = "Paul Ricoeur and Narrative Time"
    article_slug: str = "paul-ricoeur-and-narrative-time"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class NarrativeTimeRecord:
    item: str
    claim_context: str
    memory_mapping: float
    anticipation: float
    plot_logic: float
    configuration: float
    refiguration: float
    ending_function: float
    event_selection: float
    causal_articulation: float
    reversal_recognition: float
    concordance: float
    discordance: float
    whole_plot_coherence: float
    continuity: float
    change: float
    promise_responsibility: float
    memory_revision: float
    agency: float
    relational_recognition: float
    premature_closure: float
    redemptive_shortcut: float
    erased_continuity: float
    delayed_accountability: float
    nostalgic_origin: float
    uncertainty_notes: float
    source_context: float
    counterexamples: float
    method_limits: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
