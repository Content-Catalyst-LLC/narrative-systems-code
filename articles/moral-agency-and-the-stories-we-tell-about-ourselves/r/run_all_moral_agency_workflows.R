# Run all R workflows for Moral Agency and the Stories We Tell About Ourselves.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

source(file.path(article_root, "r", "moral_agency_diagnostics.R"))
message("All moral agency workflows completed.")
