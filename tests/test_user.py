import pytest
from pages.MainPage import ShopPage
from pages.LoginPage.LoginPage import LoginPage
from pages.SignupPage.SignupPage import SignupPage
from pages.SignupPage.AccountCreatedPage import AccountCreatedPage
import allure
import requests


@allure.epic('Тесты регистрации/авторизации пользователя входа/выхода из системы')
class TestUser(object):

    @allure.title("Test Case 1: Регистрация пользователя")
    def test_register_user(self, driver, fake_user):
        login_page, shop, signup_page, account_created_page = LoginPage(driver), ShopPage(driver), \
                                                              SignupPage(driver), AccountCreatedPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Ввод имени {fake_user.first_name} и email { fake_user.email} в форму создания нового пользователя'):
            login_page.create_new_user(fake_user)
        with allure.step(f'Заполнение полей регистрации нового пользователя '):
            signup_page.enter_account_information(fake_user)
        with allure.step(f'Открылась страница поздравления о созданном аккаунте'):
            account_created_page.account_created_message()
        with allure.step(f'Нажать кнопку continue'):
            account_created_page.click_continue()
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)

    @allure.title("Test Case 2: Авторизация пользователя с корректными учетными данными")
    def test_login_user(self, driver, fake_user):
        login_page, shop, signup_page = LoginPage(driver), ShopPage(driver), SignupPage(driver)

        data = {
            "name": fake_user.first_name,
            "email": fake_user.email,
            "password": fake_user.password,
            "title": "Mr",
            "birth_date": '12',
            "birth_month": "12",
            "birth_year": '1990',
            "firstname": fake_user.first_name,
            "lastname": fake_user.last_name,
            "company": fake_user.last_name,
            "address1": fake_user.address1,
            "country": fake_user.country,
            "zipcode": fake_user.zipcode,
            "state": fake_user.state,
            "city": fake_user.state,
            "mobile_number": fake_user.mobile_number
        }

        url = "https://automationexercise.com/api/createAccount"

        response = requests.request("POST", url, data=data)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Заполнение полей авторизации пользователя  некорретными данными '):
            login_page.login_to_account(fake_user)
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)

    @allure.title("Test Case 3: Авторизация пользователя с некорректными данными")
    def test_negative_register_user(self, driver, fake_user):
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
    def test_logout_user(self, driver, fake_user):
        login_page, shop, signup_page = LoginPage(driver), ShopPage(driver), SignupPage(driver)

        data = {
            "name": fake_user.first_name,
            "email": fake_user.email,
            "password": fake_user.password,
            "title": "Mr",
            "birth_date": '12',
            "birth_month": "12",
            "birth_year": '1990',
            "firstname": fake_user.first_name,
            "lastname": fake_user.last_name,
            "company": fake_user.last_name,
            "address1": fake_user.address1,
            "country": fake_user.country,
            "zipcode": fake_user.zipcode,
            "state": fake_user.state,
            "city": fake_user.state,
            "mobile_number": fake_user.mobile_number
        }

        url = "https://automationexercise.com/api/createAccount"

        response = requests.request("POST", url, data=data)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Заполнение полей авторизации пользователя  некорретными данными '):
            login_page.login_to_account(fake_user)
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)
        with allure.step(f'выход из системы'):
            shop.logout()





















