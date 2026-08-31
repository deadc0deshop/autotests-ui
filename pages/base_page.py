from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page):
        self.page = page


    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle")


    def refresh(self):
        self.page.reload(wait_until="networkidle")