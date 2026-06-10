# reversal_formula_summary.R
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

reversal <- read.csv(file.path(article_root, "data", "reversal_recognition_map.csv"), stringsAsFactors = FALSE)
risks <- read.csv(file.path(article_root, "data", "formula_risks.csv"), stringsAsFactors = FALSE)

severity_score <- c(low = 1, medium = 2, high = 3)
risks$severity_score <- severity_score[risks$severity]

risk_summary <- aggregate(severity_score ~ item, data = risks, FUN = sum)
risk_summary <- risk_summary[order(risk_summary$severity_score, decreasing = TRUE), ]

combined <- merge(reversal, risk_summary, by = "item", all = TRUE)
write.csv(combined, file.path(tables_dir, "reversal_formula_summary.csv"), row.names = FALSE)

png(file.path(figures_dir, "formula_risk_severity_summary.png"), width = 1000, height = 700)
barplot(
  risk_summary$severity_score,
  names.arg = risk_summary$item,
  las = 2,
  ylab = "Formula risk severity",
  main = "Formula Risk Severity Summary"
)
grid()
dev.off()

print(combined)
