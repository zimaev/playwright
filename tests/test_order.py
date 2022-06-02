import allure
from pages.MainPage.MainPage import ShopPage
from pages.LoginPage.LoginPage import LoginPage
from pages.SignupPage.SignupPage import SignupPage
from pages.SignupPage.AccountCreatedPage import AccountCreatedPage
from pages.CartPage.CartPage import CartPage
from pages.CartPage.CheckoutPage.CheckoutPage import CheckoutPage
from pages.CartPage.PaymentPage.PaymentPage import PaymentPage
import allure


@allure.epic('Тесты на покупку товара')
@allure.suite('Тесты на покупку товара')
class TestOrder:

    @allure.title("Test Case 14: Разместить заказ: зарегистрироваться во время оформления заказа")
    def test_place_order_register_while_checkout(self, driver, fake_user):
        """"
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Добавить товары в корзину
        5. Нажмите кнопку "Корзина"
        6. Убедитесь, что отображается страница корзины
        7. Нажмите Перейти к оформлению заказа
        8. Нажмите кнопку "Зарегистрироваться / войти"
        9. Заполните все данные в регистрации и создайте учетную запись
        10. Подтвердите "УЧЕТНАЯ ЗАПИСЬ СОЗДАНА!" и нажмите кнопку "Продолжить"
        11. Проверьте "Logged in as username" вверху
        12. Нажмите кнопку "Корзина"
        13. Нажмите кнопку "Перейти к оформлению заказа"
        14. Проверьте данные адреса и просмотрите свой заказ
        15. Введите описание в текстовую область комментария и нажмите "Оформить заказ"
        16. Введите платежные реквизиты: имя на карте, номер карты, CVC, срок годности
        17. Нажмите кнопку "Оплатить и подтвердить заказ"
        18. Проверьте сообщение об успехе "Ваш заказ успешно размещен!"
        19. Нажмите кнопку "Удалить учетную запись"
        20. Подтвердите "УЧЕТНАЯ ЗАПИСЬ УДАЛЕНА!" и нажмите кнопку "Продолжить"
        """
        login_page, shop, signup_page, account_created_page, view_cart, checkout, payment = LoginPage(driver), ShopPage(driver), \
                                                              SignupPage(driver), AccountCreatedPage(driver),\
                                                                    CartPage(driver), CheckoutPage(driver), PaymentPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Добавить товары в корзину'):
            shop.add_product_to_card(1)
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Склик на кнопку Открыть корзину'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'Склик на кнопку Proceed To Checkout'):
            driver.locator(".btn.btn-default.check_out").click()
        with allure.step(f'Склик на кнопку Proceed To Checkout'):
            driver.locator("//u[text()='Register / Login']").click()
        with allure.step(f'Ввод имени и email в форму создания нового пользователя'):
            login_page.create_new_user(fake_user)
        with allure.step(f'Заполнение полей регистрации нового пользователя '):
            signup_page.enter_account_information(fake_user)
        with allure.step(f'Открылась страница поздравления о созданном аккаунте'):
            account_created_page.account_created_message()
        with allure.step(f'Нажать кнопку Сontinue'):
            account_created_page.click_continue()
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)
        with allure.step(f'Открыть карзину'):
            shop.open_cart()
        with allure.step(f'Склик на кнопку Proceed To Checkout'):
            view_cart.click_proceed_check_out()
        with allure.step(f'Заполнение комментария к заказу'):
            checkout.fill_comment_to_order()
        with allure.step(f'Склик на кнопку Place Order'):
            checkout.click_place_order()
        with allure.step(f'Заполнение реквизитов карты'):
            payment.fill_card_details()
        with allure.step(f'Подтверждение платежных данных и оформление заказа'):
            payment.click_pay_and_confirm_order()

    @allure.title("Test Case 15: Разместить заказ: зарегистрироваться перед оформлением заказа")
    def test_place_order_register_before_checkout(self, driver, fake_user):
        """"
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите кнопку "Регистрация / вход"
        5. Заполните все детали в регистрации и создать учетную запись
        6. Подтвердите "УЧЕТНАЯ ЗАПИСЬ СОЗДАНА!" и нажмите кнопку "Продолжить"
        7. Проверьте "Logged in as username" вверху
        8. Добавить товары в корзину
        9. Нажмите кнопку "Корзина"
        10. Убедитесь, что отображается страница корзины
        11. Нажмите кнопку Перейти к оформлению заказа
        12. Проверьте детали адреса и просмотрите свой заказ
        13. Введите описание в текстовую область комментария и нажмите "Оформить заказ"
        14. Введите платежные реквизиты: имя на карте, номер карты, CVC, срок годности
        15. Нажмите кнопку "Оплатить и подтвердить заказ"
        16. Проверьте сообщение об успехе "Ваш заказ успешно размещен!"
        17. Нажмите кнопку "Удалить учетную запись"
        18. Подтвердите "УЧЕТНАЯ ЗАПИСЬ УДАЛЕНА!" и нажмите кнопку "Продолжить"
        """
        login_page, shop, signup_page, account_created_page, view_cart, checkout, payment = LoginPage(driver), ShopPage(driver), \
                                                                                            SignupPage(driver), AccountCreatedPage(driver), \
                                                                                            CartPage(driver), CheckoutPage(driver), PaymentPage(driver)

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

        with allure.step(f'Добавить товары в корзину'):
            shop.add_product_to_card(1)
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Склик на кнопку Открыть корзину'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'Склик на кнопку Proceed To Checkout'):
            driver.locator(".btn.btn-default.check_out").click()
        with allure.step(f'Заполнение комментария к заказу'):
            checkout.fill_comment_to_order()
        with allure.step(f'Склик на кнопку Place Order'):
            checkout.click_place_order()
        with allure.step(f'Заполнение реквизитов карты'):
            payment.fill_card_details()
        with allure.step(f'Подтверждение платежных данных и оформление заказа'):
            payment.click_pay_and_confirm_order()

    @allure.title("Test Case 16: Разместить заказ: войти перед оформлением заказа")
    def test_place_order_login_before_checkout(self, driver, fake_user, user_api):
        """"
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите кнопку "Регистрация / вход"
        5. Заполните адрес электронной почты, пароль и нажмите кнопку "Войти"
        6. Проверьте "Logged in as username" вверху
        7. Добавить товары в корзину
        8. Нажмите кнопку "Корзина"
        9. Убедитесь, что отображается страница корзины
        10. Нажмите Перейти к оформлению заказа
        11. Проверьте детали адреса и просмотрите свой заказ
        12. Введите описание в текстовую область комментария и нажмите "Оформить заказ"
        13. Введите платежные реквизиты: имя на карте, номер карты, CVC, срок годности
        14. Нажмите кнопку "Оплатить и подтвердить заказ"
        15. Проверьте сообщение об успехе "Ваш заказ успешно размещен!"
        16. Нажмите кнопку "Удалить учетную запись"
        17. Подтвердите "УЧЕТНАЯ ЗАПИСЬ УДАЛЕНА!" и нажмите кнопку "Продолжить"
        """
        login_page, shop, signup_page, account_created_page, view_cart, checkout, payment = LoginPage(driver), ShopPage(driver), \
                                                                                            SignupPage(driver), AccountCreatedPage(driver), \
                                                                                            CartPage(driver), CheckoutPage(driver), PaymentPage(driver)
        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Заполнение полей авторизации пользователя корретными данными '):
            login_page.login_to_account(fake_user)
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)

        with allure.step(f'Добавить товары в корзину'):
            shop.add_product_to_card(1)
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Склик на кнопку Открыть корзину'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'Склик на кнопку Proceed To Checkout'):
            driver.locator(".btn.btn-default.check_out").click()
        with allure.step(f'Заполнение комментария к заказу'):
            checkout.fill_comment_to_order()
        with allure.step(f'Склик на кнопку Place Order'):
            checkout.click_place_order()
        with allure.step(f'Заполнение реквизитов карты'):
            payment.fill_card_details()
        with allure.step(f'Подтверждение платежных данных и оформление заказа'):
            payment.click_pay_and_confirm_order()

    @allure.title("Test Case 23: Проверка сведений об адресе на странице оформления заказа")
    def test_verify_address_details_in_checkout_page(self, driver, fake_user):
        """"
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Нажмите кнопку "Регистрация / вход"
        5. Заполните все детали в регистрации и создать учетную запись
        6. Подтвердите "УЧЕТНАЯ ЗАПИСЬ СОЗДАНА!" и нажмите кнопку "Продолжить"
        7. Проверьте "Logged in as username" вверху
        8. Добавить товары в корзину
        9. Нажмите кнопку "Корзина"
        10. Убедитесь, что отображается страница корзины
        11. Нажмите кнопку Перейти к оформлению заказа
        12. Убедитесь, что адрес доставки совпадает с адресом, заполненным при регистрации аккаунта
        13. Убедитесь, что платежный адрес совпадает с адресом, заполненным при регистрации аккаунта
        14. Нажмите кнопку "Удалить учетную запись"
        15. Подтвердите "УЧЕТНАЯ ЗАПИСЬ УДАЛЕНА!" и нажмите кнопку "Продолжить"
        """
        login_page, shop, signup_page, account_created_page, view_cart, checkout, payment = LoginPage(driver), \
                                                                                            ShopPage(driver), \
                                                                                            SignupPage( driver), \
                                                                                            AccountCreatedPage(driver), \
                                                                                            CartPage( driver), \
                                                                                            CheckoutPage(driver), \
                                                                                            PaymentPage(driver)

        with allure.step(f'Открыте стартовой страницы магазина'):
            shop.open_site()
        with allure.step(f'Клик в хедере на элемент Signup / Login'):
            shop.open_login_page()
        with allure.step(f'Ввод имени {fake_user.first_name} и email {fake_user.email} в форму создания нового пользователя'):
            login_page.create_new_user(fake_user)
        with allure.step(f'Заполнение полей регистрации нового пользователя '):
            signup_page.enter_account_information(fake_user)
        with allure.step(f'Открылась страница поздравления о созданном аккаунте'):
            account_created_page.account_created_message()
        with allure.step(f'Нажать кнопку Сontinue'):
            account_created_page.click_continue()
        with allure.step(f'В хедере отображается имя {fake_user.first_name} юзера как авторизованного'):
            shop.account_logged(fake_user.first_name)
        with allure.step(f'Добавить товары в корзину'):
            shop.add_product_to_card(1)
        with allure.step(f'Всплывающее окно после отобразилось'):
            shop.modal_window_visible()
        with allure.step(f'Склик на кнопку Открыть корзину'):
            driver.locator("//u[text()='View Cart']").click()
        with allure.step(f'Склик на кнопку Proceed To Checkout'):
            driver.locator(".btn.btn-default.check_out").click()

