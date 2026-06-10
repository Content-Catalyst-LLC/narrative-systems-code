# folktale_morphology_diagnostics.R
# Base R workflow for folktale structure and Vladimir Propp's morphology.

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

items <- read.csv(file.path(article_root, "data", "folktale_morphology_items.csv"), stringsAsFactors = FALSE)

items$function_coverage <- rowMeans(items[, c(
  "function_identification",
  "sequence_clarity",
  "role_mapping",
  "variation_tracking",
  "context_notes"
)])

items$sequence_integrity <- rowMeans(items[, c(
  "order_coherence",
  "transition_logic",
  "gap_management",
  "repetition_awareness",
  "closure_handling"
)])

items$morphology_context_balance <- rowMeans(items[, c(
  "performance_context",
  "cultural_specificity",
  "language_notes",
  "tradition_review",
  "ethical_governance"
)])

items$reduction_risk <- pmin(
  1,
  items$universalization_risk * 0.22 +
    items$cultural_erasure_risk * 0.22 +
    items$performance_omission * 0.18 +
    items$variation_omission * 0.18 +
    (1 - items$morphology_context_balance) * 0.20
)

items$governance_priority_score <- pmin(
  1,
  items$reduction_risk * 0.35 +
    items$archive_bias * 0.20 +
    items$community_sensitivity * 0.20 +
    items$public_consequence * 0.15 +
    (1 - items$morphology_context_balance) * 0.10
)

items$review_priority <- ifelse(
  items$status == "revise" | items$reduction_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$morphology_context_balance < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$reduction_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$morphology_context_balance < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$reduction_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "folktale_morphology_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "folktale_morphology_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "function_coverage_scores.png"), width = 1200, height = 700)
barplot(
  items$function_coverage,
  names.arg = items$item,
  las = 2,
  ylab = "Function coverage",
  main = "Folktale Function Coverage Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "reduction_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$reduction_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Formula reduction risk",
  main = "Formula Reduction Risk Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "tale_type",
  "function_coverage",
  "sequence_integrity",
  "morphology_context_balance",
  "reduction_risk",
  "governance_priority_score",
  "review_priority"
)])
