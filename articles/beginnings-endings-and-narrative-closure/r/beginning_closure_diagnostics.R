# beginning_closure_diagnostics.R
# Base R workflow for beginnings, endings, and narrative closure.

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

items <- read.csv(file.path(article_root, "data", "beginning_closure_items.csv"), stringsAsFactors = FALSE)

items$opening_clarity <- rowMeans(items[, c(
  "voice_signal",
  "world_orientation",
  "pressure_introduction",
  "stakes_visibility",
  "question_framing",
  "contract_transparency"
)])

items$closure_integrity <- rowMeans(items[, c(
  "promise_fulfillment",
  "resolution_suitability",
  "transformation_depth",
  "aftermath_clarity",
  "emotional_honesty",
  "unresolved_harm_honesty"
)])

items$beginning_ending_alignment <- rowMeans(items[, c(
  "motif_return",
  "question_answer",
  "interpretive_echo",
  "thematic_continuity",
  "frame_revision"
)])

items$closure_risk <- pmin(
  1,
  items$premature_repair * 0.24 +
    items$false_resolution * 0.24 +
    items$system_flattening * 0.20 +
    items$aftermath_omission * 0.18 +
    items$excessive_audience_comfort * 0.14
)

items$governance_priority_score <- pmin(
  1,
  items$closure_risk * 0.35 +
    items$audience_sensitivity * 0.20 +
    items$public_consequence * 0.25 +
    (1 - items$closure_integrity) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$closure_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$closure_integrity < 0.55 | items$opening_clarity < 0.50,
  "high",
  ifelse(
    items$status == "review" | items$closure_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$closure_integrity < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$closure_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "beginning_closure_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "beginning_closure_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "opening_clarity_scores.png"), width = 1200, height = 700)
barplot(
  items$opening_clarity,
  names.arg = items$item,
  las = 2,
  ylab = "Opening clarity",
  main = "Opening Clarity Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "closure_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$closure_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Closure risk",
  main = "Closure Risk Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "opening_clarity",
  "closure_integrity",
  "beginning_ending_alignment",
  "closure_risk",
  "governance_priority_score",
  "review_priority"
)])
