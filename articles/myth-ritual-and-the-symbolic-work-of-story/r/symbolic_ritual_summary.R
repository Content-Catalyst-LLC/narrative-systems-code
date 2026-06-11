# symbolic_ritual_summary.R
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

functions <- read.csv(file.path(article_root, "data", "symbolic_functions.csv"), stringsAsFactors = FALSE)
rituals <- read.csv(file.path(article_root, "data", "ritual_contexts.csv"), stringsAsFactors = FALSE)
power <- read.csv(file.path(article_root, "data", "power_and_authority_notes.csv"), stringsAsFactors = FALSE)

summary <- merge(functions, rituals, by = "item", all = TRUE)
summary <- merge(summary, power, by = "item", all = TRUE)

write.csv(summary, file.path(tables_dir, "symbolic_ritual_power_summary.csv"), row.names = FALSE)
print(summary)
