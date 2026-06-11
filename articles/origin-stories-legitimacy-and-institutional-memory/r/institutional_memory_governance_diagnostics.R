# Base R workflow for Origin Stories, Legitimacy, and Institutional Memory.

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

records <- read.csv(file.path(article_root, "data", "institutional_memory_governance_claims.csv"), stringsAsFactors = FALSE)

records$legitimacy_alignment <- rowMeans(records[, c(
  "purpose_clarity",
  "mission_action_alignment",
  "record_evidence",
  "affected_community_testimony",
  "conduct_visibility",
  "governance_openness"
)])

records$origin_myth_risk <- pmin(
  1,
  records$founder_heroization * 0.18 +
    records$exclusion_omission * 0.18 +
    records$harm_removal * 0.18 +
    records$commemoration_saturation * 0.14 +
    records$reputational_branding * 0.16 +
    (1 - records$voice_multiplicity) * 0.16
)

records$institutional_memory_strength <- rowMeans(records[, c(
  "record_preservation",
  "archive_completeness",
  "metadata_quality",
  "testimony_stewardship",
  "knowledge_retention",
  "public_access"
)])

records$reform_credibility <- rowMeans(records[, c(
  "harm_naming",
  "structural_change",
  "evidence_release",
  "material_repair",
  "oversight",
  "transparent_progress"
)])

records$ai_memory_distortion_risk <- pmin(
  1,
  records$ai_summary_dependence * 0.24 +
    records$archive_bias_risk * 0.24 +
    records$context_loss * 0.22 +
    (1 - records$correction_pathway) * 0.16 +
    (1 - records$public_access) * 0.14
)

records$governance_priority_score <- pmin(
  1,
  records$origin_myth_risk * 0.30 +
    records$ai_memory_distortion_risk * 0.18 +
    (1 - records$legitimacy_alignment) * 0.18 +
    (1 - records$institutional_memory_strength) * 0.14 +
    (1 - records$reform_credibility) * 0.10 +
    records$public_consequence * 0.10
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "institutional_memory_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "institutional_memory_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "legitimacy_alignment_scores.png"), width = 1200, height = 700)
barplot(records$legitimacy_alignment, names.arg = records$item, las = 2, ylab = "Legitimacy alignment", main = "Legitimacy Alignment")
grid()
dev.off()

png(file.path(figures_dir, "origin_myth_risk_scores.png"), width = 1200, height = 700)
barplot(records$origin_myth_risk, names.arg = records$item, las = 2, ylab = "Origin myth risk", main = "Origin Myth Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "legitimacy_alignment",
  "origin_myth_risk",
  "institutional_memory_strength",
  "reform_credibility",
  "review_priority"
)])
