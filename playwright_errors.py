from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')


    # Locator is not found (wrong locator)
    # unknown = page.locator('#unknowm')
    # expect(unknown).to_be_visible()

    # Incorrect handling with elements
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')


    # Element has not seen in DOM yet
    new_text = 'New Text'

    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text');
            title.textContent = text;
        }
        """,
    new_text)
