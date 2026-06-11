# myth_ritual_symbolic_diagnostics.R
# Base R workflow for myth, ritual, and symbolic story analysis.

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

items <- read.csv(file.path(article_root, "data", "myth_ritual_symbolic_items.csv"), stringsAsFactors = FALSE)

items$symbolic_function <- rowMeans(items[, c(
  "origin_function",
  "cosmological_order",
  "memory_function",
  "identity_function",
  "transition_function",
  "authority_function"
)])

items$ritual_context <- rowMeans(items[, c(
  "sequence_clarity",
  "place_linkage",
  "gesture_documentation",
  "object_symbolism",
  "participant_role",
  "protocol_transparency"
)])

items$ethical_risk <- pmin(
  1,
  items$totalizing_order * 0.18 +
    items$scapegoating_risk * 0.20 +
    items$exclusion_risk * 0.18 +
    items$appropriation_risk * 0.18 +
    items$harm_exposure * 0.16 +
    (1 - items$governance_control) * 0.10
)

items$interpretation_readiness <- rowMeans(items[, c(
  "context_explanation",
  "ritual_verification",
  "language_notes",
  "access_control",
  "governance_oversight",
  "uncertainty_marking"
)])

items$governance_priority_score <- pmin(
  1,
  items$ethical_risk * 0.35 +
    items$community_sensitivity * 0.25 +
    items$public_consequence * 0.20 +
    (1 - items$interpretation_readiness) * 0.20
)

items$review_priority <- ifelse(
  items$status == "revise" | items$ethical_risk >= 0.55 | items$governance_priority_score >= 0.62 | items$interpretation_readiness < 0.55,
  "high",
  ifelse(
    items$status == "review" | items$ethical_risk >= 0.40 | items$governance_priority_score >= 0.48 | items$interpretation_readiness < 0.68,
    "medium",
    "standard"
  )
)

items <- items[order(items$ethical_risk, decreasing = TRUE), ]

write.csv(
  items,
  file.path(tables_dir, "myth_ritual_symbolic_diagnostics.csv"),
  row.names = FALSE
)

governance_queue <- items[items$review_priority != "standard", ]

write.csv(
  governance_queue,
  file.path(tables_dir, "myth_ritual_symbolic_governance_queue.csv"),
  row.names = FALSE
)

png(file.path(figures_dir, "symbolic_function_scores.png"), width = 1200, height = 700)
barplot(
  items$symbolic_function,
  names.arg = items$item,
  las = 2,
  ylab = "Symbolic function",
  main = "Myth and Ritual Symbolic Function Scores"
)
grid()
dev.off()

png(file.path(figures_dir, "ethical_risk_scores.png"), width = 1200, height = 700)
barplot(
  items$ethical_risk,
  names.arg = items$item,
  las = 2,
  ylab = "Ethical risk",
  main = "Myth and Ritual Ethical Risk Scores"
)
grid()
dev.off()

print(items[, c(
  "item",
  "symbolic_context",
  "symbolic_function",
  "ritual_context",
  "ethical_risk",
  "interpretation_readiness",
  "governance_priority_score",
  "review_priority"
)])
