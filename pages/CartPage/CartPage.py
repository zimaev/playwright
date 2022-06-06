from pages.BasePage import BasePage
from pages.CartPage.CartPageLocators import CartPageLocator
from playwright.sync_api import expect


class CartPage(BasePage):

    def click_proceed_check_out(self):
        self.click(CartPageLocator.PROCEED_TO_CHECKOUT)

    def assert_count_product_items(self, product, count):
        expect(self.page.locator(f'#product-{product} {CartPageLocator.QUANTITY}')).to_have_text(str(count))

    def assert_price_product_items(self, product, price):
        expect(self.page.locator(f'#product-{product} {CartPageLocator.PRICE}')).to_have_text(str(price))

    def assert_total_price_product_items(self, product, total_price):
        expect(self.page.locator(f'#product-{product} {CartPageLocator.TOTAL_PRICE}')).to_have_text(str(total_price))

    def delete_product(self, number):
        self.click(f'#product-{number} .cart_delete')

    def assert_product_deleted(self, number):
        expect(self.page.locator(f'#product-{number}')).not_to_be_visible()







