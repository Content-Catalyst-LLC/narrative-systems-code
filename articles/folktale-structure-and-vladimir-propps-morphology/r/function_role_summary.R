# function_role_summary.R
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

functions <- read.csv(file.path(article_root, "data", "propp_function_map.csv"), stringsAsFactors = FALSE)
roles <- read.csv(file.path(article_root, "data", "spheres_of_action.csv"), stringsAsFactors = FALSE)

summary <- merge(functions, roles, by = "item", all = TRUE)
write.csv(summary, file.path(tables_dir, "function_role_summary.csv"), row.names = FALSE)
print(summary)
