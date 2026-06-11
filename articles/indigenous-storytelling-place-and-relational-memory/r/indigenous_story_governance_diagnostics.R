# Base R workflow for Indigenous Storytelling, Place, and Relational Memory.

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

records <- read.csv(file.path(article_root, "data", "indigenous_story_governance_claims.csv"), stringsAsFactors = FALSE)

records$relational_accountability <- rowMeans(records[, c(
  "place_specificity",
  "community_authority",
  "teller_relationship",
  "listener_context",
  "obligation_visibility",
  "governance_visibility"
)])

records$protocol_risk <- pmin(
  1,
  records$access_pressure * 0.18 +
    records$seasonal_restriction * 0.16 +
    records$ceremonial_restriction * 0.18 +
    records$template_forcing * 0.16 +
    records$digital_exposure * 0.16 +
    (1 - records$governance_visibility) * 0.16
)

records$place_memory_strength <- rowMeans(records[, c(
  "land_naming",
  "ecological_knowledge",
  "ancestral_memory",
  "route_teaching",
  "seasonal_context",
  "future_generation_responsibility"
)])

records$translation_governance <- rowMeans(records[, c(
  "cultural_specificity",
  "language_context",
  "opacity_notes",
  "untranslated_terms",
  "reviewer_visibility",
  "harm_review"
)])

records$digital_sovereignty_risk <- pmin(
  1,
  records$extraction_risk * 0.18 +
    records$open_access_assumption * 0.18 +
    records$ai_training_risk * 0.20 +
    records$stereotype_bias * 0.16 +
    records$metadata_flattening * 0.14 +
    (1 - records$community_governance) * 0.14
)

records$governance_priority_score <- pmin(
  1,
  records$protocol_risk * 0.28 +
    records$digital_sovereignty_risk * 0.28 +
    (1 - records$relational_accountability) * 0.16 +
    (1 - records$translation_governance) * 0.12 +
    records$public_consequence * 0.16
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "indigenous_story_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "indigenous_story_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "relational_accountability_scores.png"), width = 1200, height = 700)
barplot(records$relational_accountability, names.arg = records$item, las = 2, ylab = "Relational accountability", main = "Indigenous Story Relational Accountability")
grid()
dev.off()

png(file.path(figures_dir, "digital_sovereignty_risk_scores.png"), width = 1200, height = 700)
barplot(records$digital_sovereignty_risk, names.arg = records$item, las = 2, ylab = "Digital sovereignty risk", main = "Digital Sovereignty Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "relational_accountability",
  "protocol_risk",
  "place_memory_strength",
  "digital_sovereignty_risk",
  "review_priority"
)])
