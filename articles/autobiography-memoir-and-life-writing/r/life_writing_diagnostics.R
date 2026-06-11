# Base R workflow for Autobiography, Memoir, and Life-Writing.

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

records <- read.csv(file.path(article_root, "data", "life_writing_claims.csv"), stringsAsFactors = FALSE)

records$life_writing_coherence <- rowMeans(records[, c(
  "memory_clarity",
  "temporal_structure",
  "voice_consistency",
  "agency",
  "relational_grounding",
  "contextual_depth"
)])

records$truth_practice <- rowMeans(records[, c(
  "fact_checking",
  "memory_framing",
  "evidence_visibility",
  "interpretation_distinction",
  "uncertainty_notes",
  "archive_review"
)])

records$ethical_risk <- pmin(
  1,
  records$privacy_risk * 0.18 +
    records$consent_limits * 0.20 +
    records$other_person_exposure * 0.20 +
    records$trauma_extraction * 0.18 +
    records$self_mythology * 0.14 +
    (1 - records$method_limits) * 0.10
)

records$interpretation_readiness <- rowMeans(records[, c(
  "source_context",
  "cultural_context",
  "evidence_visibility",
  "uncertainty_notes",
  "method_limits",
  "review_owner_clarity"
)])

records$governance_priority_score <- pmin(
  1,
  records$ethical_risk * 0.40 +
    (1 - records$truth_practice) * 0.22 +
    (1 - records$interpretation_readiness) * 0.22 +
    records$public_consequence * 0.16
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "life_writing_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "life_writing_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "life_writing_coherence_scores.png"), width = 1200, height = 700)
barplot(records$life_writing_coherence, names.arg = records$item, las = 2, ylab = "Life-writing coherence", main = "Life-Writing Coherence")
grid()
dev.off()

png(file.path(figures_dir, "life_writing_ethical_risk_scores.png"), width = 1200, height = 700)
barplot(records$ethical_risk, names.arg = records$item, las = 2, ylab = "Ethical risk", main = "Life-Writing Ethical Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "life_writing_coherence",
  "truth_practice",
  "ethical_risk",
  "interpretation_readiness",
  "review_priority"
)])
