from Pages.BasePage import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_link = "//span[normalize-space()='Shopping cart']"
        self.go_to_cart = "//input[@value='Go to cart']"
        self.coupon = '.discount-coupon-code'
        self.coupon_btn = "input[value='Apply coupon']"
        self.gift_card = '.gift-card-coupon-code'
        self.gift_card_btn = '.button-2 apply-gift-card-coupon-code-button'
        self.country_dropdown = '#CountryId'
        self.state_dropdown = '#StateProvinceId'
        self.zip_postal_code = '#ZipPostalCode'
        self.estimate_shipping_btn = "input[value='Estimate shipping']"
        self.term_of_service = '#termsofservice'
        self.checkout_btn = '#checkout'
        self.billing = "//h2[normalize-space()='Billing address']"

    def click_cart_link(self):
        self.hover(self.cart_link)
        self.click(self.go_to_cart)

    def apply_coupon(self):
        pass

    def gift_coupon(self):
        pass

    def select_country(self):
        self.drop_down(self.country_dropdown,'Canada')

    def provide_zip_code(self):
        self.fill(self.zip_postal_code,'111111')
        self.click(self.estimate_shipping_btn)

    def agree_terms(self):
        self.click(self.term_of_service)

    def checkout(self):
        self.click(self.checkout_btn)

    def verify_checkout(self):
        return self.page.locator(self.billing)