# Run all R workflows for Paul Ricoeur and Narrative Time.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

source(file.path(article_root, "r", "ricoeur_narrative_time_diagnostics.R"))
message("All Ricoeur narrative-time workflows completed.")
