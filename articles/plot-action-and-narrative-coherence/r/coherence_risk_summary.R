# coherence_risk_summary.R
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

risks <- read.csv(file.path(article_root, "data", "coherence_risks.csv"), stringsAsFactors = FALSE)
severity_score <- c(low = 1, medium = 2, high = 3)
risks$severity_score <- severity_score[risks$severity]

risk_summary <- aggregate(severity_score ~ item, data = risks, FUN = sum)
risk_summary <- risk_summary[order(risk_summary$severity_score, decreasing = TRUE), ]

write.csv(risk_summary, file.path(tables_dir, "coherence_risk_summary.csv"), row.names = FALSE)

png(file.path(figures_dir, "coherence_risk_summary.png"), width = 1000, height = 700)
barplot(
  risk_summary$severity_score,
  names.arg = risk_summary$item,
  las = 2,
  ylab = "Coherence risk severity",
  main = "Coherence Risk Summary"
)
grid()
dev.off()

print(risk_summary)
