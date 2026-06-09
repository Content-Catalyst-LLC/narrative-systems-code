# run_all_historical_storytelling_workflows.R
# Run all R workflows for The History of Storytelling from Oral Tradition to Modern Media.

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
  "historical_storytelling_diagnostics.R",
  "media_transition_summary.R",
  "digital_interactive_risk_summary.R"
)

for (script in scripts) {
  path <- file.path(r_dir, script)
  message("Running ", path)
  source(path)
}

message("All historical storytelling workflows completed.")
