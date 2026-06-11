# Base R workflow for Gender, Critique, and the Limits of Universal Story Models.

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

records <- read.csv(file.path(article_root, "data", "universal_story_model_claims.csv"), stringsAsFactors = FALSE)

records$universal_model_fit <- rowMeans(records[, c(
  "stage_evidence",
  "agency_match",
  "transformation_correspondence",
  "contextual_harmony",
  "resolution_similarity",
  "evidence_visibility"
)])

records$universalism_risk <- pmin(
  1,
  records$archive_bias * 0.18 +
    records$gender_binary_pressure * 0.20 +
    records$cultural_flattening * 0.18 +
    records$intersectional_erasure * 0.18 +
    records$queer_trans_pressure * 0.16 +
    (1 - records$local_context) * 0.10
)

records$critique_readiness <- rowMeans(records[, c(
  "source_context",
  "local_context",
  "alternative_lens",
  "gender_complexity",
  "intersectional_context",
  "uncertainty_notes",
  "review_owner_clarity"
)])

records$alternative_structure_signal <- rowMeans(records[, c(
  "relational_motion",
  "cyclical_form",
  "witness_structure",
  "care_labor",
  "fragmented_form",
  "open_process"
)])

records$governance_priority_score <- pmin(
  1,
  records$universalism_risk * 0.38 +
    (1 - records$critique_readiness) * 0.24 +
    records$alternative_structure_signal * 0.18 +
    records$public_consequence * 0.20
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "universal_story_model_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "universal_story_model_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "universalism_risk_scores.png"), width = 1200, height = 700)
barplot(records$universalism_risk, names.arg = records$item, las = 2, ylab = "Universalism risk", main = "Universal Story Model Risk")
grid()
dev.off()

png(file.path(figures_dir, "alternative_structure_signal_scores.png"), width = 1200, height = 700)
barplot(records$alternative_structure_signal, names.arg = records$item, las = 2, ylab = "Alternative-structure signal", main = "Alternative Story Structure Signal")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "universal_model_fit",
  "universalism_risk",
  "critique_readiness",
  "alternative_structure_signal",
  "review_priority"
)])
