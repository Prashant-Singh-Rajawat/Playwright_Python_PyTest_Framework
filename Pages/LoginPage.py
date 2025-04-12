from Pages.BasePage import BasePage
from Utilities.config import USERNAME, PASSWORD

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_link = 'text=Log in'
        self.login_field = '#Email'
        self.password_field = '#Password'
        self.login_button = "input[value='Log in']"
        self.logout_link = 'text=Log out'

    def click_login(self):
        self.click(self.login_link)

    def enter_credentials(self):
        self.fill(self.login_field,USERNAME)
        self.fill(self.password_field,PASSWORD)
        self.click(self.login_button)

    def verify_login(self):
        return self.page.locator(self.logout_link)