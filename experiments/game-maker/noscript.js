/**
 * noscript.js - Feature Detection for EiJackGH Lab Game Maker
 */
(function() {
    // Check for essential game engine features
    const hasCanvas = !!window.CanvasRenderingContext2D;
    const hasAudioContext = !!(window.AudioContext || window.webkitAudioContext);
    const hasArrowFunctions = (function() {
        try { eval("() => {}"); return true; } catch (e) { return false; }
    })();

    if (!hasCanvas || !hasArrowFunctions || !hasAudioContext) {
        alert("🚨 Laboratory Error: Your browser does not support the web technologies required for the Retro Game Maker. Please upgrade to a modern browser with HTML5 Canvas and Web Audio API support.");
    }
})();
