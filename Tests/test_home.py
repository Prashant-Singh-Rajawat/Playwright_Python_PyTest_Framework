import pytest
from Pages.HomePage import HomePage
from playwright.sync_api import expect

@pytest.mark.order(1)
def test_home(page):
    """
    Test Case: Verify adding a smartphone to the wishlist.

    Flow:
    1. Navigate to the Search option.
    2. Search for Smartphone.
    3. Click on Smartphone.
    4. Select a specific book.
    5. Add the smartphone to the wishlist.
    6. Verify the wishlist count displays '(1)'.
    """

    # Instantiate the HomePage
    homepage = HomePage(page)

    # Search for smartphone and addit to the wishlist
    homepage.search_smartphone()

    # Verify that wishlist count is updated to (1)
    wishlist_count = homepage.add_to_wishlist()
    expect(wishlist_count).to_have_text('(1)')
    print('✅ TEST HOME PASSED')