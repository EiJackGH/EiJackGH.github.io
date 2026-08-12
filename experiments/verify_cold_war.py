import sys
import os
from playwright.sync_api import sync_playwright

def run_verification(page):
    print("Navigating to DEFCON Zero: Cold War page...")
    page.goto("http://localhost:3000/experiments/cold-war/")
    page.wait_for_timeout(1000)

    # 1. Take a screenshot of the initial Faction Selection layout
    print("Capturing initial faction selection layout...")
    page.screenshot(path="experiments/cold-war/cold_war_faction_selection.png")

    # 2. Select USA Faction (The Western Bloc)
    print("Selecting Faction 'USA'...")
    btn_usa = page.get_by_role("button", name="🇺🇸 THE WESTERN BLOC United States of America")
    btn_usa.click(force=True)
    page.wait_for_timeout(1000)

    # 3. Take a screenshot of the main active dashboard layout
    print("Capturing active dashboard layout...")
    page.screenshot(path="experiments/cold-war/cold_war_dashboard.png")

    # Verify that HUD has correct initial values
    treasury_val = page.locator("#hud-treasury").inner_text()
    print("Starting Treasury value:", treasury_val)
    assert treasury_val == "$100M", f"Expected $100M, got {treasury_val}"

    # 4. Click 'Fund Space Race' ($20M)
    print("Executing 'Fund Space Race' action...")
    btn_space = page.locator("#btn-action-space")
    btn_space.click(force=True)
    page.wait_for_timeout(1000)

    # Check updated Treasury values after turn advance and action
    # Note: Action spends $20M (100 - 20 = 80), then endTurn() adds $18M (80 + 18 = 98)
    treasury_after = page.locator("#hud-treasury").inner_text()
    print("Treasury value after action and turn end:", treasury_after)
    assert treasury_after == "$98M", f"Expected $98M, got {treasury_after}"

    # 5. Focus a Region (e.g. North America or South America)
    print("Focusing South America region...")
    # South America button contains text "South America"
    btn_sa = page.get_by_role("button", name="South America")
    btn_sa.click(force=True)
    page.wait_for_timeout(1000)

    # Take a screenshot after focusing a region
    print("Capturing region focused layout...")
    page.screenshot(path="experiments/cold-war/cold_war_region_focused.png")

    # 6. Fire Economic Aid in South America ($15M)
    print("Executing 'Economic Aid' tactical action...")
    btn_aid = page.locator("#action-aid")
    btn_aid.click(force=True)
    page.wait_for_timeout(1000)

    # Treasury should spend $15M (98 - 15 = 83), and then endTurn adds $18M (83 + 18 = 101)
    treasury_final = page.locator("#hud-treasury").inner_text()
    print("Final Treasury value after economic aid:", treasury_final)
    assert treasury_final == "$101M", f"Expected $101M, got {treasury_final}"

    # Take final gameplay verification screenshot
    print("Capturing final gameplay verification layout...")
    page.screenshot(path="experiments/cold-war/cold_war_final_verification.png")

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
    print("Cold War verification passed successfully.")
