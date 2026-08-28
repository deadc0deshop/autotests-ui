import pytest
from _pytest.fixtures import FixtureRequest, SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number:int):
    print(f'Number: {number}')



@pytest.mark.parametrize('number, expected',  [(1,1), (2,4), (3,9)])
def test_several_numbers(number:int, expected:int):
    print(f'Number: {number}, expected: {expected}')


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
@pytest.mark.parametrize("os", ["windows", "mac"])
def test_cross_platform(browser, os):
    (print(f'Browser: {browser}, OS: {os}'))


@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser {browser}')


@pytest.mark.parametrize('user', ['Alise', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit cart', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        ...


    def test_user_without_operations(self, user: str):
        ...


users = {
    '+7888': 'User with not',
    '+7235': 'User money',
    '+346346': 'User honey'
}



@pytest.mark.parametrize(
    'phone_number',
   users.keys(),
    ids=lambda phone_number: f'{phone_number} : {users[phone_number]}'
)
def test_identifires(phone_number: str):
    ...