from playwright.sync_api import Page, expect
from pages.BasePage import BasePage
from helpers.user import User


class ShopPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.login = self.page.locator("text=Signup / Login")
        self.contact_us = self.page.locator("text=Contact us")
        self.test_cases = self.page.locator('header', has_text='Test Cases')

    def open_login_page(self):
        self.login.click()

    def open_contact_us_page(self):
        self.contact_us.click()

    def open_test_cases_page(self):
        self.test_cases.click()

    def account_logged(self, first_name):
        expect(self.page.locator('li:nth-child(9) > a')).to_contain_text(f'Logged in as {first_name}')

    def logout(self):
        self.click('li:nth-child(4) > a')


