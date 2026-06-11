# Base R workflow for Storytelling Across Oral, Literary, and Visual Media.

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

records <- read.csv(file.path(article_root, "data", "cross_media_story_governance_claims.csv"), stringsAsFactors = FALSE)

records$medium_affordance_fit <- rowMeans(records[, c(
  "embodiment",
  "interior_depth",
  "spatial_quality",
  "temporal_control",
  "audience_relation",
  "contextual_fit"
)])

records$media_transfer_risk <- pmin(
  1,
  records$voice_loss * 0.18 +
    records$context_loss * 0.20 +
    records$provenance_loss * 0.18 +
    records$audience_shift * 0.14 +
    records$representational_distortion * 0.18 +
    (1 - records$governance_review) * 0.12
)

records$multimodal_coherence <- rowMeans(records[, c(
  "text_image_integration",
  "image_sequence_logic",
  "sound_design_alignment",
  "rhythm_harmony",
  "provenance_visibility",
  "uncertainty_notation"
)])

records$consent_and_context_strength <- rowMeans(records[, c(
  "consent_clarity",
  "source_authority",
  "cultural_context",
  "reuse_boundaries",
  "provenance_visibility",
  "governance_review"
)])

records$ai_cross_media_risk <- pmin(
  1,
  records$synthetic_documentary_ambiguity * 0.20 +
    records$context_loss * 0.18 +
    records$provenance_opacity * 0.18 +
    records$voice_likeness_imitation * 0.16 +
    records$bias_reproduction * 0.16 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$media_transfer_risk * 0.24 +
    records$ai_cross_media_risk * 0.22 +
    (1 - records$medium_affordance_fit) * 0.14 +
    (1 - records$multimodal_coherence) * 0.14 +
    (1 - records$consent_and_context_strength) * 0.12 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "cross_media_story_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "cross_media_story_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "medium_affordance_fit_scores.png"), width = 1200, height = 700)
barplot(records$medium_affordance_fit, names.arg = records$item, las = 2, ylab = "Medium affordance fit", main = "Medium Affordance Fit")
grid()
dev.off()

png(file.path(figures_dir, "media_transfer_risk_scores.png"), width = 1200, height = 700)
barplot(records$media_transfer_risk, names.arg = records$item, las = 2, ylab = "Media transfer risk", main = "Media Transfer Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "transfer_context",
  "medium_affordance_fit",
  "media_transfer_risk",
  "multimodal_coherence",
  "ai_cross_media_risk",
  "review_priority"
)])
