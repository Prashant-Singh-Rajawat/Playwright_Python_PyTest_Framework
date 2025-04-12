from playwright.sync_api import expect
from Pages.LogoutPage import LogoutPage

def test_logout(page):
    """
    Test Case: Verify that wish listed Smartphone is moved to cart.

    Flow:
    1. Navigate to Shopping Cart.
    5. Verify that the user moves to Billing page.
    """

    # Instantiate the LogoutPage
    logout_page = LogoutPage(page)

    # Logout
    logout_page.logout()

    # Verify that the log-out is successful
    logout = logout_page.verify_logout()
    expect(logout).to_have_text('Log in')

    print('✅ TEST LOGOUT PASSED')