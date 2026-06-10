<?php
/**
 * Voice Perspective Canvas loader scaffold.
 *
 * This file is intentionally simple and framework-neutral.
 * It can be adapted into a WordPress shortcode or block renderer.
 */

function cc_voice_perspective_canvas_load_json($path) {
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
