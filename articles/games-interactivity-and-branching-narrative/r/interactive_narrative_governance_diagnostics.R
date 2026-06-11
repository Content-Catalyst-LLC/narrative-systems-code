# Base R workflow for Games, Interactivity, and Branching Narrative.

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

records <- read.csv(file.path(article_root, "data", "interactive_narrative_governance_claims.csv"), stringsAsFactors = FALSE)

records$agency_integrity <- rowMeans(records[, c(
  "choice_meaningfulness",
  "system_response",
  "feedback_clarity",
  "role_variation",
  "world_memory",
  "ethical_governance"
)])

records$branching_burden <- pmin(
  1,
  records$branch_count_pressure * 0.16 +
    records$state_dependency * 0.18 +
    records$consequence_tracking * 0.20 +
    records$testing_load * 0.18 +
    records$localization_cost * 0.12 +
    (1 - records$recombination_coherence) * 0.16
)

records$system_story_alignment <- rowMeans(records[, c(
  "mechanic_theme_fit",
  "rule_fiction_fit",
  "goal_value_fit",
  "progression_coherence",
  "interface_legibility",
  "consequence_consistency"
)])

records$failure_and_identity_strength <- rowMeans(records[, c(
  "failure_meaning",
  "replay_value",
  "player_consent",
  "identity_care",
  "feedback_clarity",
  "ethical_governance"
)])

records$ai_interactive_narrative_risk <- pmin(
  1,
  records$generic_quest_generation * 0.18 +
    records$character_memory_failure * 0.20 +
    records$opaque_system_response * 0.18 +
    records$player_manipulation * 0.18 +
    records$harmful_stereotype_risk * 0.14 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$branching_burden * 0.18 +
    records$ai_interactive_narrative_risk * 0.22 +
    (1 - records$agency_integrity) * 0.18 +
    (1 - records$system_story_alignment) * 0.18 +
    (1 - records$failure_and_identity_strength) * 0.10 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "interactive_narrative_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "interactive_narrative_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "agency_integrity_scores.png"), width = 1200, height = 700)
barplot(records$agency_integrity, names.arg = records$item, las = 2, ylab = "Agency integrity", main = "Agency Integrity")
grid()
dev.off()

png(file.path(figures_dir, "branching_burden_scores.png"), width = 1200, height = 700)
barplot(records$branching_burden, names.arg = records$item, las = 2, ylab = "Branching burden", main = "Branching Burden")
grid()
dev.off()

print(records[, c(
  "item",
  "game_context",
  "agency_integrity",
  "branching_burden",
  "system_story_alignment",
  "ai_interactive_narrative_risk",
  "review_priority"
)])
