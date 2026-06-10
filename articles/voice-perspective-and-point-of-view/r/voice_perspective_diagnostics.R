# voice_perspective_diagnostics.R
# Base R workflow for voice, perspective, and point of view.

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

items <- read.csv(file.path(article_root, "data", "voice_perspective_items.csv"), stringsAsFactors = FALSE)

items$voice_consistency <- rowMeans(items[, c(
  "tone_stability",
  "diction_coherence",
  "rhetorical_habit",
  "address_stability",
  "judgment_coherence"
)])

items$perspective_access <- rowMeans(items[, c(
  "knowledge_limits",
  "interior_access",
  "focalization_clarity",
  "level_stability",
  "source_boundaries"
)])

items$reliability_risk <- pmin(
  1,
  items$factual_unreliability * 0.20 +
    items$interpretive_unreliability * 0.20 +
    items$ethical_unreliability * 0.20 +
    items$memory_distortion * 0.20 +
    items$agency_gap * 0.20
)

items$governance_priority_score <- pmin(
  1,
  (1 - items$perspective_access) * 0.20 +
    items$reliability_risk * 0.30 +
    items$exposure_sensitivity * 0.20 +
    items$public_consequence * 0.20 +
    items$representation_gap * 0.10
)

items$review_priority <- ifelse(
  items$status == "revise" | items$reliability_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$perspective_access < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$reliability_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$perspective_access < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$governance_priority_score, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "voice_perspective_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "voice_perspective_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "voice_consistency_scores.png"), width = 1200, height = 700)
barplot(
  items$voice_consistency,
  names.arg = items$item,
  las = 2,
  ylab = "Voice consistency",
  main = "Voice Consistency Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "perspective_governance_priority.png"), width = 1200, height = 700)
barplot(
  items$governance_priority_score,
  names.arg = items$item,
  las = 2,
  ylab = "Governance priority",
  main = "Perspective Governance Priority"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "voice_consistency",
  "perspective_access",
  "reliability_risk",
  "governance_priority_score",
  "review_priority"
)])
