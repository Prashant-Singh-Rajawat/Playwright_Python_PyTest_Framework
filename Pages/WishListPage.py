from Pages.BasePage import BasePage

class WishListPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wishlist_link = "a[class='ico-wishlist'] span[class='cart-label']"
        self.add_to_cart = "//input[@name='addtocart']"
        self.add_cart = "input[value='Add to cart']"
        self.cart_quantity = '.cart-qty'

    def hover_on_wishlist(self):
        self.hover(self.wishlist_link)
        self.click(self.wishlist_link)

    def move_to_cart(self):
        self.click(self.add_to_cart)
        self.click(self.add_cart)

    def verify_cart_count(self):
        return self.page.locator(self.cart_quantity)