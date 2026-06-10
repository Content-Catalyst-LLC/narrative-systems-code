# recognition_event_summary.R
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

tables_dir <- file.path(article_root, "outputs", "tables")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)

reversals <- read.csv(file.path(article_root, "data", "reversal_patterns.csv"), stringsAsFactors = FALSE)
recognitions <- read.csv(file.path(article_root, "data", "recognition_events.csv"), stringsAsFactors = FALSE)

summary <- merge(reversals, recognitions, by = "item", all = TRUE)
write.csv(summary, file.path(tables_dir, "recognition_event_summary.csv"), row.names = FALSE)
print(summary)
