# Base R workflow for Creation, Flood, Exile, and Return as Narrative Patterns.

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

records <- read.csv(file.path(article_root, "data", "narrative_pattern_claims.csv"), stringsAsFactors = FALSE)

records$pattern_strength <- rowMeans(records[, c(
  "creation_signal",
  "flood_signal",
  "exile_signal",
  "return_signal"
)])

records$rupture_renewal_strength <- rowMeans(records[, c(
  "flood_signal",
  "exile_signal",
  "memory_maintenance",
  "repair_responsibility"
)])

records$interpretation_readiness <- rowMeans(records[, c(
  "source_context",
  "historical_context",
  "counterexamples",
  "method_limits",
  "ethics_governance",
  "uncertainty_notes"
)])

records$ethical_risk <- pmin(
  1,
  records$origin_nostalgia * 0.18 +
    records$cleansing_fantasy * 0.20 +
    records$exile_romanticization * 0.18 +
    records$false_return * 0.18 +
    records$power_blindness * 0.16 +
    (1 - records$uncertainty_notes) * 0.10
)

records$governance_priority_score <- pmin(
  1,
  records$ethical_risk * 0.40 +
    (1 - records$interpretation_readiness) * 0.28 +
    records$public_consequence * 0.17 +
    (1 - records$repair_responsibility) * 0.15
)

records$review_priority <- ifelse(
  records$status == "revise" | records$governance_priority_score >= 0.62,
  "high",
  ifelse(
    records$status == "review" | records$governance_priority_score >= 0.45,
    "medium",
    "standard"
  )
)

records <- records[order(records$governance_priority_score, decreasing = TRUE), ]

write.csv(records, file.path(tables_dir, "creation_flood_exile_return_diagnostics.csv"), row.names = FALSE)
write.csv(records[records$review_priority != "standard", ], file.path(tables_dir, "creation_flood_exile_return_governance_queue.csv"), row.names = FALSE)

png(file.path(figures_dir, "pattern_strength_scores.png"), width = 1200, height = 700)
barplot(
  records$pattern_strength,
  names.arg = records$item,
  las = 2,
  ylab = "Pattern strength",
  main = "Creation, Flood, Exile, and Return Pattern Strength"
)
grid()
dev.off()

png(file.path(figures_dir, "ethical_risk_scores.png"), width = 1200, height = 700)
barplot(
  records$ethical_risk,
  names.arg = records$item,
  las = 2,
  ylab = "Ethical risk",
  main = "Pattern Analysis Ethical Risk"
)
grid()
dev.off()

print(records[, c(
  "item",
  "claim_context",
  "pattern_strength",
  "rupture_renewal_strength",
  "ethical_risk",
  "interpretation_readiness",
  "review_priority"
)])
