# narrative_drift_summary.R
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

flags <- read.csv(file.path(article_root, "data", "narrative_drift_flags.csv"), stringsAsFactors = FALSE)
severity_score <- c(low = 1, medium = 2, high = 3)
flags$severity_score <- severity_score[flags$severity]

drift_summary <- aggregate(severity_score ~ item, data = flags, FUN = sum)
drift_summary <- drift_summary[order(drift_summary$severity_score, decreasing = TRUE), ]

write.csv(drift_summary, file.path(tables_dir, "narrative_drift_summary.csv"), row.names = FALSE)

png(file.path(figures_dir, "narrative_drift_summary.png"), width = 1000, height = 700)
barplot(
  drift_summary$severity_score,
  names.arg = drift_summary$item,
  las = 2,
  ylab = "Narrative drift severity",
  main = "Narrative Drift Summary"
)
grid()
dev.off()

print(drift_summary)
