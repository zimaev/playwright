import allure
from pages.MainPage.MainPage import ShopPage
from pages.ProductsPage.ProductsPage import ProductsPage
from pages.ProductDetailsPage.ProductDetailsPage import ProductsDetailsPage
from api.BrandAPI import BrandAPI
import pytest
import random
from helpers.contact_us_message import Message
from pages.LoginPage.LoginPage import LoginPage


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
        """
        shop, products, products_detail = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver)

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
    def test_search_product_category(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что категории видны на левой боковой панели
        4. Нажмите на категорию "Женщины".
        5. Нажмите на любую ссылку категории в разделе "Женщины", например: Платье
        6. Убедитесь, что отображается страница категории, и подтвердите текст "ЖЕНСКИЕ ТОПЫ".
        7. На левой боковой панели нажмите на любую ссылку подкатегории категории "Мужчины".
        8. Убедитесь, что пользователь перешел на эту страницу категории

        """
        shop, products, products_detail = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы всех продуктов'):
            shop.open_products_page()
        with allure.step(f'Список всех товаров виден'):
            products.all_products_visible()
            # driver.pause()
        with allure.step(f'Выбор категории товара'):
            products.select_category("Men")
        with allure.step(f'Выбор категории товара'):
            products.select_sub_category("TSHIRTS")



    @allure.title("Test Case 20: Поиск товаров и проверка корзины после входа в систему")
    def test_search_product_after_system(self, driver, fake_user, user_api):
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
        """
        shop, products, products_detail, login_page = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver), LoginPage(driver)

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
        with allure.step(f'Добавление первого продукта в корзину'):
            products.add_product_to_card('Frozen Tops For Kids')
        with allure.step(f'Всплывающее окно  отобразилось'):
            products.modal_window_visible()
        with allure.step(f'Клик на кнопку View Cart'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Заполнение полей авторизации пользователя корретными данными '):
            login_page.login_to_account(fake_user)
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)
        with allure.step(f'Открыте страницу корзины'):
            shop.open_cart()

    @allure.title("Test Case 21: Добавление отзыва о продукте")
    def test_add_review_on_product(self, driver, fake_user):
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
        """
        shop, products, products_detail = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver)
        msg = Message()
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
        with allure.step(f'Информация о продукте отображается'):
            products_detail.product_info_visible()
        with allure.step(f'Заполнение и отправка отзыва о товаре'):
            products_detail.add_review(msg)
        with allure.step(f'Заполнение и отправка отзыва о товаре'):
            products_detail.success_subscribe_message_visible()

    # @pytest.mark.xfail(reason='Не продуман механзм передачи имени бренда из выбора в проверку')
    @allure.title("Test Case 19: Просмотр и корзина продуктов бренда")
    def test_view_and_cart_brand_products(self,driver ):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Нажмите на кнопку "Продукты".
        4. Убедитесь, что бренды видны на левой боковой панели
        5. Нажмите на любое фирменное наименование
        6. Убедитесь, что пользователь переходит на страницу бренда и отображаются продукты бренда
        7. На левой боковой панели нажмите на любую другую ссылку бренда
        8. Убедитесь, что пользователь перешел на эту страницу бренда и может видеть товары
        """
        shop, products, products_detail = ShopPage(driver), ProductsPage(driver), ProductsDetailsPage(driver)

        brand = list(BrandAPI.get_brand_list())

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы всех продуктов'):
            shop.open_products_page()
        with allure.step(f'Список всех товаров виден'):
            products.all_products_visible()
        with allure.step(f'Список брендов отображается'):
            products.brand_list_visible()
        with allure.step(f'Выбор бренда для отображения в списке'):
            products.select_brand(brand[0])
        with allure.step(f'Бренд тображения в списке'):
            products.brand_products_visible(brand[0])
        with allure.step(f'Выбор бренда для отображения в списке'):
            products.select_brand(brand[1])
        with allure.step(f'Бренд тображения в списке'):
            products.brand_products_visible(brand[1])



