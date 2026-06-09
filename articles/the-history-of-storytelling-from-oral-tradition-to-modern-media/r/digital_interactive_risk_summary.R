# digital_interactive_risk_summary.R
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

digital <- read.csv(file.path(article_root, "data", "digital_interactive_media.csv"), stringsAsFactors = FALSE)

risk_map <- c(low = 1, medium = 2, high = 3)
digital$governance_risk_score <- risk_map[digital$governance_risk]

digital$platform_story_pressure <- rowMeans(digital[, c(
  "networking",
  "remix",
  "metrics",
  "algorithmic_visibility"
)])

digital <- digital[order(digital$platform_story_pressure, decreasing = TRUE), ]

write.csv(
  digital,
  file.path(tables_dir, "digital_interactive_risk_summary.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "digital_interactive_story_pressure.png"), width = 1000, height = 700)
barplot(
  digital$platform_story_pressure,
  names.arg = digital$medium,
  las = 2,
  ylab = "Platform story pressure",
  main = "Digital and Interactive Story Pressure"
)
grid()
dev.off()

print(digital)
