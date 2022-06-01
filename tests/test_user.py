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
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите на кнопку "Регистрация / вход"
        5. Убедитесь, что "Регистрация нового пользователя!" видна
        6. Введите имя и адрес электронной почты
        7. Нажмите кнопку "Зарегистрироваться"
        8. Убедитесь, что "ВВЕДИТЕ ИНФОРМАЦИЮ ОБ учетной записи" видна
        9. Заполните данные: название, имя, адрес электронной почты, пароль, дата рождения
        10. Установите флажок "Подписаться на нашу рассылку!"
        11. Установите флажок "Получать специальные предложения от наших партнеров!"
        12. Заполните данные: Имя, Фамилия, Компания, Адрес, Адрес2, Страна, штат, город, Почтовый индекс, номер мобильного телефона
        13. Нажмите кнопку "Создать учетную запись"
        14. Убедитесь, что видна надпись "УЧЕТНАЯ ЗАПИСЬ СОЗДАНА!".
        15. Нажмите кнопку "Продолжить"
        16. Убедитесь, что виден параметр "Войти под именем пользователя".
        17. Нажмите кнопку "Удалить учетную запись"
        18. Убедитесь, что видна надпись "УЧЕТНАЯ ЗАПИСЬ УДАЛЕНА!", и нажмите кнопку "Продолжить".
        """
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
        with allure.step(f'Нажать кнопку Сontinue'):
            account_created_page.click_continue()
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)

    @allure.title("Test Case 2: Авторизация пользователя с корректными учетными данными")
    def test_login_user_with_correct_user_password(self, driver, fake_user, user_api):
        """
        1. Запустите браузер
        2. Перейдите к URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница успешно видна.
        4. Нажмите на кнопку "Регистрация / Вход".
        5. Убедитесь, что "Вход в вашу учетную запись" виден.
        6. Введите правильный адрес электронной почты и пароль.
        7. Нажмите кнопку "Войти".
        8. Убедитесь, что "Logined in as username" виден
        9. Нажмите кнопку "Удалить учетную запись"
        10. Убедитесь, что "УЧЕТНАЯ ЗАПИСЬ УДАЛЕНА!" видна
        """
        login_page, shop, signup_page = LoginPage(driver), ShopPage(driver), SignupPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Заполнение полей авторизации пользователя корретными данными '):
            login_page.login_to_account(fake_user)
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)

    @allure.title("Test Case 3: Авторизация пользователя с некорректными данными")
    def test_login_with_incorrect_email_password(self, driver, fake_user):
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите на кнопку "Регистрация / вход"
        5. Убедитесь, что "Вход в вашу учетную запись" виден.
        6. Введите неверный адрес электронной почты и пароль
        7. Нажмите кнопку "Войти".
        8. Проверьте, видна ли ошибка "Ваш адрес электронной почты или пароль неверны!"
        """
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
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите на кнопку "Регистрация / вход"
        5. Убедитесь, что "Вход в вашу учетную запись" виден
        6. Введите правильный адрес электронной почты и пароль
        7. Нажмите кнопку "войти"
        8. Убедитесь, что "Logined in as username" виден
        9. Нажмите кнопку "Выход"
        10. Убедитесь, что пользователь перешел на страницу входа
        """
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
        """
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите на кнопку "Регистрация / вход"
        5. Убедитесь, что "Регистрация нового пользователя!" видна
        6. Введите имя и уже зарегистрированный адрес электронной почты
        7. Нажмите кнопку "Зарегистрироваться"
        8. Проверьте, что ошибка "Адрес электронной почты уже существует!" видна
        """
        login_page, shop, signup_page = LoginPage(driver), ShopPage(driver), SignupPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Ввод имени {fake_user.first_name} и email { fake_user.email} в форму создания нового пользователя'):
            login_page.create_new_user(fake_user)
        with allure.step(f'Появилось сообщение о что email найден в системе'):
            login_page.new_user_error_message()



















