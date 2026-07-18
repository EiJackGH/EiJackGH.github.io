/**
 * noscript.js - Feature Detection for SVG to PNG Converter
 */
(function() {
    const hasCanvas = !!window.CanvasRenderingContext2D;
    const hasBlob = !!window.Blob && !!window.URL && !!URL.createObjectURL;
    const hasFileReader = !!window.FileReader;

    if (!hasCanvas || !hasBlob || !hasFileReader) {
        alert("🚨 Laboratory Error: Your browser does not support the technologies required for this SVG to PNG Converter experiment. Please upgrade to a modern browser.");
    }
})();
