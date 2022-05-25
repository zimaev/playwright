from playwright.sync_api import Page, expect
from pages.BasePage import BasePage
from helpers.user import User


class ShopPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.login = self.page.locator("text=Signup / Login")

    def open_login_page(self):
        self.login.click()

    def account_logged(self, first_name):
        expect(self.page.locator('li:nth-child(9) > a')).to_contain_text(f'Logged in as {first_name}')

    def logout(self):
        self.click('li:nth-child(4) > a')


