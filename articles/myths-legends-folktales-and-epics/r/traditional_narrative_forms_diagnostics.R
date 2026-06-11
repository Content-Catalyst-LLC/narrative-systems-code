# traditional_narrative_forms_diagnostics.R
# Base R workflow for myths, legends, folktales, and epics.

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

items <- read.csv(file.path(article_root, "data", "traditional_narrative_forms_items.csv"), stringsAsFactors = FALSE)

items$form_classification <- rowMeans(items[, c(
  "truth_claim_clarity",
  "social_function",
  "memory_orientation",
  "performance_trace",
  "authority_context",
  "genre_notes"
)])

items$narrative_distinction <- rowMeans(items[, c(
  "boundary_clarity",
  "category_specificity",
  "hybrid_tracking",
  "responsible_analogy",
  "variation_management"
)])

items$cultural_memory_function <- rowMeans(items[, c(
  "origin_memory",
  "place_memory",
  "ritual_memory",
  "heroic_memory",
  "identity_memory",
  "future_obligation"
)])

items$adaptation_risk <- pmin(
  1,
  items$context_removal * 0.18 +
    items$sacred_or_restricted_material * 0.22 +
    items$performance_omission * 0.16 +
    items$translation_loss * 0.16 +
    items$extraction_risk * 0.18 +
    (1 - items$governance_control) * 0.10
)

items$governance_priority_score <- pmin(
  1,
  items$adaptation_risk * 0.35 +
    items$community_sensitivity * 0.25 +
    items$public_consequence * 0.20 +
    (1 - items$narrative_distinction) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$adaptation_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$narrative_distinction < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$adaptation_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$narrative_distinction < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$adaptation_risk, decreasing = TRUE), ]

write.csv(items, file.path(tables_dir, "traditional_narrative_forms_diagnostics.csv"), row.names = FALSE)
governance_queue <- items[items$review_priority != "standard", ]
write.csv(governance_queue, file.path(tables_dir, "traditional_narrative_forms_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "form_classification_scores.png"), width = 1200, height = 700)
barplot(items$form_classification, names.arg = items$item, las = 2, ylab = "Form classification", main = "Traditional Narrative Form Classification Scores")
grid()
dev.off()

png(file.path(figures_dir, "adaptation_risk_scores.png"), width = 1200, height = 700)
barplot(items$adaptation_risk, names.arg = items$item, las = 2, ylab = "Adaptation risk", main = "Traditional Narrative Adaptation Risk Scores")
grid()
dev.off()

print(items[, c(
  "item",
  "proposed_form",
  "form_classification",
  "narrative_distinction",
  "cultural_memory_function",
  "adaptation_risk",
  "governance_priority_score",
  "review_priority"
)])
