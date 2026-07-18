/**
 * noscript.js - Feature Detection for Flag Maker & Simulator
 */
(function() {
    const hasCanvas = !!window.CanvasRenderingContext2D;
    const hasBlob = !!window.Blob && !!window.URL && !!URL.createObjectURL;

    if (!hasCanvas || !hasBlob) {
        alert("🚨 Laboratory Error: Your browser does not support the technologies required for this Vexillology Flag Maker experiment. Please upgrade to a modern browser.");
    }
})();
