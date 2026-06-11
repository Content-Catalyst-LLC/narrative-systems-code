# compact_oral_forms_diagnostics.R
# Base R workflow for proverb, song, chant, and ritual speech analysis.

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

items <- read.csv(file.path(article_root, "data", "compact_oral_forms_items.csv"), stringsAsFactors = FALSE)

items$oral_form_context <- rowMeans(items[, c(
  "form_identification",
  "speaker_role",
  "audience_documentation",
  "occasion_notes",
  "place_linkage",
  "use_context"
)])

items$sound_and_repetition <- rowMeans(items[, c(
  "rhythm",
  "melody",
  "cadence",
  "refrain_or_formula",
  "participation",
  "embodiment"
)])

items$ritual_authority <- rowMeans(items[, c(
  "role_legitimacy",
  "protocol_review",
  "consent_status",
  "access_control",
  "governance_oversight",
  "benefit_sharing"
)])

items$archive_risk <- pmin(
  1,
  items$quote_extraction_risk * 0.18 +
    items$context_removal * 0.18 +
    items$sound_loss * 0.16 +
    items$translation_loss * 0.16 +
    items$extraction_risk * 0.18 +
    (1 - items$governance_control) * 0.14
)

items$governance_priority_score <- pmin(
  1,
  items$archive_risk * 0.35 +
    items$community_sensitivity * 0.25 +
    items$public_consequence * 0.20 +
    (1 - items$ritual_authority) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$archive_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$ritual_authority < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$archive_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$ritual_authority < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$archive_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "compact_oral_forms_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "compact_oral_forms_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "oral_form_context_scores.png"), width = 1200, height = 700)
barplot(
  items$oral_form_context,
  names.arg = items$item,
  las = 2,
  ylab = "Oral-form context",
  main = "Compact Oral Form Context Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "ritual_authority_scores.png"), width = 1200, height = 700)
barplot(
  items$ritual_authority,
  names.arg = items$item,
  las = 2,
  ylab = "Ritual authority",
  main = "Ritual Authority and Access Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "oral_form",
  "oral_form_context",
  "sound_and_repetition",
  "ritual_authority",
  "archive_risk",
  "governance_priority_score",
  "review_priority"
)])
