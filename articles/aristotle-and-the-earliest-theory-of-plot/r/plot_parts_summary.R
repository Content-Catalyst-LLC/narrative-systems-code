# plot_parts_summary.R
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

plot_parts <- read.csv(file.path(article_root, "data", "plot_parts.csv"), stringsAsFactors = FALSE)
unity <- read.csv(file.path(article_root, "data", "unity_action_checks.csv"), stringsAsFactors = FALSE)

summary <- merge(plot_parts, unity, by = "item", all = TRUE)
write.csv(summary, file.path(tables_dir, "plot_parts_unity_summary.csv"), row.names = FALSE)
print(summary)
