# Base R workflow for Paul Ricoeur and Narrative Time.

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

records <- read.csv(file.path(article_root, "data", "ricoeur_narrative_time_claims.csv"), stringsAsFactors = FALSE)

records$narrative_time_configuration <- rowMeans(records[, c("memory_mapping", "anticipation", "plot_logic", "configuration", "refiguration", "ending_function")])
records$emplotment_strength <- rowMeans(records[, c("event_selection", "causal_articulation", "reversal_recognition", "concordance", "discordance", "whole_plot_coherence")])
records$narrative_identity_readiness <- rowMeans(records[, c("continuity", "change", "promise_responsibility", "memory_revision", "agency", "relational_recognition")])
records$interpretation_readiness <- rowMeans(records[, c("source_context", "counterexamples", "method_limits", "uncertainty_notes", "configuration", "refiguration")])

records$temporal_governance_risk <- pmin(
  1,
  records$premature_closure * 0.20 +
    records$redemptive_shortcut * 0.18 +
    records$erased_continuity * 0.18 +
    records$delayed_accountability * 0.18 +
    records$nostalgic_origin * 0.14 +
    (1 - records$uncertainty_notes) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$temporal_governance_risk * 0.40 +
    (1 - records$interpretation_readiness) * 0.28 +
    records$delayed_accountability * 0.16 +
    records$premature_closure * 0.16
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "ricoeur_narrative_time_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "ricoeur_narrative_time_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "narrative_time_configuration_scores.png"), width = 1200, height = 700)
barplot(records$narrative_time_configuration, names.arg = records$item, las = 2, ylab = "Narrative-time configuration", main = "Ricoeur Narrative-Time Configuration")
grid()
dev.off()

png(file.path(figures_dir, "temporal_governance_risk_scores.png"), width = 1200, height = 700)
barplot(records$temporal_governance_risk, names.arg = records$item, las = 2, ylab = "Temporal governance risk", main = "Temporal Governance Risk")
grid()
dev.off()

print(records[, c("item", "claim_context", "narrative_time_configuration", "emplotment_strength", "narrative_identity_readiness", "temporal_governance_risk", "interpretation_readiness", "review_priority")])
