# Base R workflow for Maureen Murdock and the Heroine's Journey.

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

records <- read.csv(file.path(article_root, "data", "heroine_journey_claims.csv"), stringsAsFactors = FALSE)

records$heroine_alignment <- rowMeans(records[, c(
  "separation_from_feminine",
  "masculine_identification",
  "aridity_after_success",
  "descent_crisis",
  "reconnection_feminine",
  "integration_wholeness"
)])

records$framework_risk <- pmin(
  1,
  records$template_forcing * 0.20 +
    records$gender_essentialism * 0.20 +
    records$universal_womanhood * 0.18 +
    records$psychological_overreach * 0.18 +
    records$healing_pressure * 0.14 +
    (1 - records$cultural_context) * 0.10
)

records$critique_readiness <- rowMeans(records[, c(
  "source_context",
  "cultural_context",
  "alternative_lens",
  "gender_complexity",
  "uncertainty_notes",
  "review_owner_clarity"
)])

records$integration_quality <- rowMeans(records[, c(
  "agency",
  "relational_grounding",
  "embodiment",
  "healthy_power",
  "emotional_maturity",
  "open_process"
)])

records$governance_priority_score <- pmin(
  1,
  records$framework_risk * 0.38 +
    (1 - records$critique_readiness) * 0.24 +
    (1 - records$integration_quality) * 0.18 +
    records$public_consequence * 0.20
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "heroine_journey_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "heroine_journey_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "heroine_alignment_scores.png"), width = 1200, height = 700)
barplot(records$heroine_alignment, names.arg = records$item, las = 2, ylab = "Heroine alignment", main = "Heroine Journey Alignment")
grid()
dev.off()

png(file.path(figures_dir, "framework_risk_scores.png"), width = 1200, height = 700)
barplot(records$framework_risk, names.arg = records$item, las = 2, ylab = "Framework risk", main = "Heroine Journey Framework Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "heroine_alignment",
  "framework_risk",
  "critique_readiness",
  "integration_quality",
  "review_priority"
)])
