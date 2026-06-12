# Base R workflow for Narrative Risk and the Misuse of Story.

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

records <- read.csv(file.path(article_root, "data", "narrative_risk_governance_claims.csv"), stringsAsFactors = FALSE)

records$narrative_risk <- pmin(
  1,
  records$scapegoating * 0.18 +
    records$evidence_immunity * 0.20 +
    records$mythic_simplification * 0.18 +
    records$context_loss * 0.16 +
    records$group_blame_intensity * 0.16 +
    (1 - records$revision_openness) * 0.12
)

records$evidence_integrity <- rowMeans(records[, c(
  "corroboration",
  "source_quality",
  "timeline_clarity",
  "uncertainty_disclosure",
  "accountability_clarity",
  "disconfirmation_openness"
)])

records$trust_repair_priority <- pmin(
  1,
  records$institutional_failure * 0.18 +
    records$opacity * 0.18 +
    records$historical_distrust_reason * 0.18 +
    records$public_consequence * 0.18 +
    records$correction_difficulty * 0.14 +
    records$affected_listener_stakes * 0.14
)

records$platform_amplification_risk <- pmin(
  1,
  records$platform_speed * 0.24 +
    records$repetition_intensity * 0.24 +
    records$social_proof_pressure * 0.24 +
    records$monetization_pressure * 0.16 +
    records$context_loss * 0.12
)

records$ai_narrative_risk <- pmin(
  1,
  records$synthetic_evidence * 0.20 +
    records$provenance_opacity * 0.20 +
    records$fabricated_patterning * 0.18 +
    records$automated_consensus * 0.16 +
    records$vulnerability_targeting * 0.14 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$narrative_risk * 0.24 +
    records$ai_narrative_risk * 0.18 +
    records$platform_amplification_risk * 0.16 +
    (1 - records$evidence_integrity) * 0.16 +
    records$trust_repair_priority * 0.14 +
    records$public_consequence * 0.12
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "narrative_risk_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "narrative_risk_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "narrative_risk_scores.png"), width = 1200, height = 700)
barplot(records$narrative_risk, names.arg = records$item, las = 2, ylab = "Narrative risk", main = "Narrative Risk")
grid()
dev.off()

png(file.path(figures_dir, "evidence_integrity_scores.png"), width = 1200, height = 700)
barplot(records$evidence_integrity, names.arg = records$item, las = 2, ylab = "Evidence integrity", main = "Evidence Integrity")
grid()
dev.off()

print(records[, c(
  "item",
  "narrative_context",
  "narrative_risk",
  "evidence_integrity",
  "trust_repair_priority",
  "ai_narrative_risk",
  "review_priority"
)])
