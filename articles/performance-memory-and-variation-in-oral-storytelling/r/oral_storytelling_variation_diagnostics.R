# oral_storytelling_variation_diagnostics.R
# Base R workflow for performance, memory, and variation in oral storytelling.

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

items <- read.csv(file.path(article_root, "data", "oral_storytelling_variation_items.csv"), stringsAsFactors = FALSE)

items$performance_context <- rowMeans(items[, c(
  "teller_role",
  "audience_documentation",
  "occasion_context",
  "place_linkage",
  "embodiment",
  "interaction_notes"
)])

items$memory_support <- rowMeans(items[, c(
  "repetition",
  "formula_use",
  "sequence_clarity",
  "audience_recognition",
  "community_correction",
  "transmission_pathway"
)])

items$variation_accountability <- rowMeans(items[, c(
  "variation_tracking",
  "context_explanation",
  "language_notes",
  "source_review",
  "access_protocol",
  "governance_oversight"
)])

items$archive_risk <- pmin(
  1,
  items$fixation_risk * 0.18 +
    items$context_removal * 0.18 +
    items$performance_omission * 0.18 +
    items$translation_loss * 0.14 +
    items$extraction_risk * 0.18 +
    (1 - items$governance_control) * 0.14
)

items$governance_priority_score <- pmin(
  1,
  items$archive_risk * 0.35 +
    items$community_sensitivity * 0.25 +
    items$public_consequence * 0.20 +
    (1 - items$variation_accountability) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$archive_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$variation_accountability < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$archive_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$variation_accountability < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$archive_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "oral_storytelling_variation_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "oral_storytelling_variation_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "performance_context_scores.png"), width = 1200, height = 700)
barplot(
  items$performance_context,
  names.arg = items$item,
  las = 2,
  ylab = "Performance context",
  main = "Oral Storytelling Performance Context Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "variation_accountability_scores.png"), width = 1200, height = 700)
barplot(
  items$variation_accountability,
  names.arg = items$item,
  las = 2,
  ylab = "Variation accountability",
  main = "Oral Storytelling Variation Accountability Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "storytelling_context",
  "performance_context",
  "memory_support",
  "variation_accountability",
  "archive_risk",
  "governance_priority_score",
  "review_priority"
)])
