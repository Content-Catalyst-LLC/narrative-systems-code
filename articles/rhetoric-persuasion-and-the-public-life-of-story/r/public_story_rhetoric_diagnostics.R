# public_story_rhetoric_diagnostics.R
# Base R workflow for rhetoric, persuasion, and the public life of story.

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

items <- read.csv(file.path(article_root, "data", "public_story_rhetoric_items.csv"), stringsAsFactors = FALSE)

items$rhetorical_balance <- rowMeans(items[, c(
  "ethos_strength",
  "logos_support",
  "pathos_proportionality",
  "audience_fit",
  "context_clarity"
)])

items$persuasion_force <- pmin(
  1,
  items$identification_strength * 0.25 +
    items$emotional_intensity * 0.20 +
    items$causal_clarity * 0.20 +
    items$urgency * 0.15 +
    items$action_clarity * 0.20
)

items$public_story_risk <- pmin(
  1,
  (1 - items$verification_strength) * 0.25 +
    items$emotional_coercion * 0.20 +
    items$scapegoating_risk * 0.25 +
    items$identity_manipulation * 0.15 +
    items$closure_pressure * 0.15
)

items$governance_priority_score <- pmin(
  1,
  items$persuasion_force * 0.25 +
    items$public_story_risk * 0.35 +
    items$audience_consequence * 0.20 +
    items$representation_sensitivity * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$public_story_risk >= 0.55 | items$governance_priority_score >= 0.60,
  "high",
  ifelse(
    items$status == "review" | items$public_story_risk >= 0.40 | items$governance_priority_score >= 0.45,
    "medium",
    "standard"
  )
)

items <- items[order(items$public_story_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "public_story_rhetoric_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "public_story_rhetoric_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "rhetorical_balance_scores.png"), width = 1200, height = 700)
barplot(
  items$rhetorical_balance,
  names.arg = items$item,
  las = 2,
  ylab = "Rhetorical balance",
  main = "Rhetorical Balance in Public Stories"
)
grid()
dev.off()

png(file.path(figures_dir, "public_story_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$public_story_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Public story risk",
  main = "Public Story Risk"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "rhetorical_balance",
  "persuasion_force",
  "public_story_risk",
  "governance_priority_score",
  "review_priority"
)])
