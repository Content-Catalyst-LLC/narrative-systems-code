# monomyth_summary.R
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

sources <- read.csv(file.path(article_root, "data", "source_contexts.csv"), stringsAsFactors = FALSE)
patterns <- read.csv(file.path(article_root, "data", "pattern_features.csv"), stringsAsFactors = FALSE)
specificity <- read.csv(file.path(article_root, "data", "specificity_notes.csv"), stringsAsFactors = FALSE)

summary <- merge(sources, patterns, by = "item", all = TRUE)
summary <- merge(summary, specificity, by = "item", all = TRUE)

write.csv(summary, file.path(tables_dir, "monomyth_source_pattern_summary.csv"), row.names = FALSE)
print(summary)
