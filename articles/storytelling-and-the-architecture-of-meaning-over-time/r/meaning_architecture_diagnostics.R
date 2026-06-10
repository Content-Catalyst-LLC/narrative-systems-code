# meaning_architecture_diagnostics.R
# Base R workflow for storytelling and meaning over time.

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

items <- read.csv(file.path(article_root, "data", "meaning_architecture_items.csv"), stringsAsFactors = FALSE)

items$temporal_coherence <- rowMeans(items[, c(
  "origin_clarity",
  "sequence_clarity",
  "continuity_support",
  "rupture_recognition",
  "future_projection",
  "governance_visibility"
)])

items$memory_durability <- rowMeans(items[, c(
  "preservation",
  "archive_support",
  "repetition_strength",
  "context_retention",
  "transmission_strength"
)])

items$drift_risk <- pmin(
  1,
  (1 - items$evidence_strength) * 0.25 +
    items$source_age * 0.20 +
    items$link_breakage * 0.20 +
    (1 - items$context_retention) * 0.20 +
    items$repetition_strength * 0.15
)

items$revision_priority_score <- pmin(
  1,
  items$drift_risk * 0.40 +
    items$audience_consequence * 0.20 +
    items$representation_risk * 0.20 +
    items$map_dependency * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$revision_priority_score >= 0.50,
  "high",
  ifelse(
    items$status == "review" | items$revision_priority_score >= 0.35,
    "medium",
    "standard"
  )
)

items <- items[order(items$revision_priority_score, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "meaning_architecture_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "meaning_architecture_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "temporal_meaning_coherence.png"), width = 1200, height = 700)
barplot(
  items$temporal_coherence,
  names.arg = items$item,
  las = 2,
  ylab = "Temporal coherence",
  main = "Temporal Meaning Coherence"
)
grid()
dev.off()

png(file.path(figures_dir, "narrative_drift_risk.png"), width = 1200, height = 700)
barplot(
  items$drift_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Narrative drift risk",
  main = "Narrative Drift Risk"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "temporal_coherence",
  "memory_durability",
  "drift_risk",
  "revision_priority_score",
  "review_priority"
)])
