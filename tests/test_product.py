import allure
from pages.MainPage.MainPage import ShopPage
from pages.ProductsPage.ProductsPage import ProductsPage
from pages.ProductDetailsPage.ProductDetailsPage import ProductsDetailsPage
import pytest


@allure.epic('')
@allure.suite('')
class TestProduct(object):

    @allure.title("Test Case 8: Проверка отображения всех продуктов и страницы сведений о продукте")
    def test_verify_all_products_and_product_detail_page(self, driver):
        shop, products, products_detail  = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver)
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы всех продуктов'):
            shop.open_products_page()
        with allure.step(f'Список всех товаров виден'):
            products.all_products_visible()
        with allure.step(f'Открыть страницу товара'):
            products.open_product(number=1)
        with allure.step(f'Информация о продукте отображается'):
            products_detail.product_info_visible()

    @allure.title("Test Case 9: Поиск продукта")
    def test_search_product(self, driver):

        shop, products, products_detail = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver)
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы всех продуктов'):
            shop.open_products_page()
        with allure.step(f'Список всех товаров виден'):
            products.all_products_visible()
        with allure.step(f'Поиск товара по имени'):
            products.search_field('Frozen Tops For Kids')
        with allure.step(f'Искомый товар отображается на странице'):
            products.searched_products_visible('Frozen Tops For Kids')

