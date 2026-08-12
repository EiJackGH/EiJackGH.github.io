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

    # Take an initial screenshot
    page.screenshot(path="experiments/ww1/crown_destroy_initial.png")
    print("Initial chess screenshot captured.")

    # Locate the Crown Destroy button
    btn_crown_destroy = page.locator("#pw-crown-destroy")
    assert btn_crown_destroy.is_visible(), "Crown Destroy button should be visible"
    print("Crown Destroy button is visible:", btn_crown_destroy.is_visible())
    print("Crown Destroy button text:\n", btn_crown_destroy.inner_text())

    # Get initial CP
    initial_cp = int(page.locator("#alliedCPVal").inner_text().strip())
    print(f"Initial Allied CP: {initial_cp}")
    assert initial_cp == 10, f"Expected initial CP to be 10, got {initial_cp}"

    # Click the Crown Destroy power-up button
    print("Activating Crown Destroy power-up (1 CP)...")
    btn_crown_destroy.click(force=True)
    page.wait_for_timeout(1000)

    # Screenshot with Crown Destroy active
    page.screenshot(path="experiments/ww1/crown_destroy_selected.png")
    print("Crown Destroy selected screenshot captured.")

    # Locate a target square with an enemy crowned piece (e.g. row 0, col 3 -> General Staff 'q')
    target_square = page.locator(".chess-square[data-row='0'][data-col='3']")

    # Confirm that the target square has a piece in it before the strike
    has_piece_before = target_square.locator(".chess-piece").count() > 0
    assert has_piece_before, "Target square (row 0, col 3) should have an enemy crowned piece before the strike"

    print("Targeting square (row 0, col 3) to execute Crown Destroy...")
    target_square.click(force=True)
    page.wait_for_timeout(2000) # Wait for execution & AI response

    # Confirm that the piece is eliminated
    has_piece_after = target_square.locator(".chess-piece").count() > 0
    assert not has_piece_after, "Target square should be empty after Crown Destroy"
    print("Target piece successfully eliminated!")

    # Verify battle log
    battle_log = page.locator("#battleLog").inner_text()
    print("--- Battle Log Output ---")
    print(battle_log)
    print("-------------------------")

    assert "Crown Destroy obliterates" in battle_log, "Battle log should record the crown destroy"

    # Take screenshot of the result
    page.screenshot(path="experiments/ww1/crown_destroy_executed.png")
    print("Crown Destroy executed screenshot captured successfully.")

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
