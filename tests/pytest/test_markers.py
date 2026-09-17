import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...


def test_regression_case():
    ...

@pytest.mark.smoke
class TestSuite:
    def test_suite_1(self):
        ...

    def test_suite_2(self):
        ...


class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass


@pytest.mark.smoke
@pytest.mark.critical
def test_critical_login():
    pass


@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass


    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass