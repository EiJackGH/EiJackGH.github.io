import sys
import os
from playwright.sync_api import sync_playwright

def run_translate_verification():
    with sync_playwright() as p:
        print("Launching headless Chromium...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        print("Navigating to EiJackGH Translate Experiment...")
        page.goto("http://localhost:3000/experiments/translate/index.html")
        page.wait_for_timeout(2000)

        # 1. Verify Page Title
        title = page.title()
        print(f"Page Title: '{title}'")
        if "EiJackGH Translate" not in title:
            raise Exception(f"Unexpected title: {title}")

        # 2. Enter "Hello World" and verify natural language fallback translation
        print("Entering 'Hello World' in source-text...")
        page.fill("#source-text", "Hello World")
        page.wait_for_timeout(1000) # wait for debounce

        print("Clicking 'Translate Now' button to execute translation...")
        page.click("#btn-translate")
        page.wait_for_timeout(1500)

        target_val = page.input_value("#target-text")
        print(f"Translated output (English -> Spanish): '{target_val}'")
        if not target_val:
            raise Exception("Target translation is empty!")

        # 3. Switch to Morse Code mode
        print("Switching mode to Morse Code...")
        page.select_option("#translation-mode", "morse")
        page.wait_for_timeout(1000)

        # Verify cipher setting dropdown is visible and select 'encode'
        is_cipher_visible = page.is_visible("#cipher-setting")
        print(f"Is cipher setting dropdown visible? {is_cipher_visible}")
        page.select_option("#cipher-setting", "encode")
        page.wait_for_timeout(500)

        page.click("#btn-translate")
        page.wait_for_timeout(1000)

        morse_val = page.input_value("#target-text")
        print(f"Morse Code output: '{morse_val}'")
        if "...." not in morse_val and "-.-." not in morse_val:
            # Let's check Morse alphabet representation for 'H' is '....'
            raise Exception(f"Expected Morse dots/dashes, got: '{morse_val}'")

        # 4. Switch to L33t Speak mode
        print("Switching mode to L33t Speak...")
        page.select_option("#translation-mode", "leet")
        page.wait_for_timeout(1000)
        page.select_option("#cipher-setting", "simple")
        page.wait_for_timeout(500)

        page.click("#btn-translate")
        page.wait_for_timeout(1000)

        leet_val = page.input_value("#target-text")
        print(f"L33t Speak output: '{leet_val}'")
        if "H3LL0" not in leet_val and "3" not in leet_val:
            raise Exception(f"Expected L33t substitutions, got: '{leet_val}'")

        # 5. Capture verification screenshot
        screenshot_dir = "experiments/translate"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, "translate_verification.png")
        page.screenshot(path=screenshot_path)
        print(f"Verification screenshot captured successfully at: '{screenshot_path}'")

        print("Closing browser...")
        browser.close()

if __name__ == "__main__":
    try:
        run_translate_verification()
        print("SUCCESS: EiJackGH Translate verification passed.")
    except Exception as e:
        print("ERROR occurred during translation verification:", e)
        import traceback
        traceback.print_exc()
        sys.exit(1)
