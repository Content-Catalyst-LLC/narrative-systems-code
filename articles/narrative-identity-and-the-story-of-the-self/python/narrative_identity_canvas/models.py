from dataclasses import dataclass
@dataclass(frozen=True)
class NarrativeIdentityConfig:
    article_title: str = "Narrative Identity and the Story of the Self"
    article_slug: str = "narrative-identity-and-the-story-of-the-self"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")
@dataclass(frozen=True)
class NarrativeIdentityRecord:
    item: str; claim_context: str
    memory_continuity: float; temporal_progression: float; agency: float; relational_grounding: float; promise_responsibility: float; future_openness: float
    change_handling: float; memory_revision: float; uncertainty_notes: float; counter_memory: float; silence_respect: float; openness_to_retelling: float
    reduction_risk: float; forced_coherence: float; power_blindness: float; trauma_extraction: float; algorithmic_capture: float
    source_context: float; cultural_context: float; method_limits: float; ethics_governance: float; review_owner_clarity: float; public_consequence: float
    owner: str = "editorial"; status: str = "active"; notes: str = ""
