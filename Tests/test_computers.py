import pytest
from playwright.sync_api import expect
from Pages.ComputersPage import ComputersPage

@pytest.mark.order(4)
def test_computers(page):
    """
    Test Case: Verify adding a Computer to the cart.

    Flow:
    1. Navigate to the Computers section.
    2. Select Desktop menu.
    3. Select a desktop.
    4. Define attributes of the desktop.
    5. Add the desktop to the cart.
    6. Verify the cart count displays '(3)'.
    """

    # Instantiate the ComputersPage
    computers_page = ComputersPage(page)

    # Select, define attributes and add desktop to cart
    computers_page.select_desktop()
    computers_page.define_attributes()
    computers_page.add_to_cart()

    # Verify that cart count is updated to (3)
    cart = computers_page.verify_cart()
    expect(cart).to_have_text('(3)', timeout=5000)

    print('✅ TEST COMPUTERS PASSED')