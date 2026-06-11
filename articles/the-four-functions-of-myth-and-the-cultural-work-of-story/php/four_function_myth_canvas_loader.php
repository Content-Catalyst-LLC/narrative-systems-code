<?php
function cc_four_function_myth_canvas_load_json($path) {
    if (!file_exists($path)) {
        return array();
    }
    $decoded = json_decode(file_get_contents($path), true);
    return is_array($decoded) ? $decoded : array();
}
