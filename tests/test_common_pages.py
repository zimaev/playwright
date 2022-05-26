from pages.MainPage import ShopPage
from pages.ContactUsPage.ContactUsPage import ContactUsPage
import allure
from helpers.contact_us_message import Message


@allure.epic('Общие тесты')
@allure.suite('Общие тесты')
class TestCommon(object):

    @allure.title("Test Case 6: Форма обратной связи")
    def test_contact_us_form(self, driver):
        shop, contact_us = ShopPage(driver), ContactUsPage(driver)
        msg = Message()
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы формы для обратной связи'):
            shop.open_contact_us_page()
        with allure.step(f'На  отображается сообщение GET IN TOUCH'):
            contact_us.visible_form()
        with allure.step(f'Заполнение формы обратной связи'):
            contact_us.fill_form(msg)
        with allure.step(f'ASSERT'):
            contact_us.visible_success_message()

    @allure.title("Test Case 7: Страница проверки тестовых случаев")
    def test_contact_us_form(self, driver):
        shop, contact_us = ShopPage(driver), ContactUsPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте страницы тест-кейсов'):
            shop.open_test_cases_page()



