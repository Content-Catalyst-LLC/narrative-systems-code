# Base R workflow for Alternative Story Structures Beyond the Monomyth.

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

records <- read.csv(file.path(article_root, "data", "alternative_structure_claims.csv"), stringsAsFactors = FALSE)

records$structural_plurality <- rowMeans(records[, c(
  "arc_signal",
  "cycle_signal",
  "braid_signal",
  "mosaic_signal",
  "network_signal",
  "relational_signal",
  "fragment_signal"
)])

records$monomyth_overfit_risk <- pmin(
  1,
  records$hero_forcing * 0.20 +
    records$conflict_substitution * 0.18 +
    records$return_pressure * 0.16 +
    records$individualization_pressure * 0.18 +
    records$template_forcing * 0.18 +
    (1 - records$evidence_visibility) * 0.10
)

records$alternative_readiness <- rowMeans(records[, c(
  "source_context",
  "method_limits",
  "alternative_lens",
  "cultural_context",
  "uncertainty_notes",
  "review_owner_clarity"
)])

records$medium_fit <- rowMeans(records[, c(
  "temporal_match",
  "agency_design",
  "pacing_compatibility",
  "sequence_logic",
  "interaction_affordance",
  "experiential_coherence"
)])

records$governance_priority_score <- pmin(
  1,
  records$monomyth_overfit_risk * 0.36 +
    (1 - records$alternative_readiness) * 0.24 +
    records$structural_plurality * 0.18 +
    records$public_consequence * 0.22
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "alternative_structure_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "alternative_structure_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "structural_plurality_scores.png"), width = 1200, height = 700)
barplot(records$structural_plurality, names.arg = records$item, las = 2, ylab = "Structural plurality", main = "Alternative Story Structure Plurality")
grid()
dev.off()

png(file.path(figures_dir, "monomyth_overfit_risk_scores.png"), width = 1200, height = 700)
barplot(records$monomyth_overfit_risk, names.arg = records$item, las = 2, ylab = "Monomyth-overfit risk", main = "Monomyth Overfit Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "structural_plurality",
  "monomyth_overfit_risk",
  "alternative_readiness",
  "medium_fit",
  "review_priority"
)])
