class BasePage:
    def __init__(self,page):
        self.page = page

    def fill(self,locator,value):
        field = self.page.locator(locator)
        field.clear()
        field.fill(value)

    def click(self, locator):
        self.page.locator(locator).click()

    def drop_down(self,locator, value):
        self.page.locator(locator).select_option(value)

    def hover(self,locator):
        self.page.locator(locator).hover()

    def scroll_down(self,locator):
        self.page.locator(locator).scroll_into_view_if_needed()