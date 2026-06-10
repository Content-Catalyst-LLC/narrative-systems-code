# run_all_aristotelian_plot_workflows.R
# Run all R workflows for Aristotle and the Earliest Theory of Plot.

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
  "aristotelian_plot_diagnostics.R",
  "plot_parts_summary.R",
  "reversal_formula_summary.R"
)

for (script in scripts) {
  path <- file.path(r_dir, script)
  message("Running ", path)
  source(path)
}

message("All Aristotelian plot workflows completed.")
