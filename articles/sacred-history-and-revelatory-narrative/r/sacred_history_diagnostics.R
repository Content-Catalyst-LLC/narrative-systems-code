# Base R workflow for Sacred History and Revelatory Narrative.

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

records <- read.csv(file.path(article_root, "data", "sacred_history_claims.csv"), stringsAsFactors = FALSE)
records$revelatory_claim_strength <- rowMeans(records[, c("sacred_disclosure", "event_meaning", "authority_clarity", "obligation", "transformation", "communal_memory")])
records$sacred_history_integration <- rowMeans(records[, c("historical_context", "memory_depth", "ritual_transmission", "interpretive_authority", "ethical_governance", "public_responsibility")])
records$sacred_authority_risk <- pmin(1, records$sacred_certainty * 0.20 + records$omission_risk * 0.18 + records$political_sanctification * 0.18 + records$exclusion_risk * 0.16 + records$historical_flattening * 0.16 + (1 - records$uncertainty_marking) * 0.12)
records$interpretation_readiness <- rowMeans(records[, c("source_context", "authority_notes", "counterexamples", "method_limits", "ethical_governance", "uncertainty_marking")])
records$governance_priority_score <- pmin(1, records$sacred_authority_risk * 0.42 + (1 - records$interpretation_readiness) * 0.28 + records$public_responsibility * 0.16 + (1 - records$sacred_history_integration) * 0.14)
records$review_priority <- ifelse(records$status == "revise" | records$governance_priority_score >= 0.62, "high", ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard"))
records <- records[order(records$governance_priority_score, decreasing = TRUE), ]
write.csv(records, file.path(tables_dir, "sacred_history_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "sacred_history_governance_queue.csv"), row.names = FALSE)
png(file.path(figures_dir, "sacred_authority_risk_scores.png"), width = 1200, height = 700)
barplot(records$sacred_authority_risk, names.arg = records$item, las = 2, ylab = "Sacred authority risk", main = "Sacred Authority Risk Scores")
grid()
dev.off()
png(file.path(figures_dir, "revelatory_claim_strength_scores.png"), width = 1200, height = 700)
barplot(records$revelatory_claim_strength, names.arg = records$item, las = 2, ylab = "Revelatory claim strength", main = "Revelatory Claim Strength Scores")
grid()
dev.off()
print(records[, c("item", "claim_context", "revelatory_claim_strength", "sacred_history_integration", "sacred_authority_risk", "interpretation_readiness", "review_priority")])