#####################################################################################################################
        with allure.step(f'Проверка 1 '):
            checkout.assert_billing_address(fake_user)
        with allure.step(f'Проверка 2'):
            checkout.assert_delivery_address(fake_user)


    @allure.title("Test Case 24: Загрузка счета-фактуры после заказа на покупку")
    def test_download_invoice_after_purchase_order(self, driver):
        """"
        1. Запустите браузер
        2. Перейдите по URL-адресу 'http://automationexercise.com '
        3. Убедитесь, что домашняя страница видна успешно
        4. Добавить товары в корзину
        5. Нажмите кнопку "Корзина"
        6. Убедитесь, что отображается страница корзины
        7. Нажмите Перейти к оформлению заказа
        8. Нажмите кнопку "Зарегистрироваться / войти"
        9. Заполните все данные в регистрации и создайте учетную запись
        10. Подтвердите "УЧЕТНАЯ ЗАПИСЬ СОЗДАНА!" и нажмите кнопку "Продолжить"
        11. Проверьте "Logged in as username" вверху
        12.Нажмите кнопку "Корзина"
        13. Нажмите кнопку "Перейти к оформлению заказа"
        14. Проверьте данные адреса и просмотрите свой заказ
        15. Введите описание в текстовую область комментария и нажмите "Оформить заказ"
        16. Введите платежные реквизиты: имя на карте, номер карты, CVC, срок годности
        17. Нажмите кнопку "Оплатить и подтвердить заказ"
        18. Проверьте сообщение об успехе "Ваш заказ успешно размещен!"
        19. Нажмите кнопку "Загрузить счет" и убедитесь, что счет успешно загружен.
        20. Нажмите кнопку "Продолжить"
        21. Нажмите кнопку "Удалить учетную запись"
        22. Подтвердите "УЧЕТНАЯ ЗАПИСЬ УДАЛЕНА!" и нажмите кнопку "Продолжить"
        """
        pass
