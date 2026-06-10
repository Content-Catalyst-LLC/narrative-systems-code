# reversal_recognition_diagnostics.R
# Base R workflow for reversal, recognition, and transformation.

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

items <- read.csv(file.path(article_root, "data", "reversal_recognition_items.csv"), stringsAsFactors = FALSE)

items$reversal_integrity <- rowMeans(items[, c(
  "preparation_trace",
  "causal_linkage",
  "state_change",
  "earned_surprise",
  "action_fit",
  "knowledge_reorientation"
)])

items$recognition_clarity <- rowMeans(items[, c(
  "evidence_visibility",
  "interpretive_support",
  "meaning_revision",
  "relation_linkage",
  "uncertainty_clarity"
)])

items$transformation_depth <- rowMeans(items[, c(
  "identity_change",
  "action_consequence",
  "relationship_change",
  "value_change",
  "future_possibility",
  "governance_accountability"
)])

items$recognition_risk <- pmin(
  1,
  items$false_recognition * 0.25 +
    items$arbitrary_twist * 0.25 +
    items$closure_pressure * 0.20 +
    items$evidence_omission * 0.20 +
    (1 - items$uncertainty_clarity) * 0.10
)

items$governance_priority_score <- pmin(
  1,
  items$recognition_risk * 0.35 +
    items$audience_sensitivity * 0.20 +
    items$public_consequence * 0.25 +
    (1 - items$recognition_clarity) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$recognition_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$reversal_integrity < 0.55 | items$transformation_depth < 0.50,
  "high",
  ifelse(
    items$status == "review" | items$recognition_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$reversal_integrity < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$recognition_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "reversal_recognition_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "reversal_recognition_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "reversal_integrity_scores.png"), width = 1200, height = 700)
barplot(
  items$reversal_integrity,
  names.arg = items$item,
  las = 2,
  ylab = "Reversal integrity",
  main = "Reversal Integrity Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "recognition_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$recognition_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Recognition risk",
  main = "Recognition Risk Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "reversal_integrity",
  "recognition_clarity",
  "transformation_depth",
  "recognition_risk",
  "governance_priority_score",
  "review_priority"
)])
