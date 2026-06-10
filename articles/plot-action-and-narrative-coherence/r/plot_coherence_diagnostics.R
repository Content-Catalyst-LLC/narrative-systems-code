# plot_coherence_diagnostics.R
# Base R workflow for plot, action, and narrative coherence.

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

items <- read.csv(file.path(article_root, "data", "plot_coherence_items.csv"), stringsAsFactors = FALSE)

items$plot_coherence <- rowMeans(items[, c(
  "action_clarity",
  "causal_linkage",
  "motivation_visibility",
  "episode_dependency",
  "turning_point_strength",
  "resolution_consequence"
)])

items$action_dependency <- rowMeans(items[, c(
  "state_change",
  "knowledge_change",
  "pressure_change",
  "relationship_impact",
  "future_movement"
)])

items$coherence_risk <- pmin(
  1,
  items$false_causality * 0.25 +
    items$simplification_bias * 0.20 +
    items$closure_pressure * 0.20 +
    items$evidence_omission * 0.20 +
    (1 - items$uncertainty_clarity) * 0.15
)

items$governance_priority_score <- pmin(
  1,
  items$plot_coherence * 0.20 +
    items$coherence_risk * 0.35 +
    items$audience_sensitivity * 0.20 +
    items$public_consequence * 0.25
)

items$review_priority <- ifelse(
  items$status == "revise" | items$coherence_risk >= 0.55 | items$plot_coherence < 0.55 | items$governance_priority_score >= 0.62,
  "high",
  ifelse(
    items$status == "review" | items$coherence_risk >= 0.40 | items$plot_coherence < 0.68 | items$governance_priority_score >= 0.48,
    "medium",
    "standard"
  )
)

items <- items[order(items$coherence_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "plot_coherence_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "plot_coherence_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "plot_coherence_scores.png"), width = 1200, height = 700)
barplot(
  items$plot_coherence,
  names.arg = items$item,
  las = 2,
  ylab = "Plot coherence",
  main = "Plot Coherence Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "coherence_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$coherence_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Coherence risk",
  main = "Narrative Coherence Risk"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "plot_coherence",
  "action_dependency",
  "coherence_risk",
  "governance_priority_score",
  "review_priority"
)])
