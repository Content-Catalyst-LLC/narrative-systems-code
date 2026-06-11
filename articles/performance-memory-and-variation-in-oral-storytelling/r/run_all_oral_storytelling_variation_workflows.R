# run_all_oral_storytelling_variation_workflows.R
# Run all R workflows for Performance, Memory, and Variation in Oral Storytelling.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

r_dir <- file.path(article_root, "r")

scripts <- c(
  "oral_storytelling_variation_diagnostics.R",
  "performance_memory_summary.R",
  "archive_risk_summary.R"
)

for (script in scripts) {
  path <- file.path(r_dir, script)
  message("Running ", path)
  source(path)
}

message("All oral storytelling variation workflows completed.")
