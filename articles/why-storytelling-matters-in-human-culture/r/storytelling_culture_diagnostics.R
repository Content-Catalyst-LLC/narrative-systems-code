# storytelling_culture_diagnostics.R
# Base R workflow for cultural storytelling diagnostics and governance.

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

items <- read.csv(file.path(article_root, "data", "cultural_story_items.csv"), stringsAsFactors = FALSE)

items$cultural_value_score <- rowMeans(items[, c(
  "memory_function",
  "teaching_value",
  "identity_function",
  "belonging_function",
  "moral_imagination",
  "social_coordination"
)])

items$transmission_score <- rowMeans(items[, c(
  "transmission_strength",
  "source_transparency",
  "memory_function"
)])

items$narrative_risk <- pmin(
  1,
  items$persuasive_intensity * 0.25 +
    (1 - items$source_transparency) * 0.25 +
    (1 - items$representation_care) * 0.30 +
    items$audience_consequence * 0.20
)

items$review_priority_score <- pmin(
  1,
  items$narrative_risk * 0.45 +
    (1 - items$source_transparency) * 0.20 +
    (1 - items$representation_care) * 0.15 +
    items$public_impact * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$review_priority_score >= 0.50,
  "high",
  ifelse(
    items$status == "review" | items$review_priority_score >= 0.35,
    "medium",
    "standard"
  )
)

items <- items[order(items$review_priority_score, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "storytelling_culture_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "storytelling_culture_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "cultural_story_value_score.png"), width = 1200, height = 700)
barplot(
  items$cultural_value_score,
  names.arg = items$item,
  las = 2,
  ylab = "Cultural story value score",
  main = "Cultural Story Value"
)
grid()
dev.off()

png(file.path(figures_dir, "narrative_risk_score.png"), width = 1200, height = 700)
barplot(
  items$narrative_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Narrative risk score",
  main = "Narrative Risk in Cultural Storytelling"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "cultural_value_score",
  "transmission_score",
  "narrative_risk",
  "review_priority_score",
  "review_priority"
)])
