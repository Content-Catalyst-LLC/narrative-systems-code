# narrative_understanding_diagnostics.R
# Base R workflow for story as a mode of human understanding.

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

items <- read.csv(file.path(article_root, "data", "narrative_understanding_items.csv"), stringsAsFactors = FALSE)

items$understanding_score <- rowMeans(items[, c(
  "sequence_clarity",
  "causal_framing",
  "agency_mapping",
  "memory_integration",
  "evidence_support",
  "openness_to_revision"
)])

items$moral_understanding_score <- rowMeans(items[, c(
  "consequence_visibility",
  "agency_mapping",
  "harm_recognition",
  "responsibility_mapping",
  "repair_awareness"
)])

items$possible_world_score <- rowMeans(items[, c(
  "alternative_logic",
  "causal_framing",
  "uncertainty_signaling",
  "interpretive_diversity",
  "openness_to_revision"
)])

items$overreach_risk <- pmin(
  1,
  (1 - items$evidence_support) * 0.25 +
    items$hindsight_bias * 0.20 +
    items$false_coherence * 0.25 +
    items$selection_bias * 0.15 +
    items$closure_pressure * 0.15
)

items$review_priority <- ifelse(
  items$status == "revise" | items$overreach_risk >= 0.50,
  "high",
  ifelse(
    items$status == "review" | items$overreach_risk >= 0.35,
    "medium",
    "standard"
  )
)

items <- items[order(items$overreach_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "narrative_understanding_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "narrative_understanding_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "narrative_understanding_score.png"), width = 1200, height = 700)
barplot(
  items$understanding_score,
  names.arg = items$item,
  las = 2,
  ylab = "Narrative understanding score",
  main = "Narrative Understanding"
)
grid()
dev.off()

png(file.path(figures_dir, "narrative_overreach_risk.png"), width = 1200, height = 700)
barplot(
  items$overreach_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Narrative overreach risk",
  main = "Narrative Overreach Risk"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "understanding_score",
  "moral_understanding_score",
  "possible_world_score",
  "overreach_risk",
  "review_priority"
)])
