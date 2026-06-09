# media_transition_summary.R
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

transitions <- read.csv(file.path(article_root, "data", "manuscript_print_transitions.csv"), stringsAsFactors = FALSE)

transitions$absolute_media_change <- (
  abs(transitions$preservation_change) +
  abs(transitions$circulation_change) +
  abs(transitions$authority_change)
) / 3

transitions <- transitions[order(transitions$absolute_media_change, decreasing = TRUE), ]

write.csv(
  transitions,
  file.path(tables_dir, "media_transition_summary.csv"),
  row.names = FALSE
)

print(transitions)
