# Base R workflow for Digital Storytelling and Platform Culture.

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

records <- read.csv(file.path(article_root, "data", "digital_storytelling_governance_claims.csv"), stringsAsFactors = FALSE)

records$platform_narrative_integrity <- rowMeans(records[, c(
  "context_preservation",
  "source_authority",
  "visibility_provenance_fit",
  "audience_care",
  "medium_format_fit",
  "ethical_governance"
)])

records$context_collapse_risk <- pmin(
  1,
  records$audience_spread * 0.18 +
    records$compression_severity * 0.16 +
    records$hostile_context_exposure * 0.18 +
    records$engagement_intensity * 0.14 +
    records$sensitive_visibility * 0.18 +
    (1 - records$governance_review) * 0.16
)

records$platform_formula_drift <- pmin(
  1,
  records$hook_overdependence * 0.16 +
    records$trend_compliance * 0.16 +
    records$metric_pressure * 0.20 +
    records$retention_framing * 0.16 +
    records$outrage_signaling * 0.16 +
    (1 - records$judgment_stability) * 0.16
)

records$archive_memory_strength <- rowMeans(records[, c(
  "archive_metadata",
  "consent_status",
  "preservation_plan",
  "access_context",
  "context_preservation",
  "source_authority"
)])

records$ai_synthetic_story_risk <- pmin(
  1,
  records$synthetic_opacity * 0.18 +
    records$voice_imitation * 0.18 +
    records$provenance_loss * 0.18 +
    records$ai_context_loss * 0.18 +
    records$manipulation_targeting * 0.16 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$context_collapse_risk * 0.20 +
    records$platform_formula_drift * 0.18 +
    records$ai_synthetic_story_risk * 0.22 +
    (1 - records$platform_narrative_integrity) * 0.16 +
    (1 - records$archive_memory_strength) * 0.10 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "digital_storytelling_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "digital_storytelling_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "platform_narrative_integrity_scores.png"), width = 1200, height = 700)
barplot(records$platform_narrative_integrity, names.arg = records$item, las = 2, ylab = "Platform narrative integrity", main = "Platform Narrative Integrity")
grid()
dev.off()

png(file.path(figures_dir, "context_collapse_risk_scores.png"), width = 1200, height = 700)
barplot(records$context_collapse_risk, names.arg = records$item, las = 2, ylab = "Context-collapse risk", main = "Context-Collapse Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "platform_context",
  "platform_narrative_integrity",
  "context_collapse_risk",
  "platform_formula_drift",
  "ai_synthetic_story_risk",
  "review_priority"
)])
