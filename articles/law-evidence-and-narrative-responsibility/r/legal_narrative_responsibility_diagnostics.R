# Base R workflow for Law, Evidence, and Narrative Responsibility.

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

records <- read.csv(file.path(article_root, "data", "legal_narrative_responsibility_claims.csv"), stringsAsFactors = FALSE)

records$evidence_support <- rowMeans(records[, c(
  "relevance",
  "authentication",
  "provenance",
  "corroboration",
  "cross_checking",
  "uncertainty_notation"
)])

records$narrative_overreach_risk <- pmin(
  1,
  records$overcoherence * 0.18 +
    records$evidentiary_gap * 0.18 +
    records$stereotype_reliance * 0.16 +
    records$causation_flattening * 0.16 +
    records$affective_bias * 0.16 +
    (1 - records$uncertainty_visibility) * 0.16
)

records$procedural_voice <- rowMeans(records[, c(
  "opportunity_to_be_heard",
  "discovery_access",
  "testimony_context",
  "record_access",
  "correction_pathway",
  "procedural_posture_clarity"
)])

records$testimony_responsibility <- rowMeans(records[, c(
  "witness_dignity",
  "testimony_care",
  "role_complexity",
  "testimony_context",
  "uncertainty_notation",
  "remedy_connection"
)])

records$ai_legal_narrative_risk <- pmin(
  1,
  records$hallucinated_authority * 0.22 +
    records$summary_dependence * 0.18 +
    records$context_loss * 0.18 +
    records$procedural_distortion * 0.18 +
    records$bias_reproduction * 0.14 +
    (1 - records$human_review) * 0.10
)

records$governance_priority_score <- pmin(
  1,
  records$narrative_overreach_risk * 0.30 +
    records$ai_legal_narrative_risk * 0.22 +
    (1 - records$evidence_support) * 0.18 +
    (1 - records$procedural_voice) * 0.12 +
    (1 - records$testimony_responsibility) * 0.08 +
    records$public_consequence * 0.10
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "legal_narrative_responsibility_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "legal_narrative_responsibility_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "evidence_support_scores.png"), width = 1200, height = 700)
barplot(records$evidence_support, names.arg = records$item, las = 2, ylab = "Evidence support", main = "Evidence Support")
grid()
dev.off()

png(file.path(figures_dir, "narrative_overreach_risk_scores.png"), width = 1200, height = 700)
barplot(records$narrative_overreach_risk, names.arg = records$item, las = 2, ylab = "Narrative overreach risk", main = "Narrative Overreach Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "evidence_support",
  "narrative_overreach_risk",
  "procedural_voice",
  "ai_legal_narrative_risk",
  "review_priority"
)])
