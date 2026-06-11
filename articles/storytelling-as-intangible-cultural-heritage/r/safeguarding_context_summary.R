# safeguarding_context_summary.R
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

contexts <- read.csv(file.path(article_root, "data", "safeguarding_contexts.csv"), stringsAsFactors = FALSE)
pathways <- read.csv(file.path(article_root, "data", "transmission_pathways.csv"), stringsAsFactors = FALSE)
consent <- read.csv(file.path(article_root, "data", "consent_access_controls.csv"), stringsAsFactors = FALSE)

summary <- merge(contexts, pathways, by = "item", all = TRUE)
summary <- merge(summary, consent, by = "item", all = TRUE)

write.csv(summary, file.path(tables_dir, "safeguarding_context_summary.csv"), row.names = FALSE)
print(summary)
