# Base R workflow for National Narratives and the Politics of Memory.

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

records <- read.csv(file.path(article_root, "data", "national_memory_governance_claims.csv"), stringsAsFactors = FALSE)

records$memory_plurality <- rowMeans(records[, c(
  "group_representation",
  "source_diversity",
  "testimony_visibility",
  "archive_coverage",
  "countermemory_inclusion",
  "dissent_space"
)])

records$national_myth_risk <- pmin(
  1,
  records$hero_compression * 0.17 +
    records$innocence_story * 0.18 +
    records$exclusion_omission * 0.18 +
    records$victimhood_monopoly * 0.15 +
    records$purity_symbolism * 0.14 +
    (1 - records$revision_capacity) * 0.18
)

records$memory_accountability <- rowMeans(records[, c(
  "evidence_visibility",
  "provenance_reliability",
  "record_access",
  "testimony_care",
  "contextual_explanation",
  "repair_linkage"
)])

records$public_memory_infrastructure <- rowMeans(records[, c(
  "curriculum_balance",
  "monument_context",
  "platform_context",
  "archive_coverage",
  "record_access",
  "dissent_space"
)])

records$ai_memory_risk <- pmin(
  1,
  records$summary_dependence * 0.18 +
    records$context_loss * 0.18 +
    records$dominant_archive_bias * 0.18 +
    records$uncertainty_erasure * 0.16 +
    records$omission_of_minority_memory * 0.16 +
    (1 - records$human_review) * 0.14
)

records$governance_priority_score <- pmin(
  1,
  records$national_myth_risk * 0.30 +
    records$ai_memory_risk * 0.20 +
    (1 - records$memory_plurality) * 0.18 +
    (1 - records$memory_accountability) * 0.14 +
    (1 - records$public_memory_infrastructure) * 0.08 +
    records$public_consequence * 0.10
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "national_memory_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "national_memory_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "memory_plurality_scores.png"), width = 1200, height = 700)
barplot(records$memory_plurality, names.arg = records$item, las = 2, ylab = "Memory plurality", main = "National Memory Plurality")
grid()
dev.off()

png(file.path(figures_dir, "national_myth_risk_scores.png"), width = 1200, height = 700)
barplot(records$national_myth_risk, names.arg = records$item, las = 2, ylab = "National myth risk", main = "National Myth Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "memory_plurality",
  "national_myth_risk",
  "memory_accountability",
  "ai_memory_risk",
  "review_priority"
)])
