# Base R workflow for Memory, Trauma, and Fragmented Narrative.

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

records <- read.csv(file.path(article_root, "data", "fragmented_narrative_claims.csv"), stringsAsFactors = FALSE)

records$fragmentation_sensitivity <- rowMeans(records[, c(
  "temporal_rupture",
  "gap_marking",
  "repetition_patterning",
  "silence_respect",
  "uncertainty_notes",
  "contextual_care"
)])

records$witness_care <- rowMeans(records[, c(
  "consent",
  "agency",
  "privacy",
  "relational_context",
  "safety_framing",
  "boundary_discipline"
)])

records$trauma_narrative_risk <- pmin(
  1,
  records$forced_coherence * 0.20 +
    records$redemptive_shortcut * 0.18 +
    records$extraction_risk * 0.20 +
    records$identity_reduction * 0.18 +
    records$spectacle_pressure * 0.14 +
    (1 - records$method_limits) * 0.10
)

records$interpretation_readiness <- rowMeans(records[, c(
  "source_context",
  "cultural_context",
  "uncertainty_notes",
  "method_limits",
  "ethics_governance",
  "review_owner_clarity"
)])

records$governance_priority_score <- pmin(
  1,
  records$trauma_narrative_risk * 0.40 +
    (1 - records$witness_care) * 0.22 +
    (1 - records$interpretation_readiness) * 0.22 +
    records$public_consequence * 0.16
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "fragmented_narrative_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "fragmented_narrative_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "fragmentation_sensitivity_scores.png"), width = 1200, height = 700)
barplot(records$fragmentation_sensitivity, names.arg = records$item, las = 2, ylab = "Fragmentation sensitivity", main = "Fragmented Narrative Sensitivity")
grid()
dev.off()

png(file.path(figures_dir, "trauma_narrative_risk_scores.png"), width = 1200, height = 700)
barplot(records$trauma_narrative_risk, names.arg = records$item, las = 2, ylab = "Trauma-narrative risk", main = "Trauma Narrative Governance Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "fragmentation_sensitivity",
  "witness_care",
  "trauma_narrative_risk",
  "interpretation_readiness",
  "review_priority"
)])
