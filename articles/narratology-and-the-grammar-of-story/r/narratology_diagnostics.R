# Base R workflow for Narratology and the Grammar of Story.

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

records <- read.csv(file.path(article_root, "data", "narratology_claims.csv"), stringsAsFactors = FALSE)

records$narrative_grammar_strength <- rowMeans(records[, c("story_discourse_clarity", "voice_clarity", "focalization_clarity", "temporal_mapping", "character_agency_mapping", "information_control_analysis")])
records$focalization_complexity <- rowMeans(records[, c("perspective_shifts", "knowledge_restriction", "interior_access", "source_hierarchy", "multiple_focalizers")])
records$temporal_complexity <- rowMeans(records[, c("analepsis", "prolepsis", "ellipsis", "duration_variation", "repetition_frequency")])
records$interpretation_readiness <- rowMeans(records[, c("source_context", "counterexamples", "method_limits", "uncertainty_notes", "story_discourse_clarity", "focalization_clarity")])

records$governance_risk <- pmin(
  1,
  records$omission_risk * 0.18 +
    records$power_blindness * 0.20 +
    records$voice_imbalance * 0.20 +
    records$closure_pressure * 0.16 +
    records$unreliable_framing_risk * 0.16 +
    (1 - records$method_limits) * 0.10
)

records$governance_priority_score <- pmin(
  1,
  records$governance_risk * 0.40 +
    (1 - records$interpretation_readiness) * 0.28 +
    records$voice_imbalance * 0.16 +
    records$omission_risk * 0.16
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "narratology_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "narratology_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "narrative_grammar_strength_scores.png"), width = 1200, height = 700)
barplot(records$narrative_grammar_strength, names.arg = records$item, las = 2, ylab = "Narrative grammar strength", main = "Narrative Grammar Strength")
grid()
dev.off()

png(file.path(figures_dir, "governance_risk_scores.png"), width = 1200, height = 700)
barplot(records$governance_risk, names.arg = records$item, las = 2, ylab = "Governance risk", main = "Narratology Governance Risk")
grid()
dev.off()

print(records[, c("item", "claim_context", "narrative_grammar_strength", "focalization_complexity", "temporal_complexity", "governance_risk", "interpretation_readiness", "review_priority")])
