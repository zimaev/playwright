from playwright.sync_api import expect
from pages.BasePage import BasePage
from pages.MainPage.MainPageLocators import MainPageLocators


class ShopPage(BasePage):

    def open_login_page(self):
        self.click(MainPageLocators.LOGIN)

    def open_contact_us_page(self):
        self.click(MainPageLocators.CONTACT_US)


    def open_test_cases_page(self):

        self.click(MainPageLocators.TEST_CASES)

    def open_products_page(self):
        self.click(MainPageLocators.PRODUCTS)

    def account_logged(self, first_name):
        expect(self.page.locator('li:nth-child(9) > a')).to_have_text(f'Logged in as {first_name}')

    def logout(self):
        self.click('li:nth-child(4) > a')


