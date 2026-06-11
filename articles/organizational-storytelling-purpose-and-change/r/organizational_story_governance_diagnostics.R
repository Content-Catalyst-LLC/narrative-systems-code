# Base R workflow for Organizational Storytelling, Purpose, and Change.

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

records <- read.csv(file.path(article_root, "data", "organizational_story_governance_claims.csv"), stringsAsFactors = FALSE)

records$purpose_alignment <- rowMeans(records[, c(
  "mission_clarity",
  "decision_alignment",
  "budget_fit",
  "stakeholder_impact",
  "employee_experience",
  "governance_transparency"
)])

records$change_credibility <- rowMeans(records[, c(
  "evidence_visibility",
  "participation_integrity",
  "resource_support",
  "loss_acknowledgment",
  "feedback_loops",
  "accountability_measures"
)])

records$narrative_extraction_risk <- pmin(
  1,
  records$consent_deficit * 0.18 +
    records$selection_bias * 0.16 +
    records$power_asymmetry * 0.18 +
    records$emotional_targeting * 0.16 +
    records$brand_repurposing * 0.16 +
    (1 - records$agency) * 0.16
)

records$employee_voice_integrity <- rowMeans(records[, c(
  "employee_experience",
  "employee_voice_protection",
  "dissent_visibility",
  "feedback_loops",
  "learning_followthrough",
  "governance_transparency"
)])

records$organizational_memory_strength <- rowMeans(records[, c(
  "memory_preservation",
  "learning_followthrough",
  "evidence_visibility",
  "feedback_loops",
  "dissent_visibility",
  "accountability_measures"
)])

records$ai_organizational_story_risk <- pmin(
  1,
  records$summary_dependence * 0.18 +
    records$omitted_dissent * 0.20 +
    records$context_loss * 0.18 +
    records$privacy_risk * 0.16 +
    records$uncertainty_erasure * 0.16 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$narrative_extraction_risk * 0.22 +
    records$ai_organizational_story_risk * 0.20 +
    (1 - records$purpose_alignment) * 0.16 +
    (1 - records$change_credibility) * 0.14 +
    (1 - records$employee_voice_integrity) * 0.12 +
    (1 - records$organizational_memory_strength) * 0.06 +
    records$public_consequence * 0.10
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "organizational_story_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "organizational_story_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "purpose_alignment_scores.png"), width = 1200, height = 700)
barplot(records$purpose_alignment, names.arg = records$item, las = 2, ylab = "Purpose alignment", main = "Purpose-Practice Alignment")
grid()
dev.off()

png(file.path(figures_dir, "change_credibility_scores.png"), width = 1200, height = 700)
barplot(records$change_credibility, names.arg = records$item, las = 2, ylab = "Change credibility", main = "Change Story Credibility")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "purpose_alignment",
  "change_credibility",
  "narrative_extraction_risk",
  "ai_organizational_story_risk",
  "review_priority"
)])
