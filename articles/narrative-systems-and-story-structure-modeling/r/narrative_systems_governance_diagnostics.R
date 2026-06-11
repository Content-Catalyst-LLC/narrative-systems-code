# Base R workflow for Narrative Systems and Story Structure Modeling.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

setwd(article_root)

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

records <- read.csv(file.path(article_root, "data", "narrative_systems_governance_claims.csv"), stringsAsFactors = FALSE)

records$narrative_coherence <- rowMeans(records[, c(
  "causal_alignment",
  "state_transition_clarity",
  "agent_goal_fit",
  "world_rule_consistency",
  "temporal_mapping",
  "evidence_quality"
)])

records$formula_drift_risk <- pmin(
  1,
  records$beat_template_dependence * 0.18 +
    records$universal_model_claims * 0.18 +
    records$context_loss * 0.18 +
    records$genre_flattening * 0.16 +
    records$model_overconfidence * 0.16 +
    (1 - records$judgment_review) * 0.14
)

records$responsibility_balance <- pmax(
  0,
  1 - abs(records$individual_agency_visibility - records$systemic_agency_visibility)
)

records$network_system_strength <- rowMeans(records[, c(
  "network_mapping",
  "relationship_specificity",
  "constraint_visibility",
  "feedback_loop_clarity",
  "agent_goal_fit",
  "world_rule_consistency"
)])

records$ai_story_structure_risk <- pmin(
  1,
  records$plot_hallucination * 0.18 +
    records$causal_invention * 0.18 +
    records$stereotype_tendency * 0.18 +
    records$formula_generation * 0.18 +
    records$biased_corpus * 0.16 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$formula_drift_risk * 0.22 +
    records$ai_story_structure_risk * 0.22 +
    (1 - records$narrative_coherence) * 0.18 +
    (1 - records$responsibility_balance) * 0.12 +
    (1 - records$network_system_strength) * 0.12 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "narrative_systems_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "narrative_systems_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "narrative_coherence_scores.png"), width = 1200, height = 700)
barplot(records$narrative_coherence, names.arg = records$item, las = 2, ylab = "Narrative coherence", main = "Narrative Coherence")
grid()
dev.off()

png(file.path(figures_dir, "formula_drift_risk_scores.png"), width = 1200, height = 700)
barplot(records$formula_drift_risk, names.arg = records$item, las = 2, ylab = "Formula-drift risk", main = "Formula-Drift Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "modeling_context",
  "narrative_coherence",
  "formula_drift_risk",
  "responsibility_balance",
  "ai_story_structure_risk",
  "review_priority"
)])
