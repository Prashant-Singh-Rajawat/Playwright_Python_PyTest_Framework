from Pages.BasePage import BasePage

class BooksPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.books_link = "//ul[@class='top-menu']//a[normalize-space()='Books']"
        self.sort_by = '#products-orderby'
        self.under_25 = '//li[1]//a[1]//span[1]'
        self.choose_book = "//div[@class='product-item']//img[@title='Show details for Health Book']"
        self.book_quantity = '#addtocart_22_EnteredQuantity'
        self.click_add_to_cart = '#add-to-cart-button-22'
        self.cart = '.cart-qty'

    def click_on_books(self):
        self.click(self.books_link)

    def select_price_by_filter(self):
        self.click(self.under_25)

    def sort_by_low_to_high(self):
        self.drop_down(self.sort_by,'Price: Low to High')

    def select_book(self):
        self.click(self.choose_book)

    def select_quantity(self):
        self.fill(self.book_quantity,'2')

    def add_to_cart(self):
        self.click(self.click_add_to_cart)

    def verify_cart_count(self):
        return self.page.locator(self.cart)