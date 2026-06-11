# run_all_comparative_myth_workflows.R
# Run all R workflows for Joseph Campbell and the Comparative Study of Myth.

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
  "campbell_comparative_myth_diagnostics.R",
  "comparative_myth_summary.R",
  "generalization_risk_summary.R"
)

for (script in scripts) {
  path <- file.path(r_dir, script)
  message("Running ", path)
  source(path)
}

message("All comparative myth workflows completed.")
