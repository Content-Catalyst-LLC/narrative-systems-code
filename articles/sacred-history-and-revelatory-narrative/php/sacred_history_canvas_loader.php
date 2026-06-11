<?php
function cc_sacred_history_canvas_load_json($path) {
    if (!file_exists($path)) {
        return array();
    }
    $decoded = json_decode(file_get_contents($path), true);
    return is_array($decoded) ? $decoded : array();
}
