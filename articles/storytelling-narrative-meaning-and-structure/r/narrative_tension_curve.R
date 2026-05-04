# Storytelling: Narrative Tension Curve in R
# Educational example only.

library(tidyverse)

arc <- read_csv("../data/story_arc.csv", show_col_types = FALSE)

arc_long <- arc |>
  pivot_longer(
    cols = c(
      tension,
      conflict_intensity,
      transformation_pressure,
      resolution_pressure
    ),
    names_to = "dimension",
    values_to = "value"
  )

peak_moments <- arc_long |>
  group_by(dimension) |>
  slice_max(value, n = 1, with_ties = FALSE) |>
  ungroup()

dir.create("../outputs", showWarnings = FALSE, recursive = TRUE)

write_csv(arc, "../outputs/r_story_arc.csv")
write_csv(arc_long, "../outputs/r_story_arc_long.csv")
write_csv(peak_moments, "../outputs/r_story_arc_peak_moments.csv")

print(arc)
print(peak_moments)
