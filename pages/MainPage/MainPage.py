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

    def open_cart(self):
        self.click(MainPageLocators.CART)

    def account_logged(self, first_name):
        expect(self.page.locator('li:nth-child(9) > a')).to_have_text(f'Logged in as {first_name}')

    def logout(self):
        self.click('li:nth-child(4) > a')

    def add_product_to_card(self, number):
        self.hover(f'div .productinfo.text-center  >> nth={number - 1}')
        self.click(f'[class=overlay-content ] [data-product-id="{number}"]')

    def modal_window_visible(self):
        expect(self.page.locator('.modal-content')).to_be_visible()

    def modal_window_not_visible(self):
        expect(self.page.locator('.modal-content')).not_to_be_visible()

    def subscribe(self):
        # self.page.locator(MainPageLocators.SUBSCRIBE)
        self.type(MainPageLocators.SUBSCRIBE, 'admin@example.com')
        self.click(MainPageLocators.SUBSCRIBE_BUTTON)

    def successfully_subscribed_message(self):
        expect(self.page.locator(MainPageLocators.SUCCESS)).to_be_visible()
        expect(self.page.locator(MainPageLocators.SUCCESS)).to_have_text('You have been successfully subscribed!')




