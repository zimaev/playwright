from pages.BasePage import BasePage
from pages.CartPage.PaymentPage.PaymentPageLocators import PaymentPageLocators


class PaymentPage(BasePage):

    def fill_card_details(self):
        self.type(PaymentPageLocators.NAME_CARD, 'Name')
        self.type(PaymentPageLocators.NUMBER_CARD, '123456789')
        self.type(PaymentPageLocators.CVC, '311')
        self.type(PaymentPageLocators.MM, '01')
        self.type(PaymentPageLocators.YYYY, '2023')

    def click_pay_and_confirm_order(self):
        self.click(PaymentPageLocators.PAY_BUTTON)








