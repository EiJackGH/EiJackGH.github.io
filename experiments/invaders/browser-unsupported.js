/**
 * browser-unsupported.js
 * Detects if the browser lacks the minimum requirements for the Lab.
 */
(function() {
    // 1. Define the requirements
    const requirements = {
        canvas: !!window.CanvasRenderingContext2D,
        webAudio: !!(window.AudioContext || window.webkitAudioContext),
        arrowFunctions: (function() { 
            try { eval("() => {}"); return true; } catch (e) { return false; } 
        })()
    };

    // 2. Check if any requirement is missing
    if (!requirements.canvas || !requirements.arrowFunctions) {
        window.addEventListener('DOMContentLoaded', () => {
            const gameContainer = document.querySelector('body');
            
            // Create the warning overlay
            const warning = document.createElement('div');
            warning.style.cssText = `
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: #1a1a1a; color: #ff4444; display: flex;
                flex-direction: column; align-items: center; justify-content: center;
                z-index: 9999; font-family: 'Courier New', monospace; text-align: center;
                padding: 20px;
            `;

            warning.innerHTML = `
                <h1 style="font-size: 2rem; margin-bottom: 1rem;">⚠️ BROWSER NOT SUPPORTED</h1>
                <p style="color: #ccc; max-width: 500px;">
                    This experiment uses <b>HTML5 Canvas</b> and <b>ES6+ JavaScript</b>, 
                    which are not supported by your current browser.
                </p>
                <div style="margin-top: 2rem; border: 1px solid #444; padding: 1rem;">
                    <p style="color: #888; font-size: 0.8rem;">Minimum Requirements:</p>
                    <ul style="list-style: none; color: #00ff00; margin-top: 0.5rem;">
                        <li>Chrome 80+ / Firefox 75+ / Safari 13+</li>
                    </ul>
                </div>
                <a href="../../" style="margin-top: 2rem; color: #44aaff; text-decoration: underline;">
                    Return to Lab Home
                </a>
            `;

            gameContainer.prepend(warning);
        });
    }
})();
