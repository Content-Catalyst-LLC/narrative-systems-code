# Base R workflow for Storytelling in Comparative Perspective.

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

records <- read.csv(file.path(article_root, "data", "comparative_story_governance_claims.csv"), stringsAsFactors = FALSE)

records$comparative_integrity <- rowMeans(records[, c(
  "source_context",
  "difference_preservation",
  "evidence_quality",
  "translation_reliability",
  "protocol_compliance",
  "human_review"
)])

records$flattening_risk <- pmin(
  1,
  records$universalism_claims * 0.18 +
    records$template_capture * 0.18 +
    records$context_loss * 0.18 +
    records$archive_bias * 0.16 +
    records$power_imbalance * 0.16 +
    (1 - records$difference_preservation) * 0.14
)

records$transmission_uncertainty <- pmin(
  1,
  records$language_gap * 0.18 +
    records$media_shift * 0.16 +
    records$archive_gap * 0.18 +
    records$performance_loss * 0.18 +
    records$restricted_source_concern * 0.14 +
    (1 - records$version_documentation) * 0.16
)

records$contextual_grounding <- rowMeans(records[, c(
  "local_interpretation",
  "community_review",
  "attribution_quality",
  "corpus_balance",
  "source_context",
  "protocol_compliance"
)])

records$ai_comparative_risk <- pmin(
  1,
  records$biased_corpus * 0.18 +
    records$hallucinated_source_risk * 0.18 +
    records$ai_translation_loss * 0.18 +
    records$sacred_material_risk * 0.18 +
    records$overgeneralized_claims * 0.16 +
    (1 - records$expert_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$flattening_risk * 0.22 +
    records$transmission_uncertainty * 0.16 +
    records$ai_comparative_risk * 0.20 +
    (1 - records$comparative_integrity) * 0.16 +
    (1 - records$contextual_grounding) * 0.12 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "comparative_story_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "comparative_story_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "comparative_integrity_scores.png"), width = 1200, height = 700)
barplot(records$comparative_integrity, names.arg = records$item, las = 2, ylab = "Comparative integrity", main = "Comparative Integrity")
grid()
dev.off()

png(file.path(figures_dir, "flattening_risk_scores.png"), width = 1200, height = 700)
barplot(records$flattening_risk, names.arg = records$item, las = 2, ylab = "Flattening risk", main = "Flattening Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "comparison_context",
  "comparative_integrity",
  "flattening_risk",
  "transmission_uncertainty",
  "ai_comparative_risk",
  "review_priority"
)])
