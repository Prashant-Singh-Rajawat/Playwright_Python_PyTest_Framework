from Pages.BasePage import BasePage

class ComputersPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.computers = "//li[@class='inactive']//a[normalize-space()='Computers']"
        self.desktops = "//img[@title='Show products in category Desktops']"
        self.choose_computer = "//img[@title='Show details for Build your own expensive computer']"
        self.attribute_processor = '#product_attribute_74_5_26_82'
        self.attribute_RAM = '#product_attribute_74_6_27_85'
        self.attribute_HDD = '#product_attribute_74_3_28_87'
        self.attribute_software = '#product_attribute_74_8_29_89'
        self.add_to_cart_btn = '#add-to-cart-button-74'
        self.cart_quantity = '.cart-qty'

    def select_desktop(self):
        self.click(self.computers)
        self.click(self.desktops)
        self.click(self.choose_computer)

    def define_attributes(self):
        self.click(self.attribute_processor)
        self.click(self.attribute_RAM)
        self.click(self.attribute_HDD)
        self.click(self.attribute_software)

    def add_to_cart(self):
        self.click(self.add_to_cart_btn)

    def verify_cart(self):
        return self.page.locator(self.cart_quantity)