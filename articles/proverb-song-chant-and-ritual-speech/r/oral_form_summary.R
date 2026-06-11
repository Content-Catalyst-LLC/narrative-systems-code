# oral_form_summary.R
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

contexts <- read.csv(file.path(article_root, "data", "oral_form_contexts.csv"), stringsAsFactors = FALSE)
sound <- read.csv(file.path(article_root, "data", "sound_repetition_features.csv"), stringsAsFactors = FALSE)
authority <- read.csv(file.path(article_root, "data", "ritual_authority_notes.csv"), stringsAsFactors = FALSE)

summary <- merge(contexts, sound, by = "item", all = TRUE)
summary <- merge(summary, authority, by = "item", all = TRUE)

write.csv(summary, file.path(tables_dir, "oral_form_context_sound_authority_summary.csv"), row.names = FALSE)
print(summary)
