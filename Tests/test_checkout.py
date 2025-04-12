import pytest
from playwright.sync_api import expect
from Pages.CheckoutPage import CheckoutPage

@pytest.mark.order(6)
def test_checkout(page):
    """
    Test Case: Verify that wish listed Smartphone is moved to cart.

    Flow:
    1. Navigate to Shopping Cart.
    2. Provide Country, ZIP and estimate the delivery.
    3. Agree to the terms of service.
    4. Checkout the cart.
    5. Verify that the user moves to Billing page.
    """

    # Instantiate the CheckoutPage
    checkout_page = CheckoutPage(page)

    # Navigate to Shopping Cart.
    checkout_page.click_cart_link()

    # Provide Country, ZIP and estimate the delivery.
    checkout_page.select_country()
    checkout_page.provide_zip_code()

    # Agree to the terms of service.
    checkout_page.agree_terms()

    # Checkout the cart.
    checkout_page.checkout()

    # Verify that the user moves to Billing page.
    checkout = checkout_page.verify_checkout()
    expect(checkout).to_have_text('Billing address')

    print('✅ TEST CHECKOUT PASSED')