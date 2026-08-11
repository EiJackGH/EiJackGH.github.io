import sys
import os
from playwright.sync_api import sync_playwright

def run_cuj(page):
    print("Navigating to WW1 Arcade Minigames page...")
    page.goto("http://localhost:3000/experiments/ww1/minigames.html")
    page.wait_for_timeout(1000)

    print("Switching tab to Trench Chess...")
    page.get_by_role("button", name="Trench Chess").click(force=True)
    page.wait_for_timeout(1000)

    # Take an initial screenshot of the Trench Chess board and Tactical support buttons
    page.screenshot(path="experiments/ww1/chess_initial.png")
    print("Initial chess screenshot captured.")

    # Locate the Infantry Draft button
    btn_draft = page.locator("#pw-infantry")
    print("Infantry Draft button is visible:", btn_draft.is_visible())
    print("Infantry Draft button text:", btn_draft.inner_text())

    # Click the Infantry Draft power-up button
    print("Activating Infantry Draft power-up (8 CP)...")
    btn_draft.click(force=True)
    page.wait_for_timeout(1000)

    # Click on a valid empty square in the Allied half (e.g. row 5, col 4 -> 6th row, 5th col)
    target_square = page.locator(".chess-square[data-row='5'][data-col='4']")
    print("Clicking on target square (row 5, col 4) to deploy Infantry Draft...")
    target_square.click(force=True)
    page.wait_for_timeout(1500) # Wait for placement & AI turn transition

    # Take a screenshot after power-up deployment and AI turn response
    page.screenshot(path="experiments/ww1/chess_powerup_deployed.png")
    print("Powerup deployed screenshot captured.")

    # Now select a standard Allied piece and highlight its moves (e.g. Pawn at row 6, col 3 -> 'P')
    pawn_square = page.locator(".chess-square[data-row='6'][data-col='3']")
    print("Selecting Allied Infantry pawn at row 6, col 3...")
    pawn_square.click(force=True)
    page.wait_for_timeout(1000)

    # Take screenshot of selected piece with valid moves highlighted
    page.screenshot(path="experiments/ww1/chess_piece_selected.png")
    print("Piece selected screenshot captured.")

    # Move pawn to row 5, col 3
    dest_square = page.locator(".chess-square[data-row='5'][data-col='3']")
    print("Advancing Pawn to row 5, col 3...")
    dest_square.click(force=True)
    page.wait_for_timeout(1500) # Wait for move and AI response

    # Take final screenshot of the gameplay state
    page.screenshot(path="experiments/ww1/chess_final_verification.png")
    print("Final gameplay screenshot captured.")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        print("Launching headless Chromium...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            run_cuj(page)
        except Exception as e:
            print("ERROR occurred:", e)
            import traceback
            traceback.print_exc()
        finally:
            print("Closing browser...")
            browser.close()
    print("Playwright run finished.")
