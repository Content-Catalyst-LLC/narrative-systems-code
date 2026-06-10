# conflict_tension_diagnostics.R
# Base R workflow for conflict, tension, and narrative movement.

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

items <- read.csv(file.path(article_root, "data", "conflict_tension_items.csv"), stringsAsFactors = FALSE)

items$conflict_clarity <- rowMeans(items[, c(
  "desire_clarity",
  "obstacle_clarity",
  "pressure_strength",
  "agency_visibility",
  "stakes_visibility",
  "relation_legibility"
)])

items$tension_durability <- rowMeans(items[, c(
  "unresolved_pressure",
  "meaningful_delay",
  "stakes_heightening",
  "expectation_pressure",
  "complication_movement"
)])

items$narrative_movement <- rowMeans(items[, c(
  "state_change",
  "knowledge_change",
  "relationship_impact",
  "pressure_change",
  "future_movement",
  "value_transformation"
)])

items$conflict_risk <- pmin(
  1,
  items$scapegoating * 0.25 +
    items$conflict_inflation * 0.20 +
    items$trauma_spectacle * 0.20 +
    items$false_balance * 0.20 +
    items$closure_pressure * 0.15
)

items$governance_priority_score <- pmin(
  1,
  items$conflict_risk * 0.35 +
    items$audience_sensitivity * 0.20 +
    items$public_consequence * 0.25 +
    (1 - items$conflict_clarity) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$conflict_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$conflict_clarity < 0.55 | items$narrative_movement < 0.50,
  "high",
  ifelse(
    items$status == "review" | items$conflict_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$conflict_clarity < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$conflict_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "conflict_tension_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "conflict_tension_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "conflict_clarity_scores.png"), width = 1200, height = 700)
barplot(
  items$conflict_clarity,
  names.arg = items$item,
  las = 2,
  ylab = "Conflict clarity",
  main = "Conflict Clarity Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "conflict_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$conflict_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Conflict risk",
  main = "Conflict Risk Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "conflict_clarity",
  "tension_durability",
  "narrative_movement",
  "conflict_risk",
  "governance_priority_score",
  "review_priority"
)])
