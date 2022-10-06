from pages.MainPage.MainPage import ShopPage
from pages.ContactUsPage.ContactUsPage import ContactUsPage
import allure
from helpers.contact_us_message import Message


@allure.epic('Общие тесты')
@allure.suite('Общие тесты')
class TestCommon:

    @allure.title("Test Case 6: Форма обратной связи")
    def test_contact_us_form(self, driver):

        msg = Message()

        with allure.step(f'Открыте стартовой страницы магазина'):
            ShopPage(driver).open_site()
        with allure.step(f'Открыте страницы формы для обратной связи'):
            ShopPage(driver).open_contact_us_page()
        with allure.step(f'На странице отображается сообщение GET IN TOUCH'):
            ContactUsPage(driver).visible_form()
        with allure.step(f'Заполнение формы обратной связи'):
            ContactUsPage(driver).fill_form(msg)
        with allure.step(f'ASSERT'):
            ContactUsPage(driver).visible_success_message()

    @allure.title("Test Case 7: Страница проверки тестовых случаев")
    def test_case_page(self, driver):

        with allure.step(f'Открыте стартовой страницы магазина'):
            ShopPage(driver).open_site()
        with allure.step(f'Открыте страницы тест-кейсов'):
            ShopPage(driver).open_test_cases_page()

    @allure.title("Test Case 10: Проверка подписки на домашней странице")
    def test_verify_subscription_in_home_page(self, driver):

        with allure.step(f'Открыте стартовой страницы магазина'):
            ShopPage(driver).open_site()
        with allure.step(f'Ввод email в поле ввода и нажатие кнопки со стрелкой'):
            ShopPage(driver).subscribe()
        with allure.step(f'Проверка появления сообщение Вы успешно подписаны'):
            ShopPage(driver).successfully_subscribed_message()

    @allure.title("Test Case 11: Проверка подписки на странице корзины")
    def test_verify_subscription_in_card_page(self, driver):

        with allure.step(f'Открыте стартовой страницы магазина'):
            ShopPage(driver).open_site()
        with allure.step(f'Открыте  страницe корзины'):
            ShopPage(driver).open_cart()
        with allure.step(f'Ввод email в поле ввода и нажатие кнопки со стрелкой'):
            ShopPage(driver).subscribe()
        with allure.step(f'Проверка появления сообщение Вы успешно подписаны'):
            ShopPage(driver).successfully_subscribed_message()






