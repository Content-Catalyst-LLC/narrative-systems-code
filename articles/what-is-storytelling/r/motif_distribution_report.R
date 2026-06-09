# motif_distribution_report.R
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

motifs <- read.csv(file.path(article_root, "data", "motifs.csv"), stringsAsFactors = FALSE)
motifs$motif_score <- motifs$frequency * motifs$interpretive_weight
motifs <- motifs[order(motifs$motif_score, decreasing = TRUE), ]

write.csv(motifs, file.path(tables_dir, "motif_distribution_report.csv"), row.names = FALSE)

png(file.path(figures_dir, "motif_scores.png"), width = 1000, height = 700)
barplot(
  motifs$motif_score,
  names.arg = motifs$motif,
  las = 2,
  ylab = "Motif score",
  main = "Motif Recurrence and Interpretive Weight"
)
grid()
dev.off()

print(motifs)
