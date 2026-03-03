"""
Send a message in a Google Meet chat via Playwright.

Usage:
  1. Close Brave completely first
  2. Relaunch Brave with debugging:
       /Applications/Brave\ Browser.app/Contents/MacOS/Brave\ Browser --remote-debugging-port=9222
  3. Join your Google Meet call in Brave, open the chat panel
  4. Run this script:
       python3 meet_share.py "your message here"
"""

import sys
import asyncio
from playwright.async_api import async_playwright


async def send_meet_message(message: str):
    async with async_playwright() as p:
        # Connect to the running Brave instance
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        print(f"Connected to Brave ({len(browser.contexts)} context(s))")

        # Find the Google Meet tab
        meet_page = None
        for context in browser.contexts:
            for page in context.pages:
                if "meet.google.com" in page.url:
                    meet_page = page
                    break
            if meet_page:
                break

        if not meet_page:
            print("No Google Meet tab found. Make sure you have a Meet call open.")
            return

        print(f"Found Meet tab: {meet_page.url}")

        # Try to find and click the chat input, then type the message
        # Google Meet chat input is a textarea within the chat panel
        chat_input = meet_page.locator('textarea[aria-label*="Send a message"], textarea[aria-label*="message"], div[aria-label*="Send a message"][contenteditable="true"]')

        try:
            await chat_input.wait_for(timeout=5000)
            await chat_input.click()
            await chat_input.fill(message)
            print(f"Typed message: {message}")

            # Press Enter to send
            await chat_input.press("Enter")
            print("Message sent!")
        except Exception:
            print("Could not find the chat input box.")
            print("Make sure the chat panel is open in your Meet call.")
            print("Taking a screenshot for debugging...")
            await meet_page.screenshot(path="/Users/annie/meet_debug.png")
            print("Screenshot saved to ~/meet_debug.png")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 meet_share.py \"your message\"")
        sys.exit(1)

    asyncio.run(send_meet_message(sys.argv[1]))
