from playwright.sync_api import Page, expect
from pages.BasePage import BasePage
from pages.ProductsPage.ProductsPageLocators import ProductsPageLocators


class ProductsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.features_items = page.locator('.features_items')
        self.view_product = page.locator('.nav.nav-pills.nav-justified')

    def all_products_visible(self):
        expect(self.features_items).to_be_visible()

    def brand_list_visible(self):
        expect(self.page.locator(ProductsPageLocators.BRAND_LIST)).to_be_visible()
        self.attach_screenshot(ProductsPageLocators.BRAND_LIST, 'brand_list_visible')

    def add_product_to_card(self, number):
        self.hover(f'div .productinfo.text-center  >> nth={number - 1}')
        self.click(f'[class=overlay-content ] [data-product-id="{number}"]')

    def open_product(self, number):
        self.click(f".nav.nav-pills.nav-justified >> nth={number - 1}")

    def select_brand(self, brand):
        self.click(f'text={brand}')

    def select_category(self, category):
        self.click(f'#{category}')

    def search_field(self, name):
        self.click('#search_product')
        self.type('#search_product', name)
        self.click('#submit_search')

    def searched_products_visible(self, name):
        expect(self.page.locator('.overlay-content p')).to_contain_text(name)
        self.attach_screenshot('.overlay-content p', 'searched_products_visible')

    def brand_products_visible(self, name):
        expect(self.page.locator('.title.text-center')).to_have_text(f'Brand -{name} Products')
        self.attach_screenshot('.title.text-center', 'brand_products_visible')

    def modal_window_visible(self):
        expect(self.page.locator('.modal-content')).to_be_visible()
        self.attach_screenshot('.modal-content', 'modal_window_visible')

    def modal_window_not_visible(self):
        expect(self.page.locator('.modal-content')).not_to_be_visible()







