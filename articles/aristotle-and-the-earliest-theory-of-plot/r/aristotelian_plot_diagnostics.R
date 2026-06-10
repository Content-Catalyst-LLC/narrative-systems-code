# aristotelian_plot_diagnostics.R
# Base R workflow for Aristotle and the earliest theory of plot.

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

items <- read.csv(file.path(article_root, "data", "aristotelian_plot_items.csv"), stringsAsFactors = FALSE)

items$plot_unity <- rowMeans(items[, c(
  "action_clarity",
  "causal_linkage",
  "episode_dependency",
  "turning_point_relevance",
  "resolution_support",
  "goal_coherence"
)])

items$reversal_recognition_strength <- rowMeans(items[, c(
  "direction_change",
  "knowledge_change",
  "preparation_strength",
  "consequence_pressure",
  "emotional_intellectual_impact"
)])

items$formula_risk <- pmin(
  1,
  items$hero_template_saturation * 0.20 +
    items$closure_pressure * 0.25 +
    items$unity_bias * 0.20 +
    items$genre_bias * 0.20 +
    (1 - items$medium_fit) * 0.15
)

items$governance_score <- rowMeans(cbind(
  items$plot_unity,
  items$character_action_integration,
  items$genre_fit,
  items$medium_fit,
  items$cultural_awareness
))

items$review_priority <- ifelse(
  items$status == "revise" | items$formula_risk >= 0.55 | items$plot_unity < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$formula_risk >= 0.40 | items$plot_unity < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$formula_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "aristotelian_plot_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "aristotelian_plot_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "plot_unity_scores.png"), width = 1200, height = 700)
barplot(
  items$plot_unity,
  names.arg = items$item,
  las = 2,
  ylab = "Plot unity",
  main = "Aristotelian Plot Unity"
)
grid()
dev.off()

png(file.path(figures_dir, "formula_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$formula_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Formula risk",
  main = "Plot Formula Risk"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "plot_unity",
  "reversal_recognition_strength",
  "formula_risk",
  "governance_score",
  "review_priority"
)])
