from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input_registration = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input_registration.fill('user.name@gmail.com')

    login_input_registration = page.get_by_test_id('registration-form-username-input').locator('input')
    login_input_registration.fill('username')

    password_input_registration = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input_registration.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()


    dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard).to_be_visible()
    expect(dashboard).to_have_text('Dashboard')
