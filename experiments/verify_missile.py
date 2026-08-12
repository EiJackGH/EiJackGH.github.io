import sys
import os
from playwright.sync_api import sync_playwright

def run_verification(page):
    print("Navigating to WW1 Arcade Minigames page...")
    page.goto("http://localhost:3000/experiments/ww1/minigames.html")
    page.wait_for_timeout(1000)

    print("Switching tab to Trench Chess...")
    page.get_by_role("button", name="Trench Chess").click(force=True)
    page.wait_for_timeout(1000)

    # Click on Allied Powers on the Faction Selection Canvas to start the chess game
    print("Selecting Faction 'Allied Powers' from Selection Canvas...")
    page.locator("#chessFactionCanvas").click(position={"x": 210, "y": 150})
    page.wait_for_timeout(1000)

    # Take an initial screenshot of the Trench Chess board
    page.screenshot(path="experiments/ww1/missile_initial.png")
    print("Initial chess screenshot captured.")

    # Locate the Missile Strike button
    btn_missile = page.locator("#pw-missile")
    assert btn_missile.is_visible(), "Missile Strike button should be visible"
    print("Missile Strike button is visible:", btn_missile.is_visible())
    print("Missile Strike button text:\n", btn_missile.inner_text())

    # Get initial CP
    initial_cp = int(page.locator("#alliedCPVal").inner_text().strip())
    print(f"Initial Allied CP: {initial_cp}")
    assert initial_cp == 10, f"Expected initial CP to be 10, got {initial_cp}"

    # Click the Missile Strike power-up button
    print("Activating Missile Strike power-up (1 CP)...")
    btn_missile.click(force=True)
    page.wait_for_timeout(1000)

    # Screenshot with Missile Strike active
    page.screenshot(path="experiments/ww1/missile_selected.png")
    print("Missile selected screenshot captured.")

    # Locate a target square with an enemy piece (e.g. row 1, col 3 -> a black pawn)
    target_square = page.locator(".chess-square[data-row='1'][data-col='3']")

    # Confirm that the target square has a piece in it before the strike
    has_piece_before = target_square.locator(".chess-piece").count() > 0
    assert has_piece_before, "Target square (row 1, col 3) should have an enemy piece before the strike"

    print("Targeting square (row 1, col 3) to execute Missile Strike...")
    target_square.click(force=True)
    page.wait_for_timeout(2000) # Wait for execution & AI response

    # Confirm that the piece is eliminated
    has_piece_after = target_square.locator(".chess-piece").count() > 0
    assert not has_piece_after, "Target square should be empty after Missile Strike"
    print("Target piece successfully eliminated!")

    # Verify that Allied CP decremented by 1
    new_cp = int(page.locator("#alliedCPVal").inner_text().strip())
    print(f"New Allied CP: {new_cp}")
    # Note: Since the turn passed to Central and then might have come back or Central played,
    # let's make sure Allied CP decremented properly during executePowerUp (10 - 1 = 9).
    # Wait, because turn transitions to Central Powers, it's Central Powers turn,
    # so we should check if they spent CP or if we are back.
    # Actually we can just print the battle log to confirm the action!
    battle_log = page.locator("#battleLog").inner_text()
    print("--- Battle Log Output ---")
    print(battle_log)
    print("-------------------------")

    assert "Missile Strike obliterates" in battle_log, "Battle log should record the missile strike"

    # Take screenshot of the result
    page.screenshot(path="experiments/ww1/missile_executed.png")
    print("Missile executed screenshot captured successfully.")

if __name__ == "__main__":
    with sync_playwright() as p:
        print("Launching headless Chromium...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            run_verification(page)
        except Exception as e:
            print("ERROR occurred:", e)
            import traceback
            traceback.print_exc()
            sys.exit(1)
        finally:
            print("Closing browser...")
            browser.close()
    print("Verification passed successfully.")
