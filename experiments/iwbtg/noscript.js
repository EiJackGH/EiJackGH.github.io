/**
 * noscript.js - Feature Detection for EiJackGH Lab
 */
(function() {
    // Check for essential game engine features
    const hasCanvas = !!window.CanvasRenderingContext2D;
    const hasArrowFunctions = (function() { 
        try { eval("() => {}"); return true; } catch (e) { return false; } 
    })();

    if (!hasCanvas || !hasArrowFunctions) {
        // If the browser is too old, we alert the user
        alert("🚨 Laboratory Error: Your browser does not support the technologies required for this experiment. Please upgrade to a modern browser.");
        
        // Optional: Redirect back to your blog which is likely simpler HTML
        // window.location.href = "../../blog/";
    }
})();
