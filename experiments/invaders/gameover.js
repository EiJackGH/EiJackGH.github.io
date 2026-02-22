/**
 * gameover.js - Handles the UI state when the game ends
 */

const GameOver = {
    draw: function(ctx, canvas, score) {
        // 1. Darken the background
        ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // 2. Draw "Victory" Text
        ctx.fillStyle = "#00FF00";
        ctx.font = "bold 40px 'Courier New'";
        ctx.textAlign = "center";
        ctx.fillText("MISSION COMPLETE", canvas.width / 2, canvas.height / 2 - 20);

        // 3. Display Final Score
        ctx.font = "20px 'Courier New'";
        ctx.fillStyle = "#FFFFFF";
        ctx.fillText("FINAL SCORE: " + score, canvas.width / 2, canvas.height / 2 + 30);

        // 4. Instructions
        ctx.fillStyle = "#888888";
        ctx.font = "16px 'Courier New'";
        ctx.fillText("Press [R] to Restart Laboratory", canvas.width / 2, canvas.height / 2 + 80);
    },

    listenForRestart: function() {
        window.addEventListener('keydown', (e) => {
            if (e.code === 'KeyR') {
                location.reload();
            }
        });
    }
};

// Export for use in game.js
window.GameOver = GameOver;
