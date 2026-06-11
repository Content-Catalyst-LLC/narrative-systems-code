# campbell_comparative_myth_diagnostics.R
# Base R workflow for Joseph Campbell and comparative mythology analysis.

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

claims <- read.csv(file.path(article_root, "data", "comparative_myth_claims.csv"), stringsAsFactors = FALSE)

claims$comparative_pattern <- rowMeans(claims[, c(
  "departure_pattern",
  "threshold_crossing",
  "ordeal_or_trial",
  "helper_presence",
  "return_pattern",
  "boon_or_renewal"
)])

claims$cultural_specificity <- rowMeans(claims[, c(
  "language_notes",
  "ritual_context",
  "historical_context",
  "community_authority",
  "source_tradition",
  "performance_or_oral_context"
)])

claims$generalization_risk <- pmin(
  1,
  claims$universal_claim_strength * 0.18 +
    claims$selective_evidence * 0.18 +
    claims$context_loss * 0.18 +
    claims$formula_reduction * 0.16 +
    claims$ethical_risk * 0.16 +
    (1 - claims$counterexample_inclusion) * 0.14
)

claims$interpretation_readiness <- rowMeans(data.frame(
  cultural_specificity = claims$cultural_specificity,
  counterexample_inclusion = claims$counterexample_inclusion,
  method_limits = claims$method_limits,
  ritual_verification = claims$ritual_verification,
  ethics_governance = claims$ethics_governance,
  uncertainty_marking = claims$uncertainty_marking
))

claims$governance_priority_score <- pmin(
  1,
  claims$generalization_risk * 0.35 +
    claims$community_sensitivity * 0.25 +
    claims$public_consequence * 0.20 +
    (1 - claims$interpretation_readiness) * 0.20
)

claims$review_priority <- ifelse(
  claims$status == "revise" | claims$generalization_risk >= 0.55 | claims$governance_priority_score >= 0.62 | claims$interpretation_readiness < 0.55,
  "high",
  ifelse(
    claims$status == "review" | claims$generalization_risk >= 0.40 | claims$governance_priority_score >= 0.48 | claims$interpretation_readiness < 0.68,
    "medium",
    "standard"
  )
)

claims <- claims[order(claims$generalization_risk, decreasing = TRUE), ]

write.csv(
  claims,
  file.path(tables_dir, "comparative_myth_claim_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- claims[claims$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "comparative_myth_claim_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "comparative_pattern_scores.png"), width = 1200, height = 700)
barplot(
  claims$comparative_pattern,
  names.arg = claims$item,
  las = 2,
  ylab = "Comparative pattern",
  main = "Comparative Myth Pattern Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "generalization_risk_scores.png"), width = 1200, height = 700)
barplot(
  claims$generalization_risk,
  names.arg = claims$item,
  las = 2,
  ylab = "Generalization risk",
  main = "Comparative Myth Generalization Risk Scores"
)
grid()
dev.off()

print(claims[, c(
  "item",
  "claim_context",
  "comparative_pattern",
  "cultural_specificity",
  "generalization_risk",
  "interpretation_readiness",
  "governance_priority_score",
  "review_priority"
)])
