import pytest
from Utilities.config import BASE_URL
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def page(browser_context):
    page = browser_context.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()