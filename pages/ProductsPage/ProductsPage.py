from playwright.sync_api import Page, expect
from pages.BasePage import BasePage


class ProductsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.features_items = page.locator('.features_items')
        self.view_product = page.locator('.nav.nav-pills.nav-justified')

    def all_products_visible(self):
        expect(self.features_items).to_be_visible()

    def add_product_to_card(self, number):
        self.hover(f'div .productinfo.text-center  >> nth={number - 1}')
        self.page.pause()
        self.click(f'.overlay-content .btn.btn-default.add-to-cart nth={number - 1}')

    def open_product(self, number):
        self.click(f".nav.nav-pills.nav-justified >> nth={number - 1}")

    def search_field(self, name):
        self.click('#search_product')
        self.type('#search_product', name)
        self.click('#submit_search')

    def searched_products_visible(self, name):
        expect(self.page.locator('.overlay-content p')).to_contain_text(name)

    def modal_window_visible(self):
        expect(self.page.locator('.modal-content')).to_be_visible()

    def modal_window_not_visible(self):
        expect(self.page.locator('.modal-content')).not_to_be_visible()





