# Base R workflow for Moral Agency and the Stories We Tell About Ourselves.

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

records <- read.csv(file.path(article_root, "data", "moral_agency_claims.csv"), stringsAsFactors = FALSE)

records$moral_clarity <- rowMeans(records[, c(
  "action_naming",
  "intention_distinction",
  "consequence_clarity",
  "harm_marking",
  "repair_orientation",
  "other_visibility"
)])

records$excuse_risk <- pmin(
  1,
  records$context_overuse * 0.16 +
    records$intention_shielding * 0.18 +
    records$victimhood_shielding * 0.18 +
    records$blame_shifting * 0.18 +
    records$growth_substitution * 0.16 +
    records$harm_minimization * 0.14
)

records$repair_readiness <- rowMeans(records[, c(
  "harm_acknowledgment",
  "apology_precision",
  "material_response",
  "conduct_change",
  "future_accountability",
  "third_party_oversight"
)])

records$interpretation_readiness <- rowMeans(records[, c(
  "source_context",
  "evidence_visibility",
  "uncertainty_notes",
  "cultural_context",
  "method_limits",
  "review_owner_clarity"
)])

records$governance_priority_score <- pmin(
  1,
  records$excuse_risk * 0.36 +
    (1 - records$repair_readiness) * 0.24 +
    (1 - records$interpretation_readiness) * 0.22 +
    records$public_consequence * 0.18
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "moral_agency_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "moral_agency_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "moral_clarity_scores.png"), width = 1200, height = 700)
barplot(records$moral_clarity, names.arg = records$item, las = 2, ylab = "Moral clarity", main = "Moral Self-Narrative Clarity")
grid()
dev.off()

png(file.path(figures_dir, "excuse_risk_scores.png"), width = 1200, height = 700)
barplot(records$excuse_risk, names.arg = records$item, las = 2, ylab = "Excuse risk", main = "Moral Self-Narrative Excuse Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "moral_clarity",
  "excuse_risk",
  "repair_readiness",
  "interpretation_readiness",
  "review_priority"
)])
