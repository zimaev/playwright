from pages.BasePage import BasePage
from pages.CartPage.CartPageLocators import CartPageLocator
from playwright.sync_api import expect


class CartPage(BasePage):

    def click_proceed_check_out(self):
        self.click(CartPageLocator.PROCEED_TO_CHECKOUT)

    def assert_count_product_items(self, count):
        expect(self.page.locator(CartPageLocator.QUANTITY)).to_have_text(str(count))



