<?php
/**
 * Traditional Narrative Forms Canvas loader scaffold.
 */

function cc_traditional_narrative_forms_canvas_load_json($path) {
    if (!file_exists($path)) {
        return array();
    }

    $contents = file_get_contents($path);
    $decoded = json_decode($contents, true);

    if (!is_array($decoded)) {
        return array();
    }

    return $decoded;
}
