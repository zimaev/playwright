from pages.BasePage import BasePage
from pages.CartPage.CheckoutPage.CheckoutPageLocators import CheckoutPageLocators

class CheckoutPage(BasePage):

    def click_place_order(self):
        self.click(CheckoutPageLocators.PLACE_ORDER)

    def fill_comment_to_order(self):
        self.type(CheckoutPageLocators.TEXT_AREA, 'Lorem')



