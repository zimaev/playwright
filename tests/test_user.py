from pages.MainPage.MainPage import ShopPage
from pages.LoginPage.LoginPage import LoginPage
from pages.SignupPage.SignupPage import SignupPage
from pages.SignupPage.AccountCreatedPage import AccountCreatedPage
import allure


@allure.epic('Тесты регистрации/авторизации пользователя входа/выхода из системы')
@allure.suite('Тесты регистрации/авторизации пользователя входа/выхода из системы')
class TestUser(object):

    @allure.title("Test Case 1: Регистрация пользователя")
    def test_register_user(self, driver, fake_user):

        with allure.step(f'Открыте стартовой страницы магазина'):
            ShopPage(driver).open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            ShopPage(driver).open_login_page()
        with allure.step(f'Ввод имени и email в форму создания нового пользователя'):
            LoginPage(driver).create_new_user(fake_user)
        with allure.step(f'Заполнение полей регистрации нового пользователя '):
            SignupPage(driver).enter_account_information(fake_user)
        with allure.step(f'Открылась страница поздравления о созданном аккаунте'):
            AccountCreatedPage(driver).account_created_message()
        with allure.step(f'Нажать кнопку Сontinue'):
            AccountCreatedPage(driver).click_continue()
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            ShopPage(driver).account_logged(fake_user.first_name)

    @allure.title("Test Case 2: Авторизация пользователя с корректными учетными данными")
    def test_login_user_with_correct_user_password(self, driver, fake_user, user_api):

        with allure.step(f'Открыте стартовой страницы магазина'):
            ShopPage(driver).open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            ShopPage(driver).open_login_page()
        with allure.step(f'Заполнение полей авторизации пользователя корретными данными '):
            LoginPage(driver).login_to_account(fake_user)
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            ShopPage(driver).account_logged(fake_user.first_name)

    @allure.title("Test Case 3: Авторизация пользователя с некорректными данными")
    def test_login_with_incorrect_email_password(self, driver, fake_user):

        login_page, shop, signup_page = LoginPage(driver), ShopPage(driver), SignupPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Заполнение полей авторизации пользователя  некорретными данными'):
            login_page.login_to_account(fake_user)
        with allure.step(f'Появилось сообщение о некорректном email или пароле'):
            login_page.login_error_message()

    @allure.title("Test Case 4: Выход пользователя из системы")
    def test_logout_user(self, driver, fake_user, user_api):

        login_page, shop, signup_page = LoginPage(driver), ShopPage(driver), SignupPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Заполнение полей авторизации пользователя некорретными данными '):
            login_page.login_to_account(fake_user)
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)
        with allure.step(f'Выход из системы'):
            shop.logout()

    @allure.title("Test Case 5: Регистрация нового пользователя с существущими в системе учетными данными")
    def test_login_user_with_alredy_email_address(self, driver, fake_user, user_api):

        login_page, shop, signup_page = LoginPage(driver), ShopPage(driver), SignupPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Ввод имени {fake_user.first_name} и email { fake_user.email} в форму создания нового пользователя'):
            login_page.create_new_user(fake_user)
        with allure.step(f'Появилось сообщение о что email найден в системе'):
            login_page.new_user_error_message()



















