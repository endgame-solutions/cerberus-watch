from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    current_dir = os.getcwd()
    login_url = f"file://{current_dir}/login.html"

    # Intercept redirect so we can stay on the page to see the loading state and take a screenshot
    # before the setTimeout triggers the location.href assignment
    page.add_init_script("""
        Object.defineProperty(window, 'location', {
            configurable: true,
            get() {
                return {
                    href: 'mock_href',
                    set href(val) {
                        console.log('Redirecting to: ' + val);
                    }
                };
            }
        });
    """)

    page.goto(login_url)
    page.wait_for_timeout(500)

    # Fill username and password
    page.get_by_label("Username").fill("testuser")
    page.wait_for_timeout(500)
    page.get_by_label("Password").fill("password123")
    page.wait_for_timeout(500)

    # Click the login button
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(200) # Short wait to let DOM update

    # Verify the spinner appeared and button is disabled
    # the button text should change to "Logging in..."
    button = page.locator("#login-form button[type='submit']")

    # Take screenshot while loading
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
    os.makedirs("/home/jules/verification/videos", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()