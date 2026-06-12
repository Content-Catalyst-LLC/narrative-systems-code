# Base R workflow for Why Storytelling Still Matters.

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

records <- read.csv(file.path(article_root, "data", "storytelling_value_governance_claims.csv"), stringsAsFactors = FALSE)

records$storytelling_value <- rowMeans(records[, c(
  "clarity",
  "evidence_grounding",
  "memory_continuity",
  "audience_reasoning",
  "dignity_protection",
  "public_usefulness"
)])

records$narrative_responsibility <- rowMeans(records[, c(
  "truthfulness",
  "context_adequacy",
  "consent_discipline",
  "uncertainty_disclosure",
  "revision_openness",
  "accountability"
)])

records$misuse_risk <- pmin(
  1,
  records$oversimplification * 0.18 +
    records$emotional_exploitation * 0.18 +
    records$scapegoating * 0.18 +
    records$context_loss * 0.18 +
    records$platform_frictionlessness * 0.14 +
    (1 - records$human_review) * 0.14
)

records$ai_storytelling_governance <- rowMeans(records[, c(
  "provenance_visibility",
  "source_traceability",
  "ai_human_review",
  "ai_consent_discipline",
  "use_limit_clarity",
  "correction_process"
)])

records$governance_priority_score <- pmin(
  1,
  records$misuse_risk * 0.28 +
    (1 - records$narrative_responsibility) * 0.22 +
    (1 - records$storytelling_value) * 0.16 +
    (1 - records$ai_storytelling_governance) * 0.14 +
    records$ethical_stakes * 0.12 +
    (1 - records$cultural_context) * 0.08
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "storytelling_value_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "storytelling_value_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "storytelling_value_scores.png"), width = 1200, height = 700)
barplot(records$storytelling_value, names.arg = records$item, las = 2, ylab = "Storytelling value", main = "Storytelling Value")
grid()
dev.off()

png(file.path(figures_dir, "misuse_risk_scores.png"), width = 1200, height = 700)
barplot(records$misuse_risk, names.arg = records$item, las = 2, ylab = "Misuse risk", main = "Misuse Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "story_context",
  "storytelling_value",
  "narrative_responsibility",
  "misuse_risk",
  "ai_storytelling_governance",
  "review_priority"
)])
