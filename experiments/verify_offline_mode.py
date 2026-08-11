import sys
import os
from playwright.sync_api import sync_playwright

def run_offline_verification(page, context):
    print("Navigating to WW1 Lobby Screen...")
    page.goto("http://localhost:3000/experiments/ww1/index.html")
    page.wait_for_timeout(1500)

    # 1. Check initial state (should be online, toast is not shown / has no class 'show')
    toast = page.locator("#network-status-toast")
    is_shown_initially = page.evaluate("document.getElementById('network-status-toast').classList.contains('show')")
    print(f"Is toast shown initially? {is_shown_initially}")
    if is_shown_initially:
        raise Exception("Network status toast is shown initially when it shouldn't be!")

    # 2. Go Offline
    print("Going offline (emulating offline mode)...")
    context.set_offline(True)
    # Fire event to be absolutely sure in headless browser context
    page.evaluate("window.dispatchEvent(new Event('offline'))")
    page.wait_for_timeout(1500)

    # Verify toast is shown and has offline class
    is_offline_shown = page.evaluate("document.getElementById('network-status-toast').classList.contains('show')")
    is_offline_class = page.evaluate("document.getElementById('network-status-toast').classList.contains('offline')")
    toast_title = page.locator("#network-toast-title").inner_text()
    toast_desc = page.locator("#network-toast-desc").inner_text()
    news_text = page.locator("#news-text").inner_text()

    print(f"Offline status check - shown: {is_offline_shown}, class offline: {is_offline_class}")
    print(f"Toast Title: {toast_title}")
    print(f"Toast Desc: {toast_desc}")
    print(f"News Ticker: {news_text}")

    if not is_offline_shown:
        raise Exception("Network toast not shown when offline!")
    if not is_offline_class:
        raise Exception("Network toast missing 'offline' class!")
    if "disrupted" not in toast_title.lower():
        raise Exception(f"Expected disruption title, got: {toast_title}")
    if "TELEGRAPH OUTAGE" not in news_text:
        raise Exception(f"Expected news ticker to update to offline status, got: {news_text}")

    # Capture offline screenshot
    os.makedirs("experiments/ww1", exist_ok=True)
    page.screenshot(path="experiments/ww1/offline_disrupted.png")
    print("Offline screenshot captured: experiments/ww1/offline_disrupted.png")

    # 3. Go Online
    print("Going online (emulating online mode)...")
    context.set_offline(False)
    # Fire event to be absolutely sure in headless browser context
    page.evaluate("window.dispatchEvent(new Event('online'))")
    page.wait_for_timeout(1500)

    # Verify toast transitions to online
    is_online_shown = page.evaluate("document.getElementById('network-status-toast').classList.contains('show')")
    is_online_class = page.evaluate("document.getElementById('network-status-toast').classList.contains('online')")
    toast_title_online = page.locator("#network-toast-title").inner_text()
    toast_desc_online = page.locator("#network-toast-desc").inner_text()
    news_text_online = page.locator("#news-text").inner_text()

    print(f"Online status check - shown: {is_online_shown}, class online: {is_online_class}")
    print(f"Toast Title: {toast_title_online}")
    print(f"Toast Desc: {toast_desc_online}")
    print(f"News Ticker: {news_text_online}")

    if not is_online_shown:
        raise Exception("Network toast not shown immediately after going online!")
    if not is_online_class:
        raise Exception("Network toast missing 'online' class!")
    if "restored" not in toast_title_online.lower():
        raise Exception(f"Expected restored title, got: {toast_title_online}")
    if "TELEGRAPH RESTORED" not in news_text_online:
        raise Exception(f"Expected news ticker to update to online status, got: {news_text_online}")

    # Capture online restored screenshot
    page.screenshot(path="experiments/ww1/online_restored.png")
    print("Online restored screenshot captured: experiments/ww1/online_restored.png")

    # 4. Wait for toast to auto-fade (hide)
    print("Waiting for toast to auto-fade out...")
    page.wait_for_timeout(4000)

    is_toast_hidden_now = not page.evaluate("document.getElementById('network-status-toast').classList.contains('show')")
    print(f"Is toast hidden now? {is_toast_hidden_now}")
    if not is_toast_hidden_now:
        raise Exception("Toast failed to auto-hide after transition to online!")

    page.screenshot(path="experiments/ww1/online_hidden.png")
    print("Online hidden screenshot captured: experiments/ww1/online_hidden.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        print("Launching headless Chromium...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        try:
            run_offline_verification(page, context)
        except Exception as e:
            print("ERROR occurred during offline verification:", e)
            import traceback
            traceback.print_exc()
            sys.exit(1)
        finally:
            print("Closing browser...")
            browser.close()
    print("Verification finished successfully.")
