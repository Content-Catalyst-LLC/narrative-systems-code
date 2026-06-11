# performance_memory_summary.R
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

performance <- read.csv(file.path(article_root, "data", "performance_contexts.csv"), stringsAsFactors = FALSE)
memory <- read.csv(file.path(article_root, "data", "memory_supports.csv"), stringsAsFactors = FALSE)
variation <- read.csv(file.path(article_root, "data", "variation_patterns.csv"), stringsAsFactors = FALSE)

summary <- merge(performance, memory, by = "item", all = TRUE)
summary <- merge(summary, variation, by = "item", all = TRUE)

write.csv(summary, file.path(tables_dir, "performance_memory_variation_summary.csv"), row.names = FALSE)
print(summary)
