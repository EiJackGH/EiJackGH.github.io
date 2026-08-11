import sys
import os
from playwright.sync_api import sync_playwright

def run_siam_verification(page):
    print("Navigating to WW1 Lobby Screen...")
    page.goto("http://localhost:3000/experiments/ww1/index.html")
    page.wait_for_timeout(1500)

    # Locate the Siam faction card
    print("Locating Siam faction card...")
    siam_card = page.locator("text=Siam")
    if not siam_card.is_visible():
        raise Exception("Siam card not visible in the lobby grid!")

    print("Siam card text found:", siam_card.inner_text())

    # Click on the Siam faction card
    print("Selecting Siam faction...")
    siam_card.click(force=True)
    page.wait_for_timeout(1000)

    # Take lobby screenshot
    page.screenshot(path="experiments/ww1/siam_lobby_selected.png")
    print("Lobby screenshot with Siam selected captured: experiments/ww1/siam_lobby_selected.png")

    # Click the Launch Operation button
    print("Launching Operation...")
    launch_btn = page.locator("button:has-text('Launch Operation')")
    launch_btn.click(force=True)

    # Wait for the loading screen to disappear
    print("Waiting for loading screen to complete and game loop to start...")
    page.wait_for_selector("#loading-screen", state="hidden", timeout=15000)
    page.wait_for_timeout(2000)

    # Take active gameplay screenshot
    page.screenshot(path="experiments/ww1/siam_game_active.png")
    print("Active gameplay screenshot captured: experiments/ww1/siam_game_active.png")

    # Now verify the Wiki page
    print("Navigating to WW1 Wiki page...")
    page.goto("http://localhost:3000/experiments/ww1/wiki.html")
    page.wait_for_timeout(1500)

    # Scroll to the Siam card
    siam_wiki_header = page.locator("text=Prince Chakrabongse Bhuvanath")
    if not siam_wiki_header.is_visible():
        raise Exception("Siam card in wiki not visible!")

    siam_wiki_header.scroll_into_view_if_needed()
    page.wait_for_timeout(1000)

    # Take wiki screenshot
    page.screenshot(path="experiments/ww1/siam_wiki_card.png")
    print("Wiki screenshot with Siam card captured: experiments/ww1/siam_wiki_card.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        print("Launching headless Chromium...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        try:
            run_siam_verification(page)
        except Exception as e:
            print("ERROR occurred:", e)
            import traceback
            traceback.print_exc()
            sys.exit(1)
        finally:
            print("Closing browser...")
            browser.close()
    print("Verification finished successfully.")
