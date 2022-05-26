import allure
import pytest

from pages.MainPage.MainPage import ShopPage
from pages.ProductsPage.ProductsPage import ProductsPage


@allure.epic('Тесты корзины')
@allure.suite('Тесты корзины')
class TestCart(object):

    def test_add_product_in_card(self, driver):
        shop, products = ShopPage(driver), ProductsPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы всех продуктов'):
            shop.open_products_page()
        with allure.step(f'Список всех товаров виден'):
            products.all_products_visible()

        products.add_product_to_card(1)
        products.modal_window_visible()
        driver.locator("text=Continue Shopping").click()
        products.modal_window_not_visible()
        products.add_product_to_card(2)
        driver.locator("text=Continue Shopping").click()
        products.modal_window_not_visible()
        products.add_product_to_card(3)
        driver.locator("text=Continue Shopping").click()
        products.modal_window_not_visible()
        products.add_product_to_card(4)
        driver.locator("text=Continue Shopping").click()
        products.modal_window_not_visible()
        # driver.locator("text=Continue Shopping").click()


