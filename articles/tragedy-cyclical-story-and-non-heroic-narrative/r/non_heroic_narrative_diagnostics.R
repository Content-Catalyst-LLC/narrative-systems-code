# Base R workflow for Tragedy, Cyclical Story, and Non-Heroic Narrative.

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

records <- read.csv(file.path(article_root, "data", "non_heroic_narrative_claims.csv"), stringsAsFactors = FALSE)

records$tragic_structure <- rowMeans(records[, c(
  "consequential_action",
  "limit_pressure",
  "reversal",
  "recognition_knowledge",
  "irreversibility",
  "witness_burden"
)])

records$cyclical_structure <- rowMeans(records[, c(
  "repeated_pattern",
  "seasonal_ritual_signal",
  "generational_transmission",
  "institutional_habit",
  "ecological_feedback",
  "variation_across_return"
)])

records$non_heroic_agency <- rowMeans(records[, c(
  "care",
  "endurance",
  "witness",
  "refusal",
  "maintenance",
  "survival"
)])

records$heroic_overfit_risk <- pmin(
  1,
  records$hero_forcing * 0.18 +
    records$victory_pressure * 0.18 +
    records$closure_pressure * 0.18 +
    records$return_pressure * 0.16 +
    records$growth_pressure * 0.16 +
    (1 - records$evidence_visibility) * 0.14
)

records$review_readiness <- rowMeans(records[, c(
  "source_context",
  "method_limits",
  "uncertainty_notes",
  "review_owner_clarity",
  "evidence_visibility"
)])

records$governance_priority_score <- pmin(
  1,
  records$heroic_overfit_risk * 0.34 +
    (1 - records$review_readiness) * 0.24 +
    pmax(records$tragic_structure, records$cyclical_structure, records$non_heroic_agency) * 0.18 +
    records$public_consequence * 0.24
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "non_heroic_narrative_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "non_heroic_narrative_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "tragic_structure_scores.png"), width = 1200, height = 700)
barplot(records$tragic_structure, names.arg = records$item, las = 2, ylab = "Tragic structure", main = "Tragic Structure Signal")
grid()
dev.off()

png(file.path(figures_dir, "non_heroic_agency_scores.png"), width = 1200, height = 700)
barplot(records$non_heroic_agency, names.arg = records$item, las = 2, ylab = "Non-heroic agency", main = "Non-Heroic Agency Signal")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "tragic_structure",
  "cyclical_structure",
  "non_heroic_agency",
  "heroic_overfit_risk",
  "review_priority"
)])
