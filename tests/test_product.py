import allure
from pages.MainPage.MainPage import ShopPage
from pages.ProductsPage.ProductsPage import ProductsPage
from pages.ProductDetailsPage.ProductDetailsPage import ProductsDetailsPage
import pytest


@allure.epic('Тесты на товары')
@allure.suite('Тесты на товары')
class TestProduct:

    @allure.title("Test Case 8: Проверка отображения всех продуктов и страницы сведений о продукте")
    def test_verify_all_products_and_product_detail_page(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите на кнопку "Продукты"
        5. Убедитесь, что пользователь успешно перешел на страницу ВСЕХ ПРОДУКТОВ
        6. Список продуктов виден
        7. Нажмите "Просмотреть продукт" первого продукта
        8. Пользователь попадает на страницу сведений о продукте
        9. Убедитесь, что видны детали: название продукта, категория, цена, доступность, состояние, бренд
        :param driver:
        :return:
        """
        shop, products, products_detail = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver)
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
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите на кнопку "Продукты"
        5. Убедитесь, что пользователь успешно перешел на страницу ВСЕХ ПРОДУКТОВ
        6. Введите название продукта в поле ввода поиска и нажмите кнопку поиска
        7. Убедитесь, что "ИСКОМЫЕ ПРОДУКТЫ" видны
        8. Убедитесь, что все продукты, связанные с поиском, видны
        :param driver:
        :return:
        """

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

    @allure.title("Test Case 18: Просмотр продуктов категории")
    def test_search_product(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что категории видны на левой боковой панели
        4. Нажмите на категорию "Женщины".
        5. Нажмите на любую ссылку категории в разделе "Женщины", например: Платье
        6. Убедитесь, что отображается страница категории, и подтвердите текст "ЖЕНСКИЕ ТОПЫ".
        7. На левой боковой панели нажмите на любую ссылку подкатегории категории "Мужчины".
        8. Убедитесь, что пользователь перешел на эту страницу категории
        :param driver:
        :return:
        """
        pass

    @allure.title("Test Case 20: Поиск товаров и проверка корзины после входа в систему")
    def test_search_product(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Нажмите на кнопку "Продукты".
        4. Убедитесь, что пользователь успешно перешел на страницу "ВСЕ ПРОДУКТЫ".
        5. Введите название продукта в поле ввода поиска и нажмите кнопку поиска
        6. Убедитесь, что "ИСКОМЫЕ ПРОДУКТЫ" видны.
        7. Убедитесь, что все продукты, связанные с поиском, видны
        8. Добавьте эти товары в корзину
        9. Нажмите кнопку "Корзина" и убедитесь, что товары видны в корзине
        10. Нажмите кнопку "Регистрация / Вход" и отправьте регистрационные данные
        11. Снова перейдите на страницу Корзины
        12. Убедитесь, что эти продукты также видны в корзине после входа в систему
        :param driver:
        :return:
        """
        pass

    @allure.title("Test Case 21: Добавление отзыва о продукте")
    def test_search_product(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Нажмите на кнопку "Продукты".
        4. Убедитесь, что пользователь успешно перешел на страницу "ВСЕ ПРОДУКТЫ".
        5. Нажмите на кнопку "Просмотреть продукт".
        6. Убедитесь, что надпись "Написать отзыв" видна.
        7. Введите имя, адрес электронной почты и отзыв
        8. Нажмите кнопку "Отправить"
        9. Проверьте сообщение об успехе "Спасибо за ваш отзыв".
        :param driver:
        :return:
        """
        pass

