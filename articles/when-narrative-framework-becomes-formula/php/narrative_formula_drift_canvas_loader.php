<?php
function cc_narrative_formula_drift_canvas_load_json($path) {
    if (!file_exists($path)) { return array(); }
    $decoded = json_decode(file_get_contents($path), true);
    return is_array($decoded) ? $decoded : array();
}
