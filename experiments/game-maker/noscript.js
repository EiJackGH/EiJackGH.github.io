/**
 * noscript.js - Feature Detection for EiJackGH Lab Game Maker
 */
(function() {
    'use strict';

    // 1. Detect Internet Explorer via MS-specific engine tokens
    // - document.documentMode catches IE 8 through IE 11
    // - window.ActiveXObject catches legacy variants
    var isInternetExplorer = !!window.MSInputMethodContext || !!document.documentMode || typeof window.ActiveXObject !== 'undefined';

    if (isInternetExplorer) {
        alert("Your Internet Explorer doesnt support Game Maker");

        var checkAndInjectBlocker = function() {
            var body = document.body;
            if (!body) {
                setTimeout(checkAndInjectBlocker, 10);
                return;
            }

            // Hide or clear elements to prevent broken layouts
            body.innerHTML = '';

            // Create a heavily compatible legacy container
            var container = document.createElement('div');
            container.id = 'ie-unsupported-warning';
            container.style.backgroundColor = '#0f172a';
            container.style.color = '#f8fafc';
            container.style.fontFamily = 'Arial, sans-serif';
            container.style.padding = '50px 20px';
            container.style.textAlign = 'center';
            container.style.position = 'fixed';
            container.style.top = '0';
            container.style.left = '0';
            container.style.width = '100%';
            container.style.height = '100%';
            container.style.boxSizing = 'border-box';
            container.style.zIndex = '99999';

            container.innerHTML =
                '<div style="max-width: 600px; margin: 100px auto; padding: 40px; background: #1e293b; border: 2px solid #ef4444; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">' +
                    '<div style="font-size: 50px; margin-bottom: 20px;">🚨</div>' +
                    '<h2 style="color: #ef4444; margin-top: 0; font-size: 24px;">Your Internet Explorer doesnt support Game Maker</h2>' +
                    '<p style="font-size: 16px; line-height: 1.6; color: #cbd5e1; margin-top: 20px;">' +
                        'This experiment uses high-performance HTML5 Canvas, Web Audio API, and modern ES6+ JavaScript, which are completely incompatible with Internet Explorer.' +
                    '</p>' +
                    '<p style="font-size: 15px; font-weight: bold; color: #a855f7; margin-top: 25px;">' +
                        'Please switch to a modern web browser to continue:' +
                    '</p>' +
                    '<div style="margin-top: 20px; font-size: 14px; color: #94a3b8; display: inline-block; background: #0f172a; padding: 12px 24px; border-radius: 8px;">' +
                        'Google Chrome &bull; Microsoft Edge &bull; Mozilla Firefox &bull; Apple Safari' +
                    '</div>' +
                    '<div style="margin-top: 30px;">' +
                        '<a href="../../" style="color: #38bdf8; text-decoration: underline; font-weight: bold;">Return to Lab Home</a>' +
                    '</div>' +
                '</div>';

            body.appendChild(container);
        };

        checkAndInjectBlocker();
        throw new Error('Your Internet Explorer doesnt support Game Maker');
    }

    // Check for essential game engine features
    var hasCanvas = !!window.CanvasRenderingContext2D;
    var hasAudioContext = !!(window.AudioContext || window.webkitAudioContext);
    var hasArrowFunctions = (function() {
        try { eval("() => {}"); return true; } catch (e) { return false; }
    })();

    if (!hasCanvas || !hasArrowFunctions || !hasAudioContext) {
        alert("🚨 Laboratory Error: Your browser does not support the web technologies required for the Retro Game Maker. Please upgrade to a modern browser with HTML5 Canvas and Web Audio API support.");
    }
})();
