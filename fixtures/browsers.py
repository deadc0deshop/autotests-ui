import pytest
from pathlib import Path
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page
from config import settings

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from tools.routes import AppRoute


@pytest.fixture(params=settings.browsers)
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )



@pytest.fixture(scope="session")
def initialize_browser_state(
    playwright: Playwright,
    worker_id: str,
    tmp_path_factory: pytest.TempPathFactory,
) -> Path:
    # xdist workers run their own session fixtures; keep their state files separate.
    state_file = tmp_path_factory.mktemp(f"browser-state-{worker_id}") / "state.json"
    browser = playwright.chromium.launch(headless=settings.headless)  # Используем settings.headless
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email,  # Используем settings.test_user.email
        username=settings.test_user.username,  # Используем settings.test_user.username
        password=settings.test_user.password  # Используем settings.test_user.password
    )
    registration_page.click_registration_button()
    page.wait_for_url("**/#/dashboard", timeout=15000)
    page.wait_for_function(
        """() => {
            const raw = localStorage.getItem('persist:users');
            if (!raw) return false;
            const state = JSON.parse(raw);
            return state.user !== 'null' && state.user !== null && state.users !== '[]';
        }""",
        timeout=15000,
    )

    context.storage_state(path=state_file)
    browser.close()
    return state_file


@pytest.fixture(params=settings.browsers)
def chromium_page_with_state(initialize_browser_state: Path, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=str(initialize_browser_state)
    )
