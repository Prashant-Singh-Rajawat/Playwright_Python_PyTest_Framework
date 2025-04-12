import pytest
from playwright.sync_api import expect
from Pages.WishListPage import WishListPage

@pytest.mark.order(5)
def test_wishlist(page):
    """
    Test Case: Verify that wish listed Smartphone is moved to cart.

    Flow:
    1. Hover on the wishlist.
    2. Click on Go to cart.
    3. Select the smartphone.
    4. Move the smartphone to the cart.
    5. Verify that the cart count displays '(4)'.
    """

    # Instantiate the ComputersPage
    wishlist_page = WishListPage(page)

    # Move the wish listed Smartphone to cart
    wishlist_page.hover_on_wishlist()
    wishlist_page.move_to_cart()

    # Verify that cart count is updated to (3)
    cart_count = wishlist_page.verify_cart_count()
    expect(cart_count).to_have_text('(4)')

    print('✅ TEST WISHLIST PASSED')