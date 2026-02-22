/**
 * noscript.js - Feature Detection for the Lab
 */
(function() {
    const features = {
        canvas: !!window.CanvasRenderingContext2D,
        localStorage: (function() {
            try { return !!window.localStorage; } catch(e) { return false; }
        })(),
        arrowFunctions: (function() {
            try { new Function('() => {}'); return true; } catch(e) { return false; }
        })()
    };

    if (!features.canvas || !features.arrowFunctions) {
        alert("🚨 Your browser is too old to run this experiment! Please update to a modern browser like Chrome, Firefox, or Edge.");
        // Optional: Redirect to a 'lite' version of your blog
        // window.location.href = "../../blog/";
    }
})();
