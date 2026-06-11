# Base R workflow for The Hero's Journey in Film and Popular Narrative.

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

records <- read.csv(file.path(article_root, "data", "hero_journey_film_governance_claims.csv"), stringsAsFactors = FALSE)

records$heroic_arc_integrity <- rowMeans(records[, c(
  "call_authenticity",
  "threshold_significance",
  "ordeal_relevance",
  "value_change",
  "return_boon",
  "ethical_consequence"
)])

records$formula_risk <- pmin(
  1,
  records$beat_compliance * 0.18 +
    records$generic_mentor * 0.16 +
    records$mechanical_call * 0.18 +
    records$ordeal_spectacle * 0.16 +
    records$forced_return * 0.16 +
    (1 - records$story_particularity) * 0.16
)

records$cinematic_transformation <- rowMeans(records[, c(
  "visual_motif",
  "sound_design",
  "editing_rhythm",
  "performance_shift",
  "blocking_change",
  "mise_en_scene"
)])

records$culture_gender_integrity <- rowMeans(records[, c(
  "collective_agency",
  "cultural_specificity",
  "gender_complexity",
  "nonheroic_alternatives",
  "story_particularity",
  "ethical_consequence"
)])

records$ai_hero_template_risk <- pmin(
  1,
  records$stage_compliance * 0.18 +
    records$cultural_loss * 0.20 +
    records$genre_cliche * 0.18 +
    records$universalist_pressure * 0.16 +
    records$trope_recycling * 0.16 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$formula_risk * 0.24 +
    records$ai_hero_template_risk * 0.20 +
    (1 - records$heroic_arc_integrity) * 0.16 +
    (1 - records$cinematic_transformation) * 0.12 +
    (1 - records$culture_gender_integrity) * 0.14 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "hero_journey_film_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "hero_journey_film_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "heroic_arc_integrity_scores.png"), width = 1200, height = 700)
barplot(records$heroic_arc_integrity, names.arg = records$item, las = 2, ylab = "Heroic arc integrity", main = "Heroic Arc Integrity")
grid()
dev.off()

png(file.path(figures_dir, "formula_risk_scores.png"), width = 1200, height = 700)
barplot(records$formula_risk, names.arg = records$item, las = 2, ylab = "Formula risk", main = "Hero Journey Formula Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "film_context",
  "heroic_arc_integrity",
  "formula_risk",
  "cinematic_transformation",
  "ai_hero_template_risk",
  "review_priority"
)])
