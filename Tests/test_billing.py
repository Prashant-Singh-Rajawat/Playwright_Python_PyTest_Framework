import pytest
from playwright.sync_api import expect
from Pages.BillingPage import BillingPage

@pytest.mark.order(7)
def test_billing(page):
    """
    Test Case: Verify that the billing is done successful.

    Flow:
    1. Navigate to Billing.
    2. Provide 'Billing Address' information.
    3. Provide 'Shipping Address' information.
    4. Provide 'Payment Method' information.
    5. Provide 'Payment Information'.
    6. Provide 'Confirm Order' information.
    7. Verify that the billing is done successful.
    """

    # Instantiate the BillingPage
    billing_page = BillingPage(page)

    # Provide 'Select Address' information.
    billing_page.select_address()

    # Provide 'Billing Address' information.
    billing_page.billing_address()

    # Provide 'Shipping Address' information.
    billing_page.shipping_address()

    # Provide 'Payment Method' information.
    billing_page.payment_method()

    # Provide 'Payment Information'.
    billing_page.payment_information()

    # Provide 'Confirm Order' information.
    billing_page.confirm_order()

    # Download Order Details
    billing_page.order_details()

    order_details = billing_page.verify_billing()
    expect(order_details).to_have_text('PDF Invoice')

    print('✅ TEST BILLING PASSED')