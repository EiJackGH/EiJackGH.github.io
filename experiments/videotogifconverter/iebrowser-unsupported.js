/**
 * internetexplorerbrowser-unsupported.js
 * Strict ES5 compliance script to detect Internet Explorer lifecycle contexts.
 * Blocks application runtime execution for obsolete engines.
 */
(function () {
  'use strict';

  // 1. Detect Internet Explorer via MS-specific engine tokens
  // - document.documentMode catches IE 8 through IE 11
  // - window.ActiveXObject catches legacy variants
  var isInternetExplorer = !!window.MSInputMethodContext || !!document.documentMode || typeof window.ActiveXObject !== 'undefined';

  if (isInternetExplorer) {
    // Standard block wrapper to intercept DOM attachment phases safely
    var checkAndInjectBlocker = function () {
      var body = document.body;
      if (!body) {
        // If body isn't ready, defer execution to next tick
        setTimeout(checkAndInjectBlocker, 10);
        return;
      }

      // Hide or clear the primary application node to prevent broken runtime structures
      var appRoot = document.getElementById('app-root');
      if (appRoot) {
        appRoot.style.display = 'none';
        appRoot.innerHTML = '';
      }

      // Create a heavily compatible modal layout container
      var container = document.createElement('div');
      container.id = 'ie-unsupported-warning';
      
      // Inline styling using simple properties fully parsed by legacy CSS engines
      container.style.backgroundColor = '#ffffff';
      container.style.color = '#333333';
      container.style.fontFamily = 'Arial, sans-serif';
      container.style.padding = '40px 20px';
      container.style.textAlign = 'center';
      container.style.maxWidth = '550px';
      container.style.margin = '50px auto';
      container.style.border = '1px solid #cccccc';
      container.style.borderRadius = '4px';

      // Safe DOM injection mapping
      container.innerHTML = 
        '<h2 style="color: #d9534f; margin-top: 0;">Browser Out of Date</h2>' +
        '<p style="font-size: 15px; line-height: 1.6; color: #555555;">' +
          'You are currently using Internet Explorer. This application handles high-intensity client-side file conversions that require modern browser performance layers.' +
        '</p>' +
        '<p style="font-size: 14px; margin: 20px 0; font-weight: bold; color: #333333;">' +
          'Internet Explorer is no longer supported.' +
        '</p>' +
        '<div style="margin-top: 30px; font-size: 13px; color: #777777;">' +
          'Please switch to a modern web application browser such as Google Chrome, Microsoft Edge, or Mozilla Firefox to convert your files.' +
        '</div>';

      body.appendChild(container);
    };

    // Initialize execution hook immediately
    checkAndInjectBlocker();

    // Force structural termination of downstream script asset parsing
    throw new Error('[Legacy Engine Block] Application execution prevented on unsupported Internet Explorer browser.');
  }
})();
