# oral_tradition_diagnostics.R
# Base R workflow for oral tradition, performance, and collective memory.

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

items <- read.csv(file.path(article_root, "data", "oral_tradition_items.csv"), stringsAsFactors = FALSE)

items$performance_context <- rowMeans(items[, c(
  "teller_role",
  "audience_response",
  "occasion_clarity",
  "embodiment",
  "setting_place",
  "cultural_frame"
)])

items$transmission_integrity <- rowMeans(items[, c(
  "lineage_clarity",
  "variation_tracking",
  "memory_supports",
  "governance_protocol",
  "authority_permission",
  "record_context"
)])

items$memory_function <- rowMeans(items[, c(
  "origin_memory",
  "place_memory",
  "identity_memory",
  "historical_memory",
  "ritual_memory",
  "future_obligation"
)])

items$archive_risk <- pmin(
  1,
  items$consent_limits * 0.18 +
    items$restricted_knowledge * 0.22 +
    items$exposure_risk * 0.18 +
    items$ownership_risk * 0.18 +
    items$extraction_risk * 0.14 +
    (1 - items$governance_control) * 0.10
)

items$governance_priority_score <- pmin(
  1,
  items$archive_risk * 0.35 +
    items$community_sensitivity * 0.25 +
    items$public_consequence * 0.20 +
    (1 - items$transmission_integrity) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$archive_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$transmission_integrity < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$archive_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$transmission_integrity < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$archive_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "oral_tradition_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "oral_tradition_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "performance_context_scores.png"), width = 1200, height = 700)
barplot(
  items$performance_context,
  names.arg = items$item,
  las = 2,
  ylab = "Performance context",
  main = "Performance Context Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "archive_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$archive_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Archive risk",
  main = "Archive Risk Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "tradition_type",
  "performance_context",
  "transmission_integrity",
  "memory_function",
  "archive_risk",
  "governance_priority_score",
  "review_priority"
)])
