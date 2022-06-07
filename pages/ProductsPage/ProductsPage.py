from playwright.sync_api import Page, expect
from pages.BasePage import BasePage
from pages.ProductsPage.ProductsPageLocators import ProductsPageLocators
from api.ProductAPI import ProductAPI
import random


class ProductsPage(BasePage):

    def all_products_visible(self):
        expect(self.page.locator(ProductsPageLocators.FEATURES_ITEMS)).to_be_visible()

    def brand_list_visible(self):
        expect(self.page.locator(ProductsPageLocators.BRAND_LIST)).to_be_visible()

    def add_product_to_card(self, name):
        if isinstance(name, str):
            number = ProductAPI.search_product(name).json()['products']
            self.hover(f"[class='productinfo text-center'] [data-product-id='{number[0]['id']}']")
            self.click(f"[class=overlay-content ] [data-product-id='{number[0]['id']}']")
        if isinstance(name, int):
            product_list = ProductAPI.get_product_list().json()['products']
            self.hover(f'div .productinfo.text-center p:has-text("{product_list[name - 1]["name"]}")')
            self.click(f'[class=overlay-content ] [data-product-id="{name}"]')

    def open_product(self, number):
        self.click(f".nav.nav-pills.nav-justified >> nth={number - 1}")

    def select_brand(self, brand):
        self.click(f'text={brand}')

    def select_category(self, category):
        self.click(f'[href="#{category}"]')

    def select_sub_category(self, sub_category):
        self.click(f'a >> text={sub_category}')

    def continue_shopping(self, ):
        self.click('text=Continue Shopping')

    def search_field(self, name):
        self.click('#search_product')
        self.type('#search_product', name)
        self.click('#submit_search')

    def searched_products_visible(self, name):
        expect(self.page.locator('.overlay-content p')).to_contain_text(name)

    def brand_products_visible(self, name):
        expect(self.page.locator('.title.text-center')).to_have_text(f'Brand - {name} Products')

    def modal_window_visible(self):
        expect(self.page.locator('div.modal-content')).to_be_visible()

    def modal_window_not_visible(self):
        expect(self.page.locator('div.modal-content')).not_to_be_visible()







