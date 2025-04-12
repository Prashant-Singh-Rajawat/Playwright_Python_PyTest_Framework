from Pages.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_store = '#small-searchterms'
        self.search_btn = "input[value='Search']"
        self.smartphone = "img[title='Show details for Smartphone']"
        self.add_wishlist = '#add-to-wishlist-button-43'
        self.wishlist_link = '.wishlist-qty'

    def search_smartphone(self):
        self.fill(self.search_store,'SmartPhone')
        self.click(self.search_btn)

    def add_to_wishlist(self):
        self.click(self.smartphone)
        self.click(self.add_wishlist)
        return self.page.locator(self.wishlist_link)