from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regressiong
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')

        login_input = page.get_by_test_id('registration-form-username-input').locator('input')
        login_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_main = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_main).to_be_visible()
        expect(courses_main).to_have_text('Courses')

        block_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(block_text).to_be_visible()
        expect(block_text).to_have_text('There is no results')