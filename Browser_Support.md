## 🌐 Browser Support & Compatibility

Because these experiments utilize modern web technologies like **HTML5 Canvas**, **WebAssembly (v86)**, and **ES6+ JavaScript**, they require a modern evergreen browser.

| Browser | Minimum Version | Status | Notes |
| :--- | :--- | :--- | :--- |
| **Chrome / Edge** | 80+ | ✅ Supported | Best performance for Canvas & JIT. |
| **Firefox** | 75+ | ✅ Supported | Fully compatible. |
| **Safari** (macOS) | 13.1+ | ✅ Supported | Requires modern WebKit for some JS features. |
| **Opera** | 67+ | ✅ Supported | Standard Chromium-based support. |
| **Internet Explorer** | All | ❌ Not Supported | Use a modern browser to view experiments. |

### 🛠 Technical Requirements
To ensure the experiments run smoothly, please verify the following are enabled:
* **JavaScript**: Required for all logic and rendering.
* **Hardware Acceleration**: Recommended for 60FPS gameplay in *Space Invaders*.
* **LocalStorage**: Used for saving high scores and experiment states.
