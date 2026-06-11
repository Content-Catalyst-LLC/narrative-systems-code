# Base R workflow for Storytelling in Religion, Politics, and Public Life.

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

records <- read.csv(file.path(article_root, "data", "public_story_governance_claims.csv"), stringsAsFactors = FALSE)

records$public_narrative_strength <- rowMeans(records[, c(
  "self_story_evidence",
  "shared_value_clarity",
  "now_challenge_clarity",
  "agency",
  "hope",
  "responsibility"
)])

records$mythic_simplification_risk <- pmin(
  1,
  records$enemy_simplification * 0.18 +
    records$boundary_hardening * 0.18 +
    records$crisis_compression * 0.17 +
    records$urgency_pressure * 0.16 +
    records$scapegoat_intensity * 0.17 +
    (1 - records$evidence_visibility) * 0.14
)

records$civil_religion_accountability <- rowMeans(records[, c(
  "memory_plurality",
  "historical_truthfulness",
  "public_limit_clarity",
  "dissent_space",
  "repair_justice",
  "anti_idolatry_critique"
)])

records$testimony_ethics <- rowMeans(records[, c(
  "witness_care",
  "testimony_context",
  "harm_visibility",
  "extraction_resistance",
  "responsibility",
  "repair_justice"
)])

records$ai_public_rhetoric_risk <- pmin(
  1,
  records$formulaic_default * 0.18 +
    records$outrage_intensity * 0.18 +
    records$resolution_smoothing * 0.16 +
    records$identity_boundary_pressure * 0.18 +
    records$context_missingness * 0.16 +
    (1 - records$human_governance) * 0.14
)

records$governance_priority_score <- pmin(
  1,
  records$mythic_simplification_risk * 0.30 +
    records$ai_public_rhetoric_risk * 0.24 +
    (1 - records$civil_religion_accountability) * 0.14 +
    (1 - records$testimony_ethics) * 0.12 +
    records$public_consequence * 0.20
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "public_story_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "public_story_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "public_narrative_strength_scores.png"), width = 1200, height = 700)
barplot(records$public_narrative_strength, names.arg = records$item, las = 2, ylab = "Public narrative strength", main = "Public Narrative Strength")
grid()
dev.off()

png(file.path(figures_dir, "mythic_simplification_risk_scores.png"), width = 1200, height = 700)
barplot(records$mythic_simplification_risk, names.arg = records$item, las = 2, ylab = "Mythic simplification risk", main = "Mythic Simplification Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "public_narrative_strength",
  "mythic_simplification_risk",
  "civil_religion_accountability",
  "ai_public_rhetoric_risk",
  "review_priority"
)])
