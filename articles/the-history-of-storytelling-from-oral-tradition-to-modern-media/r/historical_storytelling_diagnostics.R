# historical_storytelling_diagnostics.R
# Base R workflow for storytelling media history diagnostics.

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

media <- read.csv(file.path(article_root, "data", "story_media_history.csv"), stringsAsFactors = FALSE)

media$transmission_strength <- rowMeans(media[, c(
  "preservation",
  "repeatability",
  "circulation",
  "archive_durability"
)])

media$preservation_risk <- pmin(
  1,
  (1 - media$archive_durability) * 0.25 +
    media$governance_complexity * 0.20 +
    (1 - media$context_retention) * 0.25 +
    (1 - media$access_openness) * 0.15 +
    (1 - media$platform_stability) * 0.15
)

media$review_priority <- ifelse(
  media$status == "review" | media$preservation_risk >= 0.50,
  "high",
  ifelse(media$preservation_risk >= 0.35, "medium", "standard")
)

media <- media[order(media$preservation_risk, decreasing = TRUE), ]

write.csv(
  media,
  file.path(tables_dir, "historical_storytelling_media_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- media[media$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "historical_storytelling_preservation_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "story_media_transmission_strength.png"), width = 1200, height = 700)
barplot(
  media$transmission_strength,
  names.arg = media$medium,
  las = 2,
  ylab = "Transmission strength",
  main = "Story Media Transmission Strength"
)
grid()
dev.off()

png(file.path(figures_dir, "story_media_preservation_risk.png"), width = 1200, height = 700)
barplot(
  media$preservation_risk,
  names.arg = media$medium,
  las = 2,
  ylab = "Preservation risk",
  main = "Story Media Preservation Risk"
)
grid()
dev.off()

print(media[, c(
  "medium",
  "period_label",
  "transmission_strength",
  "participation",
  "preservation_risk",
  "review_priority"
)])
