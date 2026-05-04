# Storytelling: Story Metadata Summary in R
# Educational example only.

library(tidyverse)

characters <- read_csv("../data/characters.csv", show_col_types = FALSE)
motifs <- read_csv("../data/motifs.csv", show_col_types = FALSE)

characters <- characters |>
  mutate(transformation_score = final_state - initial_state) |>
  arrange(desc(transformation_score))

motifs <- motifs |>
  mutate(relative_frequency = frequency / sum(frequency)) |>
  arrange(desc(frequency))

dir.create("../outputs", showWarnings = FALSE, recursive = TRUE)

write_csv(characters, "../outputs/r_character_arcs.csv")
write_csv(motifs, "../outputs/r_motif_inventory.csv")

print(characters)
print(motifs)
