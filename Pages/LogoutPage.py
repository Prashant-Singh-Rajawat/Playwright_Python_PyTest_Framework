from Pages.BasePage import BasePage

class LogoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.click_logout = 'text=Log out'
        self.login_button = "//a[normalize-space()='Log in']"

    def logout(self):
        self.click(self.click_logout)

    def verify_logout(self):
        return self.page.locator(self.login_button)