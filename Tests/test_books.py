import pytest
from Pages.BooksPage import BooksPage
from playwright.sync_api import expect

@pytest.mark.order(3)
def test_books(page):
    """
    Test Case: Verify adding a book to the cart.

    Flow:
    1. Navigate to the Books section.
    2. Filter books Under $25.
    3. Sort the books by 'Price: Low to High'.
    4. Select a specific book.
    5. Change the quantity to 2.
    6. Add the book to the cart.
    7. Verify the cart count displays '(2)'.
    """
    # Instantiate the BooksPage
    books_page = BooksPage(page)

    # Navigate to Books and apply filters
    books_page.click_on_books()
    books_page.select_price_by_filter()
    books_page.sort_by_low_to_high()

    # Select and add book to cart
    books_page.select_book()
    books_page.select_quantity()
    books_page.add_to_cart()

    # Verify that cart count is updated to (2)
    cart = books_page.verify_cart_count()
    expect(cart).to_have_text('(2)', timeout=5000)

    print('✅ TEST BOOKS PASSED')