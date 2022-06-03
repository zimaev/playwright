from pages.BasePage import BasePage
from pages.CartPage.CheckoutPage.CheckoutPageLocators import CheckoutPageLocators
from playwright.sync_api import expect
import random


class CheckoutPage(BasePage):

    def click_place_order(self):
        self.click(CheckoutPageLocators.PLACE_ORDER)

    def fill_comment_to_order(self):
        self.type(CheckoutPageLocators.TEXT_AREA, 'Lorem')

    def assert_billing_address(self, user):
        expect(self.page.locator(CheckoutPageLocators.BILLING_FIRST_NAME)).to_contain_text(f'{user.first_name} {user.last_name}')
        expect(self.page.locator(CheckoutPageLocators.BILLING_COMPANY)).to_have_text(user.company)
        expect(self.page.locator(CheckoutPageLocators.BILLING_PHONE)).to_have_text(user.mobile_number)
        expect(self.page.locator(CheckoutPageLocators.BILLING_COUNTY)).to_have_text(user.country)

    def assert_delivery_address(self, user):
        expect(self.page.locator(CheckoutPageLocators.DELIVERY_FIRST_NAME)).to_contain_text(f'{user.first_name} {user.last_name}')
        expect(self.page.locator(CheckoutPageLocators.BILLING_COMPANY)).to_have_text(user.company)
        expect(self.page.locator(CheckoutPageLocators.DELIVERY_PHONE)).to_have_text(user.mobile_number)
        expect(self.page.locator(CheckoutPageLocators.DELIVERY_COUNTY)).to_have_text(user.country)



