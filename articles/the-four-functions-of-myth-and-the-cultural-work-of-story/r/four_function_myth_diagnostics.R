# Base R workflow for four-function myth diagnostics.

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

claims <- read.csv(file.path(article_root, "data", "four_function_myth_claims.csv"), stringsAsFactors = FALSE)

function_matrix <- claims[, c(
  "mystical_function",
  "cosmological_function",
  "sociological_function",
  "pedagogical_function"
)]

claims$function_balance <- apply(function_matrix, 1, function(row) {
  avg <- mean(row)
  sd_value <- sqrt(mean((row - avg)^2))
  max(0, 1 - (sd_value / (avg + 0.0001)))
})

claims$cultural_work <- rowMeans(claims[, c(
  "mystical_function",
  "cosmological_function",
  "sociological_function",
  "pedagogical_function",
  "ritual_memory",
  "authority_clarity"
)])

claims$sociological_risk <- pmin(
  1,
  claims$hierarchy_protection * 0.20 +
    claims$exclusion_risk * 0.20 +
    claims$coercive_compliance * 0.18 +
    claims$omission_risk * 0.16 +
    claims$power_invisibility * 0.16 +
    (1 - claims$accountability_marking) * 0.10
)

claims$interpretation_readiness <- rowMeans(claims[, c(
  "source_context",
  "counterexample_inclusion",
  "method_limits",
  "ethics_governance",
  "accountability_marking",
  "uncertainty_notes"
)])

claims$governance_priority_score <- pmin(
  1,
  claims$sociological_risk * 0.34 +
    claims$community_sensitivity * 0.22 +
    claims$public_consequence * 0.18 +
    (1 - claims$interpretation_readiness) * 0.16 +
    (1 - claims$source_context) * 0.10
)

claims$review_priority <- ifelse(
  claims$status == "revise" | claims$sociological_risk >= 0.55 | claims$governance_priority_score >= 0.62 | claims$interpretation_readiness < 0.55,
  "high",
  ifelse(
    claims$status == "review" | claims$sociological_risk >= 0.40 | claims$governance_priority_score >= 0.48 | claims$interpretation_readiness < 0.68,
    "medium",
    "standard"
  )
)

claims <- claims[order(claims$sociological_risk, decreasing = TRUE), ]

write.csv(claims, file.path(tables_dir, "four_function_myth_diagnostics.csv"), row.names = FALSE)
write.csv(claims[claims$review_priority != "standard", ], file.path(tables_dir, "four_function_myth_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "four_function_cultural_work_scores.png"), width = 1200, height = 700)
barplot(claims$cultural_work, names.arg = claims$item, las = 2, ylab = "Cultural work", main = "Four-Function Myth Cultural Work Scores")
grid()
dev.off()

png(file.path(figures_dir, "four_function_sociological_risk_scores.png"), width = 1200, height = 700)
barplot(claims$sociological_risk, names.arg = claims$item, las = 2, ylab = "Sociological risk", main = "Four-Function Myth Sociological Risk Scores")
grid()
dev.off()

png(file.path(figures_dir, "four_function_balance_scores.png"), width = 1200, height = 700)
barplot(claims$function_balance, names.arg = claims$item, las = 2, ylab = "Function balance", main = "Four-Function Myth Balance Scores")
grid()
dev.off()

print(claims[, c("item", "claim_context", "function_balance", "cultural_work", "sociological_risk", "interpretation_readiness", "review_priority")])
