import pytest
from Pages.LoginPage import LoginPage
from playwright.sync_api import expect

@pytest.mark.order(2)
def test_login(page):
    """
    Test Case: Verify login is successful.

    Flow:
    1. Click on the 'Log in'.
    2. Provide Username and Password.
    3. Log in.
    4. Verify that the login is successful.
    """

    # Instantiate the LoginPage
    login_page = LoginPage(page)

    # Click on login and provide credentials
    login_page.click_login()
    login_page.enter_credentials()

    # Verify that the login is successful
    login = login_page.verify_login()
    expect(login).to_have_text('Log out')
    print('✅ TEST LOGIN PASSED')