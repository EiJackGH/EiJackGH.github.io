/**
 * browser-unsupported.js
 * Detects modern web APIs required for client-side GIF-to-Video conversion.
 * Redirects or updates the DOM if conditions are not met.
 */
(function () {
  'use strict';

  // Define the core feature set required by your converter
  var requirements = {
    webAssembly: typeof WebAssembly === 'object' && typeof WebAssembly.instantiate === 'function',
    webWorker: typeof Worker !== 'undefined',
    sharedArrayBuffer: typeof SharedArrayBuffer !== 'undefined',
    blob: typeof Blob !== 'undefined' && typeof URL !== 'undefined'
  };

  // Evaluate if any structural feature is missing
  var isUnsupported = !requirements.webAssembly || 
                      !requirements.webWorker || 
                      !requirements.sharedArrayBuffer || 
                      !requirements.blob;

  if (isUnsupported) {
    // Wait until the DOM is loaded to securely manipulate the fallback interface
    document.addEventListener('DOMContentLoaded', function () {
      // 1. Hide the primary app shell to prevent broken interactions
      var appContainer = document.getElementById('app-root') || document.body;
      appContainer.innerHTML = ''; 

      // 2. Inject an explicit browser incompatibility view
      var errorOverlay = document.createElement('div');
      errorOverlay.id = 'unsupported-browser-overlay';
      errorOverlay.style.cssText = 'font-family: system-ui, -apple-system, sans-serif; max-width: 600px; margin: 10% auto; padding: 40px; text-align: center; background: #fff3f3; border: 1px solid #f5c2c2; border-radius: 8px; color: #721c24; box-shadow: 0 4px 6px rgba(0,0,0,0.05);';

      errorOverlay.innerHTML = 
        '<h1 style="margin-top: 0; font-size: 24px;">⚠️ Browser Not Supported</h1>' +
        '<p style="font-size: 16px; line-height: 1.5; color: #555;">' +
          'Our GIF to Video Converter compiles files locally inside your browser using advanced high-performance operations (WebAssembly & Multi-threading).' +
        '</p>' +
        '<p style="font-size: 15px; margin: 20px 0; font-weight: bold;">' +
          'Your current browser environment does not support these features.' +
        '</p>' +
        '<div style="text-align: left; background: #fff; padding: 15px; border-radius: 4px; border: 1px solid #e9ecef; margin: 20px 0; font-size: 13px; font-family: monospace;">' +
          '<strong>Diagnostic Log:</strong><br>' +
          '• WebAssembly: ' + (requirements.webAssembly ? '✅ OK' : '❌ Missing') + '<br>' +
          '• Web Workers: ' + (requirements.webWorker ? '✅ OK' : '❌ Missing') + '<br>' +
          '• SharedArrayBuffer: ' + (requirements.sharedArrayBuffer ? '✅ OK' : '❌ Missing (Check COOP/COEP Headers)') + '<br>' +
          '• Binary Blob Handling: ' + (requirements.blob ? '✅ OK' : '❌ Missing') +
        '</div>' +
        '<p style="font-size: 14px; margin-bottom: 0; color: #666;">' +
          'Please upgrade to a modern version of Google Chrome, Mozilla Firefox, or Microsoft Edge.' +
        '</p>';

      document.body.appendChild(errorOverlay);
    });

    // Stop execution of any downstream application scripts
    throw new Error('[App Security] Execution halted: Browser missing essential APIs.');
  }
})();
