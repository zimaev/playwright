import allure
import pytest

from pages.CartPage.CartPage import CartPage
from pages.MainPage.MainPage import ShopPage
from pages.ProductsPage.ProductsPage import ProductsPage
from pages.ProductDetailsPage.ProductDetailsPage import ProductsDetailsPage


@allure.epic('Тесты корзины')
@allure.suite('Тесты корзины')
class TestCart:

    @allure.title('Test Case 12: Добавление товара в корзину')
    @pytest.mark.flaky(reruns=2)
    def test_add_product_in_card(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com'
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите кнопку "Продукты"
        5. Наведите курсор на первый продукт и нажмите "Добавить в корзину"
        6. Нажмите кнопку "Продолжить покупки"
        7. Наведите курсор на второй продукт и нажмите "Добавить в корзину"
        8. Нажмите кнопку "Просмотреть корзину"
        9. Убедитесь, что оба продукта добавлены в корзину
        10. Проверьте их цены, количество и общую цену
        """
        shop, products, cart = ShopPage(driver), ProductsPage(driver), CartPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы всех продуктов'):
            shop.open_products_page()
        with allure.step(f'Список всех товаров виден'):
            products.all_products_visible()
        with allure.step(f'Добавление первого продукта в корзину'):
            products.add_product_to_card(1)
        with allure.step(f'Всплывающее окно после отобразилось'):
            products.modal_window_visible()
        with allure.step(f'Склик на кнопку Continue Shopping'):
            products.continue_shopping()
        with allure.step(f'Всплывающее окно исчезло'):
            products.modal_window_not_visible()
        with allure.step(f'Добавление второго продукта в корзину'):
            products.add_product_to_card(2)
        with allure.step(f'Всплывающее окно после отобразилось'):
            products.modal_window_visible()
        with allure.step(f'Склик на кнопку Continue Shopping'):
            products.continue_shopping()
        with allure.step(f'Всплывающее окно исчезло'):
            products.modal_window_not_visible()
        with allure.step(f'Добавление третьего продукта в корзину'):
            products.add_product_to_card(3)
        with allure.step(f'Всплывающее окно отобразилось'):
            products.modal_window_visible()
        with allure.step(f'Клик на кнопку View Cart'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'Проверка количества каждой товарной позиции'):
            cart.assert_count_product_items(product=1, count=1)
            cart.assert_count_product_items(product=2, count=1)
            cart.assert_count_product_items(product=3, count=1)
        with allure.step(f'Проверка цены каждой товарной позиции'):
            cart.assert_price_product_items(product=1, price='Rs. 500')
            cart.assert_price_product_items(product=2, price='Rs. 400')
            cart.assert_price_product_items(product=3, price='Rs. 1000')
        with allure.step(f'Проверка итоговой цены каждой товарной позиции'):
            cart.assert_price_product_items(product=1, price='Rs. 500')
            cart.assert_price_product_items(product=2, price='Rs. 400')
            cart.assert_price_product_items(product=3, price='Rs. 1000')

    @allure.title('Test Case 13: Проверка количества товара в корзине')
    def test_verify_product_quantity_in_cart(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите "Просмотреть продукт" для любого продукта на домашней странице
        5. Проверьте, что деталь продукта открыта
        6. Увеличьте количество до 4
        7. Нажмите кнопку "Добавить в корзину"
        8. Нажмите кнопку "Просмотреть корзину"
        9. Убедитесь, что продукт отображается на странице корзины с точным количеством
        """
        shop, products, products_detail, view_cart = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver), CartPage(driver)
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы всех продуктов'):
            shop.open_products_page()
        with allure.step(f'Список всех товаров виден'):
            products.all_products_visible()
        with allure.step(f'Открыть страницу товара'):
            products.open_product(1)
        with allure.step(f'Информация о продукте отображается'):
            products_detail.product_info_visible()
        with allure.step(f'Увеличьте количество до 4'):
            products_detail.set_product_count("4")
        with allure.step(f'Добавление продукта в корзину'):
            products_detail.click_add_to_card()
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Клик на кнопку View Cart'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'продукт отображается на странице корзины с точным количеством'):
            view_cart.assert_count_product_items(product=1, count=4)

    @allure.title('Test Case 17: Удаление товаров из корзины')
    def test_remove_products_from_cart(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Добавить товары в корзину
        5. Нажмите кнопку "Корзина"
        6. Убедитесь, что отображается страница корзины
        7. Нажмите кнопку "X", соответствующую конкретному продукту
        8. Убедитесь, что товар удален из корзины

        """
        shop, products, products_detail, view_cart = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(
            driver), CartPage(driver)
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Добавить товары в корзину'):
            shop.add_product_to_card(1)
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Склик на кнопку Continue Shopping'):
            driver.locator("text=Continue Shopping").click()
        with allure.step(f'Добавить товары в корзину'):
            shop.add_product_to_card(7)
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Клик на кнопку View Cart'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'Клик на кнопку удаления товара'):
            view_cart.delete_product(7)
        with allure.step(f'Товар не отображается в корзине'):
            view_cart.assert_product_deleted(7)

    @allure.title('Test Case 22: Добавить в корзину из рекомендуемых товаров')
    def test_add_to_cart_from_recommended_items(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Прокрутите страницу вниз.
        4. Убедитесь, что "РЕКОМЕНДУЕМЫЕ ТОВАРЫ" видны.
        5. Нажмите на кнопку "Добавить в корзину" на рекомендуемом товаре.
        6. Нажмите на кнопку "Просмотреть корзину".
        7. Убедитесь, что товар отображается на странице корзины
        """
        shop, products, products_detail, view_cart = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(
            driver), CartPage(driver)
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Добавить товары в корзину'):
            shop.add_product_to_card(1)
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Склик на кнопку Continue Shopping'):
            driver.locator("text=Continue Shopping").click()
        with allure.step(f'Добавить товары в корзину'):
            shop.add_product_to_card(2)
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Клик на кнопку View Cart'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'Проверка количества каждой товарной позиции'):
            view_cart.assert_count_product_items(product=1, count=1)
        with allure.step(f'Проверка цены каждой товарной позиции'):
            view_cart.assert_price_product_items(product=1, price='Rs. 500')

