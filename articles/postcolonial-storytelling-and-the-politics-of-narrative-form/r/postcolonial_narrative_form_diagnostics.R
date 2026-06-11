# Base R workflow for Postcolonial Storytelling and the Politics of Narrative Form.

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

records <- read.csv(file.path(article_root, "data", "postcolonial_narrative_form_claims.csv"), stringsAsFactors = FALSE)

records$colonial_form_risk <- pmin(
  1,
  records$archive_dominance * 0.18 +
    records$language_hierarchy * 0.18 +
    records$gaze_centrality * 0.18 +
    records$template_forcing * 0.18 +
    records$extraction_anxiety * 0.16 +
    (1 - records$opacity_protection) * 0.12
)

records$postcolonial_form_strength <- rowMeans(records[, c(
  "voice_complexity",
  "language_politics",
  "memory_fragmentation",
  "archive_critique",
  "temporal_multiplicity",
  "spatial_politics",
  "relational_land_context"
)])

records$translation_governance <- rowMeans(records[, c(
  "cultural_specificity",
  "local_authority",
  "opacity_notes",
  "untranslated_terms",
  "reviewer_visibility",
  "harm_review"
)])

records$digital_coloniality <- pmin(
  1,
  records$english_dominance * 0.18 +
    records$stereotype_bias * 0.18 +
    records$extraction_risk * 0.18 +
    records$archive_flattening * 0.16 +
    records$visual_orientalism * 0.16 +
    (1 - records$community_governance) * 0.14
)

records$governance_priority_score <- pmin(
  1,
  records$colonial_form_risk * 0.30 +
    records$digital_coloniality * 0.24 +
    (1 - records$translation_governance) * 0.18 +
    records$public_consequence * 0.18 +
    (1 - records$postcolonial_form_strength) * 0.10
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "postcolonial_narrative_form_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "postcolonial_narrative_form_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "colonial_form_risk_scores.png"), width = 1200, height = 700)
barplot(records$colonial_form_risk, names.arg = records$item, las = 2, ylab = "Colonial-form risk", main = "Colonial-Form Risk")
grid()
dev.off()

png(file.path(figures_dir, "postcolonial_form_strength_scores.png"), width = 1200, height = 700)
barplot(records$postcolonial_form_strength, names.arg = records$item, las = 2, ylab = "Postcolonial-form strength", main = "Postcolonial Narrative Form Strength")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "colonial_form_risk",
  "postcolonial_form_strength",
  "translation_governance",
  "digital_coloniality",
  "review_priority"
)])
