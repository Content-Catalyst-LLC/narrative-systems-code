# Base R workflow for threshold and ordeal diagnostics.

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

claims <- read.csv(file.path(article_root, "data", "threshold_ordeal_claims.csv"), stringsAsFactors = FALSE)

claims$ethical_risk <- pmin(
  1,
  claims$harm_romanticization * 0.20 +
    claims$suffering_spectacle * 0.18 +
    claims$forced_closure * 0.18 +
    claims$context_loss * 0.16 +
    claims$power_hiding * 0.16 +
    (1 - claims$unresolved_marking) * 0.12
)

claims$interpretation_readiness <- rowMeans(claims[, c(
  "specificity_preservation",
  "counterexample_inclusion",
  "method_limits",
  "ethics_governance",
  "uncertainty_marking"
)])

claims$governance_priority_score <- pmin(
  1,
  claims$ethical_risk * 0.32 +
    claims$community_sensitivity * 0.22 +
    claims$public_consequence * 0.18 +
    (1 - claims$ordeal_transformation) * 0.14 +
    (1 - claims$interpretation_readiness) * 0.14
)

claims$review_priority <- ifelse(
  claims$status == "revise" | claims$ethical_risk >= 0.55 | claims$governance_priority_score >= 0.62 | claims$interpretation_readiness < 0.55,
  "high",
  ifelse(
    claims$status == "review" | claims$ethical_risk >= 0.40 | claims$governance_priority_score >= 0.48 | claims$interpretation_readiness < 0.68,
    "medium",
    "standard"
  )
)

claims <- claims[order(claims$ethical_risk, decreasing = TRUE), ]

write.csv(claims, file.path(tables_dir, "threshold_ordeal_diagnostics.csv"), row.names = FALSE)
write.csv(claims[claims$review_priority != "standard", ], file.path(tables_dir, "threshold_ordeal_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "threshold_strength_scores.png"), width = 1200, height = 700)
barplot(claims$threshold_strength, names.arg = claims$item, las = 2, ylab = "Threshold strength", main = "Threshold Strength Scores")
grid()
dev.off()

png(file.path(figures_dir, "ordeal_transformation_scores.png"), width = 1200, height = 700)
barplot(claims$ordeal_transformation, names.arg = claims$item, las = 2, ylab = "Ordeal transformation", main = "Ordeal Transformation Scores")
grid()
dev.off()

png(file.path(figures_dir, "ethical_risk_scores.png"), width = 1200, height = 700)
barplot(claims$ethical_risk, names.arg = claims$item, las = 2, ylab = "Ethical risk", main = "Threshold and Ordeal Ethical Risk Scores")
grid()
dev.off()

print(claims[, c("item", "claim_context", "threshold_strength", "trial_depth", "ordeal_transformation", "ethical_risk", "interpretation_readiness", "review_priority")])
