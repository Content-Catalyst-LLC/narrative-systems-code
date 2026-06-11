# Base R workflow for Storytelling and the Ethics of Representation.

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

records <- read.csv(file.path(article_root, "data", "representation_ethics_governance_claims.csv"), stringsAsFactors = FALSE)

records$representation_integrity <- rowMeans(records[, c(
  "voice_agency",
  "context_preservation",
  "dignity_protection",
  "source_accuracy",
  "provenance_visibility",
  "accountability_capacity"
)])

records$representation_risk <- pmin(
  1,
  records$stereotype_tendency * 0.18 +
    records$exposure_risk * 0.18 +
    records$context_loss * 0.18 +
    records$voice_replacement * 0.16 +
    records$power_asymmetry * 0.16 +
    (1 - records$governance_review) * 0.14
)

records$consent_adequacy <- rowMeans(records[, c(
  "informed_consent",
  "ongoing_consent",
  "use_clarity",
  "platform_circulation_clarity",
  "withdrawal_clarity",
  "reuse_ai_clarity"
)])

records$cultural_and_visual_strength <- rowMeans(records[, c(
  "cultural_protocols",
  "community_review",
  "attribution_quality",
  "image_context",
  "visual_dignity",
  "caption_accuracy"
)])

records$ai_representation_risk <- pmin(
  1,
  records$synthetic_opacity * 0.18 +
    records$likeness_imitation * 0.18 +
    records$cultural_fabrication * 0.20 +
    records$provenance_loss * 0.18 +
    records$evidence_confusion * 0.14 +
    (1 - records$human_review) * 0.12
)

records$governance_priority_score <- pmin(
  1,
  records$representation_risk * 0.22 +
    records$ai_representation_risk * 0.20 +
    (1 - records$representation_integrity) * 0.18 +
    (1 - records$consent_adequacy) * 0.16 +
    (1 - records$cultural_and_visual_strength) * 0.10 +
    records$public_consequence * 0.14
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(records$status == "review" | records$governance_priority_score >= 0.45, "medium", "standard")
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "representation_ethics_governance_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "representation_ethics_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "representation_integrity_scores.png"), width = 1200, height = 700)
barplot(records$representation_integrity, names.arg = records$item, las = 2, ylab = "Representation integrity", main = "Representation Integrity")
grid()
dev.off()

png(file.path(figures_dir, "representation_risk_scores.png"), width = 1200, height = 700)
barplot(records$representation_risk, names.arg = records$item, las = 2, ylab = "Representation risk", main = "Representation Risk")
grid()
dev.off()

print(records[, c(
  "item",
  "representation_context",
  "representation_integrity",
  "representation_risk",
  "consent_adequacy",
  "ai_representation_risk",
  "review_priority"
)])
