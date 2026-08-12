/**
 * noscript.js - Feature Detection & IE Blocker for EiJackGH Translate
 */
(function() {
    'use strict';

    // 1. Detect Internet Explorer via MS-specific engine tokens
    var isInternetExplorer = !!window.MSInputMethodContext || !!document.documentMode || typeof window.ActiveXObject !== 'undefined';

    if (isInternetExplorer) {
        alert("Your Internet Explorer doesnt support EiJackGH Translate");

        var checkAndInjectBlocker = function() {
            var body = document.body;
            if (!body) {
                setTimeout(checkAndInjectBlocker, 10);
                return;
            }

            body.innerHTML = '';

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
                '<div style="max-width: 600px; margin: 100px auto; padding: 40px; background: #1e293b; border: 2px solid #38bdf8; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">' +
                    '<div style="font-size: 50px; margin-bottom: 20px;">🌐</div>' +
                    '<h2 style="color: #38bdf8; margin-top: 0; font-size: 24px;">Internet Explorer Not Supported</h2>' +
                    '<p style="font-size: 16px; line-height: 1.6; color: #cbd5e1; margin-top: 20px;">' +
                        'EiJackGH Translate relies on modern standards including HTML5, Web Audio API, Speech Synthesis, and ES6+ JavaScript, which are completely incompatible with Internet Explorer.' +
                    '</p>' +
                    '<p style="font-size: 15px; font-weight: bold; color: #14b8a6; margin-top: 25px;">' +
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
        throw new Error('Your Internet Explorer doesnt support EiJackGH Translate');
    }

    // 2. Feature detection for modern web APIs
    var hasAudioContext = !!(window.AudioContext || window.webkitAudioContext);
    var hasSpeechSynthesis = !!window.speechSynthesis;

    if (!hasAudioContext || !hasSpeechSynthesis) {
        console.warn("⚠️ browser-unsupported: Missing AudioContext or SpeechSynthesis. Certain features of EiJackGH Translate may be disabled.");
    }
})();
