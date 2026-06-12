# Base R workflow for Rhetorical Moves and the Ethics of Persuasive Story.

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

records <- read.csv(file.path(article_root, "data", "rhetorical_moves_governance_claims.csv"), stringsAsFactors = FALSE)

records$rhetorical_integrity <- rowMeans(records[, c(
  "evidence_truthfulness",
  "proportionality",
  "context_adequacy",
  "dignity_protection",
  "audience_agency",
  "transparency"
)])

records$manipulation_risk <- pmin(
  1,
  records$fear_amplification * 0.18 +
    records$emotional_exploitation * 0.18 +
    records$omission_of_context * 0.18 +
    records$social_proof_pressure * 0.16 +
    records$urgency_coercion * 0.16 +
    (1 - records$judgment_review) * 0.14
)

records$audience_agency_score <- rowMeans(records[, c(
  "claim_clarity",
  "uncertainty_disclosure",
  "tradeoff_openness",
  "evidence_visibility",
  "response_optionality",
  "question_space"
)])

records$platform_persuasion_risk <- pmin(
  1,
  records$platform_amplification * 0.24 +
    records$microtargeting_intensity * 0.24 +
    records$context_collapse_risk * 0.22 +
    (1 - records$sponsorship_clarity) * 0.14 +
    records$social_proof_pressure * 0.16
)

records$ai_persuasion_risk <- pmin(
  1,
  records$personalization_targeting * 0.18 +
    records$vulnerability_exploitation * 0.20 +
    records$synthetic_evidence_risk * 0.20 +
    records$opaque_testing * 0.16 +
    records$data_opacity * 0.14 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$manipulation_risk * 0.22 +
    records$platform_persuasion_risk * 0.16 +
    records$ai_persuasion_risk * 0.20 +
    (1 - records$rhetorical_integrity) * 0.16 +
    (1 - records$audience_agency_score) * 0.12 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "rhetorical_moves_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "rhetorical_moves_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "rhetorical_integrity_scores.png"), width = 1200, height = 700)
barplot(records$rhetorical_integrity, names.arg = records$item, las = 2, ylab = "Rhetorical integrity", main = "Rhetorical Integrity")
grid()
dev.off()

png(file.path(figures_dir, "manipulation_risk_scores.png"), width = 1200, height = 700)
barplot(records$manipulation_risk, names.arg = records$item, las = 2, ylab = "Manipulation risk", main = "Manipulation Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "persuasion_context",
  "rhetorical_integrity",
  "manipulation_risk",
  "audience_agency_score",
  "ai_persuasion_risk",
  "review_priority"
)])
