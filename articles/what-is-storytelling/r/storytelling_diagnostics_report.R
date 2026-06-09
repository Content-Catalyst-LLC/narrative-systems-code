# storytelling_diagnostics_report.R
# Base R workflow for storytelling structure and governance diagnostics.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

setwd(article_root)

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

items <- read.csv(file.path(article_root, "data", "storytelling_items.csv"), stringsAsFactors = FALSE)

items$coherence_score <- rowMeans(items[, c(
  "sequence_clarity",
  "agency_clarity",
  "causal_connection",
  "transformation_clarity",
  "interpretive_relevance"
)])

items$craft_score <- rowMeans(items[, c(
  "sequence_clarity",
  "conflict_definition",
  "transformation_clarity",
  "motif_use",
  "interpretive_relevance"
)])

items$governance_risk <- pmin(
  1,
  (1 - items$evidence_strength) * 0.30 +
    (1 - items$representation_care) * 0.30 +
    items$persuasive_intensity * 0.20 +
    items$audience_consequence * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$governance_risk >= 0.48,
  "high",
  ifelse(
    items$status == "review" | items$governance_risk >= 0.34,
    "medium",
    "standard"
  )
)

items <- items[order(items$governance_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "storytelling_diagnostics_summary.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "storytelling_governance_queue_r.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "storytelling_coherence_score.png"), width = 1200, height = 700)
barplot(
  items$coherence_score,
  names.arg = items$item,
  las = 2,
  ylab = "Narrative coherence score",
  main = "Storytelling Coherence Score"
)
grid()
dev.off()

png(file.path(figures_dir, "storytelling_governance_risk.png"), width = 1200, height = 700)
barplot(
  items$governance_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Governance risk",
  main = "Storytelling Governance Risk"
)
grid()
dev.off()

print(items[, c(
  "item",
  "story_type",
  "coherence_score",
  "craft_score",
  "governance_risk",
  "review_priority"
)])
