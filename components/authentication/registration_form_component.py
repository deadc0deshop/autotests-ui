from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input
import allure

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.login_input = Input(page, 'registration-form-username-input', 'Login')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')

    @allure.step('Fill registration form')
    def fill(self, email: str, login: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.login_input.fill(login)
        self.login_input.check_have_value(login)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step('Check visible registration form')
    def check_visible(self, email: str, login: str, password: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.login_input.check_visible()
        self.login_input.check_have_value(login)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)