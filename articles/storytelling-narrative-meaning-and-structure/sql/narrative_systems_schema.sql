-- Narrative Systems SQL schema
-- Educational schema for stories, events, characters, motifs, conflicts, turning points, themes, media forms, and ethical cautions.

CREATE TABLE IF NOT EXISTS stories (
    story_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    tradition_or_medium TEXT NOT NULL,
    description TEXT NOT NULL,
    cultural_context TEXT,
    ethical_caution TEXT
);

CREATE TABLE IF NOT EXISTS narrative_events (
    event_id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL,
    event_name TEXT NOT NULL,
    sequence_order INTEGER NOT NULL,
    stage TEXT NOT NULL,
    tension REAL,
    transformation_pressure REAL,
    description TEXT,
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

CREATE TABLE IF NOT EXISTS characters (
    character_id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL,
    character_name TEXT NOT NULL,
    narrative_role TEXT NOT NULL,
    initial_state REAL,
    final_state REAL,
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

CREATE TABLE IF NOT EXISTS character_relationships (
    relationship_id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL,
    source_character_id INTEGER NOT NULL,
    target_character_id INTEGER NOT NULL,
    relationship_type TEXT NOT NULL,
    FOREIGN KEY (story_id) REFERENCES stories(story_id),
    FOREIGN KEY (source_character_id) REFERENCES characters(character_id),
    FOREIGN KEY (target_character_id) REFERENCES characters(character_id)
);

CREATE TABLE IF NOT EXISTS motifs (
    motif_id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL,
    motif_name TEXT NOT NULL,
    symbolic_function TEXT NOT NULL,
    frequency INTEGER,
    interpretation_note TEXT,
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

CREATE TABLE IF NOT EXISTS conflicts (
    conflict_id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL,
    conflict_type TEXT NOT NULL,
    description TEXT NOT NULL,
    stakes TEXT NOT NULL,
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

CREATE TABLE IF NOT EXISTS turning_points (
    turning_point_id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    turning_point_type TEXT NOT NULL,
    interpretation_note TEXT,
    FOREIGN KEY (story_id) REFERENCES stories(story_id),
    FOREIGN KEY (event_id) REFERENCES narrative_events(event_id)
);

CREATE TABLE IF NOT EXISTS themes (
    theme_id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL,
    theme_name TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

CREATE TABLE IF NOT EXISTS media_forms (
    media_form_id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL,
    medium TEXT NOT NULL,
    adaptation_note TEXT,
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

INSERT INTO stories
(story_id, title, tradition_or_medium, description, cultural_context, ethical_caution)
VALUES
(1, 'Synthetic Teaching Story', 'Teaching example', 'A synthetic story model for narrative systems analysis.', 'Created for educational use.', 'Do not treat synthetic structure as universal narrative law.');
