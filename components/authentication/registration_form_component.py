from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.login_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill(self, email: str, login: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.login_input.fill(login)
        expect(self.login_input).to_have_value(login)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def check_visible(self, email: str, login: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.login_input).to_be_visible()
        expect(self.login_input).to_have_value(login)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)