# monomyth_claim_diagnostics.R
# Base R workflow for auditing monomyth claims.

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

claims <- read.csv(file.path(article_root, "data", "monomyth_claims.csv"), stringsAsFactors = FALSE)

claims$monomyth_pattern <- rowMeans(claims[, c(
  "departure_pattern",
  "threshold_crossing",
  "initiation_trial",
  "descent_symbolic_death",
  "boon",
  "return_pattern"
)])

claims$specificity_preservation <- rowMeans(claims[, c(
  "language_notes",
  "cultural_tradition",
  "ritual_context",
  "historical_context",
  "oral_performance_context",
  "authority_notes"
)])

claims$formula_drift <- pmin(
  1,
  claims$stage_literalism * 0.18 +
    claims$beat_matching * 0.18 +
    claims$context_loss * 0.18 +
    claims$overfitting * 0.16 +
    claims$universal_claim_strength * 0.16 +
    (1 - claims$counterexample_inclusion) * 0.14
)

claims$interpretation_readiness <- rowMeans(data.frame(
  specificity_preservation = claims$specificity_preservation,
  counterexample_inclusion = claims$counterexample_inclusion,
  method_limits = claims$method_limits,
  ethics_governance = claims$ethics_governance,
  ritual_verification = claims$ritual_verification,
  uncertainty_marking = claims$uncertainty_marking
))

claims$governance_priority_score <- pmin(
  1,
  claims$formula_drift * 0.35 +
    claims$community_sensitivity * 0.25 +
    claims$public_consequence * 0.20 +
    (1 - claims$interpretation_readiness) * 0.20
)

claims$review_priority <- ifelse(
  claims$status == "revise" | claims$formula_drift >= 0.55 | claims$governance_priority_score >= 0.62 | claims$interpretation_readiness < 0.55,
  "high",
  ifelse(
    claims$status == "review" | claims$formula_drift >= 0.40 | claims$governance_priority_score >= 0.48 | claims$interpretation_readiness < 0.68,
    "medium",
    "standard"
  )
)

claims <- claims[order(claims$formula_drift, decreasing = TRUE), ]

write.csv(
  claims,
  file.path(tables_dir, "monomyth_claim_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- claims[claims$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "monomyth_claim_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "monomyth_pattern_scores.png"), width = 1200, height = 700)
barplot(
  claims$monomyth_pattern,
  names.arg = claims$item,
  las = 2,
  ylab = "Monomyth pattern",
  main = "Monomyth Pattern Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "formula_drift_scores.png"), width = 1200, height = 700)
barplot(
  claims$formula_drift,
  names.arg = claims$item,
  las = 2,
  ylab = "Formula drift",
  main = "Monomyth Formula Drift Scores"
)
grid()
dev.off()

print(claims[, c(
  "item",
  "claim_context",
  "monomyth_pattern",
  "specificity_preservation",
  "formula_drift",
  "interpretation_readiness",
  "governance_priority_score",
  "review_priority"
)])
