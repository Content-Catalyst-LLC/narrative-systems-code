# Base R workflow for Public Narrative and Social Change.

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

records <- read.csv(file.path(article_root, "data", "public_narrative_governance_claims.csv"), stringsAsFactors = FALSE)

records$public_narrative_coherence <- rowMeans(records[, c(
  "self_clarity",
  "us_clarity",
  "now_clarity",
  "value_articulation",
  "action_clarity",
  "governance_review"
)])

records$mobilization_readiness <- rowMeans(records[, c(
  "diagnostic_frame",
  "proposed_solution",
  "resource_support",
  "coalition_openness",
  "tactical_action",
  "feedback_loop"
)])

records$testimony_extraction_risk <- pmin(
  1,
  records$consent_deficit * 0.18 +
    records$emotional_targeting * 0.18 +
    records$safety_risk * 0.18 +
    records$reuse_uncertainty * 0.16 +
    records$visibility_risk * 0.16 +
    (1 - records$agency) * 0.14
)

records$public_voice_integrity <- rowMeans(records[, c(
  "voice_plurality",
  "affected_community_authority",
  "evidence_visibility",
  "coalition_openness",
  "digital_context",
  "governance_review"
)])

records$ai_public_narrative_risk <- pmin(
  1,
  records$summary_dependence * 0.18 +
    records$omitted_voices * 0.20 +
    records$context_loss * 0.18 +
    records$bias_reproduction * 0.16 +
    records$uncertainty_erasure * 0.16 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$testimony_extraction_risk * 0.22 +
    records$ai_public_narrative_risk * 0.20 +
    (1 - records$public_narrative_coherence) * 0.16 +
    (1 - records$mobilization_readiness) * 0.14 +
    (1 - records$public_voice_integrity) * 0.12 +
    records$public_consequence * 0.16
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "public_narrative_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "public_narrative_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "public_narrative_coherence_scores.png"), width = 1200, height = 700)
barplot(records$public_narrative_coherence, names.arg = records$item, las = 2, ylab = "Public narrative coherence", main = "Public Narrative Coherence")
grid()
dev.off()

png(file.path(figures_dir, "mobilization_readiness_scores.png"), width = 1200, height = 700)
barplot(records$mobilization_readiness, names.arg = records$item, las = 2, ylab = "Mobilization readiness", main = "Mobilization Readiness")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "public_narrative_coherence",
  "mobilization_readiness",
  "testimony_extraction_risk",
  "ai_public_narrative_risk",
  "review_priority"
)])
