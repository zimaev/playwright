from pages.MainPage.MainPage import ShopPage
from pages.ContactUsPage.ContactUsPage import ContactUsPage
import allure
from helpers.contact_us_message import Message
from pages.CartPage.CartPage import CartPage


@allure.epic('Общие тесты')
@allure.suite('Общие тесты')
class TestCommon:

    @allure.title("Test Case 6: Форма обратной связи")
    def test_contact_us_form(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите на кнопку "Связаться с нами"
        5. Убедитесь, что "ВОЙТИ В КОНТАКТ" виден
        6. Введите имя, адрес электронной почты, тему и сообщение
        7. Загрузить файл
        8. Нажмите кнопку "Отправить"
        9. Нажмите кнопку OK
        10. Проверьте сообщение об успехе "Успех! Ваши данные были успешно отправлены.
        11. Нажмите кнопку "Домой" и убедитесь, что вы успешно попали на домашнюю страницу
        """
        shop, contact_us = ShopPage(driver), ContactUsPage(driver)
        msg = Message()

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы формы для обратной связи'):
            shop.open_contact_us_page()
        with allure.step(f'На странице отображается сообщение GET IN TOUCH'):
            contact_us.visible_form()
        with allure.step(f'Заполнение формы обратной связи'):
            contact_us.fill_form(msg)
        with allure.step(f'ASSERT'):
            contact_us.visible_success_message()

    @allure.title("Test Case 7: Страница проверки тестовых случаев")
    def test_case_us_form(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите на кнопку "Test Cases"
        5. Убедитесь, что пользователь успешно перешел на страницу test cases
        """
        shop, contact_us = ShopPage(driver), ContactUsPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы тест-кейсов'):
            shop.open_test_cases_page()

    @allure.title("Test Case 10: Проверка подписки на домашней странице")
    def test_verify_subscription_in_home_page(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Прокрутите вниз до нижнего колонтитула
        5. Проверьте текст "ПОДПИСКА"
        6. Введите адрес электронной почты в поле ввода и нажмите кнопку со стрелкой
        7. Проверка успеха сообщение "Вы успешно подписаны!" отображается
        """
        shop = ShopPage(driver)
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Ввод email в поле ввода и нажатие кнопки со стрелкой'):
            shop.subscribe()
        with allure.step(f'Проверка появления сообщение Вы успешно подписаны'):
            shop.successfully_subscribed_message()

    @allure.title("Test Case 11: Проверка подписки на странице корзины")
    def test_verify_subscription_in_card_page(self, driver):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите кнопку "Корзина".
        5. Прокрутите вниз до нижнего колонтитула
        6. Проверьте текст "ПОДПИСКА".
        7. Введите адрес электронной почты в поле ввода и нажмите кнопку со стрелкой
        8. Проверка успеха отображается сообщение "Вы успешно подписались!"
        """
        shop, view_cart = ShopPage(driver), CartPage(driver)
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте  страницe корзины'):
            shop.open_cart()
        with allure.step(f'Ввод email в поле ввода и нажатие кнопки со стрелкой'):
            shop.subscribe()
        with allure.step(f'Проверка появления сообщение Вы успешно подписаны'):
            shop.successfully_subscribed_message()






