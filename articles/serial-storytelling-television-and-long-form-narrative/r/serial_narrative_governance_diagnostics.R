# Base R workflow for Serial Storytelling, Television, and Long-Form Narrative.

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

records <- read.csv(file.path(article_root, "data", "serial_narrative_governance_claims.csv"), stringsAsFactors = FALSE)

records$season_coherence <- rowMeans(records[, c(
  "episode_function",
  "arc_progression",
  "thematic_development",
  "character_memory",
  "payoff_integrity_signal",
  "finale_consequence"
)])

records$continuity_burden <- pmin(
  1,
  records$unresolved_arcs * 0.20 +
    records$lore_density * 0.16 +
    records$memory_expectation * 0.18 +
    records$recap_uncertainty * 0.14 +
    records$continuity_saturation * 0.18 +
    (1 - records$audience_accessibility) * 0.14
)

records$payoff_integrity <- rowMeans(records[, c(
  "foreshadowing_support",
  "character_relevance",
  "emotional_payoff",
  "mystery_logic",
  "retrospective_coherence",
  "thematic_alignment"
)])

records$ensemble_and_ethics_strength <- rowMeans(records[, c(
  "ensemble_balance",
  "representation_depth",
  "trauma_care",
  "audience_trust",
  "character_memory",
  "finale_consequence"
)])

records$ai_serial_risk <- pmin(
  1,
  records$generic_plotting * 0.18 +
    records$continuity_fabrication * 0.20 +
    records$memory_erasure * 0.18 +
    records$payoff_simplification * 0.16 +
    records$franchise_overextension * 0.16 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$continuity_burden * 0.20 +
    records$ai_serial_risk * 0.20 +
    (1 - records$season_coherence) * 0.16 +
    (1 - records$payoff_integrity) * 0.18 +
    (1 - records$ensemble_and_ethics_strength) * 0.12 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "serial_narrative_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "serial_narrative_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "season_coherence_scores.png"), width = 1200, height = 700)
barplot(records$season_coherence, names.arg = records$item, las = 2, ylab = "Season coherence", main = "Season Coherence")
grid()
dev.off()

png(file.path(figures_dir, "continuity_burden_scores.png"), width = 1200, height = 700)
barplot(records$continuity_burden, names.arg = records$item, las = 2, ylab = "Continuity burden", main = "Continuity Burden")
grid()
dev.off()

print(records[, c(
  "item",
  "serial_context",
  "season_coherence",
  "continuity_burden",
  "payoff_integrity",
  "ai_serial_risk",
  "review_priority"
)])
