# storytelling_heritage_diagnostics.R
# Base R workflow for storytelling as intangible cultural heritage.

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

items <- read.csv(file.path(article_root, "data", "storytelling_heritage_items.csv"), stringsAsFactors = FALSE)

items$living_continuity <- rowMeans(items[, c(
  "transmission_support",
  "performance_context",
  "language_vitality",
  "apprenticeship_pathways",
  "community_recognition",
  "variation_management"
)])

items$safeguarding_readiness <- rowMeans(items[, c(
  "consent_clarity",
  "governance_protocol",
  "metadata_quality",
  "access_control",
  "benefit_sharing",
  "review_process"
)])

items$heritage_context_preservation <- rowMeans(items[, c(
  "occasion_context",
  "place_linkage",
  "ritual_frame",
  "embodiment",
  "social_transmission",
  "knowledge_holder_context"
)])

items$archive_risk <- pmin(
  1,
  items$context_removal * 0.18 +
    items$sacred_or_restricted_material * 0.22 +
    items$performance_omission * 0.16 +
    items$translation_loss * 0.16 +
    items$extraction_risk * 0.18 +
    (1 - items$governance_control) * 0.10
)

items$governance_priority_score <- pmin(
  1,
  items$archive_risk * 0.35 +
    items$community_sensitivity * 0.25 +
    items$public_consequence * 0.20 +
    (1 - items$safeguarding_readiness) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$archive_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$safeguarding_readiness < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$archive_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$safeguarding_readiness < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$archive_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "storytelling_heritage_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "storytelling_heritage_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "living_continuity_scores.png"), width = 1200, height = 700)
barplot(
  items$living_continuity,
  names.arg = items$item,
  las = 2,
  ylab = "Living continuity",
  main = "Storytelling Heritage Living Continuity Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "archive_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$archive_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Archive risk",
  main = "Storytelling Heritage Archive Risk Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "heritage_context",
  "living_continuity",
  "safeguarding_readiness",
  "heritage_context_preservation",
  "archive_risk",
  "governance_priority_score",
  "review_priority"
)])
