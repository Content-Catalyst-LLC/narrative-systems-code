# Base R workflow for Adaptation and the Migration of Stories Across Media.

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

records <- read.csv(file.path(article_root, "data", "adaptation_governance_claims.csv"), stringsAsFactors = FALSE)

records$adaptation_integrity <- rowMeans(records[, c(
  "source_core_preservation",
  "medium_fit",
  "transformation_purpose",
  "context_preservation",
  "reception_value",
  "ethical_governance"
)])

records$transfer_loss <- pmin(
  1,
  records$voice_loss * 0.18 +
    records$interiority_loss * 0.16 +
    records$context_loss * 0.20 +
    records$provenance_loss * 0.18 +
    records$agency_loss * 0.16 +
    (1 - records$governance_review) * 0.12
)

records$franchise_drift <- pmin(
  1,
  records$repetition_compliance * 0.18 +
    records$lore_excess * 0.18 +
    records$nostalgia_reliance * 0.16 +
    records$continuity_saturation * 0.16 +
    records$market_overextension * 0.16 +
    (1 - records$story_purpose) * 0.16
)

records$ai_adaptation_risk <- pmin(
  1,
  records$plot_summary_dependence * 0.18 +
    records$voice_style_imitation * 0.20 +
    records$context_loss * 0.18 +
    records$synthetic_opacity * 0.16 +
    records$uncertainty_erasure * 0.16 +
    (1 - records$human_review) * 0.12
)

records$consent_and_context_strength <- rowMeans(cbind(
  records$consent_clarity,
  records$source_authority,
  records$cultural_context,
  records$context_preservation,
  1 - records$provenance_loss,
  records$governance_review
))

records$governance_priority_score <- pmin(
  1,
  records$transfer_loss * 0.22 +
    records$franchise_drift * 0.16 +
    records$ai_adaptation_risk * 0.20 +
    (1 - records$adaptation_integrity) * 0.16 +
    (1 - records$consent_and_context_strength) * 0.12 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "adaptation_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "adaptation_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "adaptation_integrity_scores.png"), width = 1200, height = 700)
barplot(records$adaptation_integrity, names.arg = records$item, las = 2, ylab = "Adaptation integrity", main = "Adaptation Integrity")
grid()
dev.off()

png(file.path(figures_dir, "transfer_loss_scores.png"), width = 1200, height = 700)
barplot(records$transfer_loss, names.arg = records$item, las = 2, ylab = "Transfer loss", main = "Adaptation Transfer Loss")
grid()
dev.off()

print(records[, c(
  "item",
  "adaptation_context",
  "adaptation_integrity",
  "transfer_loss",
  "franchise_drift",
  "ai_adaptation_risk",
  "review_priority"
)])
