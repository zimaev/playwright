from playwright.sync_api import Page, expect
from pages.BasePage import BasePage
import allure
from pages.ProductDetailsPage.ProductsDetailsPageLocators import ProductsDetailsPageLocators


class ProductsDetailsPage(BasePage):

    def product_info_visible(self):
        with allure.step(f'Имя продукта отображается'):
            expect(self.page.locator(ProductsDetailsPageLocators.PRODUCT_NAME)).to_be_visible()
        with allure.step(f'Категория продукта отображается'):
            expect(self.page.locator(ProductsDetailsPageLocators.CATEGORY)).to_be_visible()
        with allure.step(f'Цена продукта отображается'):
            expect(self.page.locator(ProductsDetailsPageLocators.PRICE)).to_be_visible()
        with allure.step(f'Доступность продукта отображается'):
            expect(self.page.locator(ProductsDetailsPageLocators.AVAILABILITY)).to_be_visible()
        with allure.step(f'Состояние продукта отображается'):
            expect(self.page.locator(ProductsDetailsPageLocators.CONDITION)).to_be_visible()
        with allure.step(f'Бренд продукта отображается'):
            expect(self.page.locator(ProductsDetailsPageLocators.BRAND)).to_be_visible()

    def set_product_count(self, count):
        self.page.locator("input[name=\"quantity\"]").click()
        self.page.locator("input[name=\"quantity\"]").fill(count)

    def click_add_to_card(self):
        self.click('.btn.btn-default.cart')

    def add_review(self, msg ):
        self.type(ProductsDetailsPageLocators.NAME, msg.name)
        self.type(ProductsDetailsPageLocators.EMAIL, msg.email)
        self.type(ProductsDetailsPageLocators.TEXT, msg.message)
        self.click(ProductsDetailsPageLocators.SUBMIT)

    def success_subscribe_message_visible(self):
        expect(self.page.locator(ProductsDetailsPageLocators.ALERT_SUCCESS)).to_be_visible()
        expect(self.page.locator(ProductsDetailsPageLocators.ALERT_SUCCESS)).to_have_text('Thank you for your review.')








