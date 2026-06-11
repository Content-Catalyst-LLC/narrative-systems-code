# form_distinction_summary.R
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

forms <- read.csv(file.path(article_root, "data", "form_distinctions.csv"), stringsAsFactors = FALSE)
truth_claims <- read.csv(file.path(article_root, "data", "truth_claims.csv"), stringsAsFactors = FALSE)

write.csv(forms, file.path(tables_dir, "form_distinction_summary.csv"), row.names = FALSE)
write.csv(truth_claims, file.path(tables_dir, "truth_claim_summary.csv"), row.names = FALSE)

print(forms)
print(truth_claims)
