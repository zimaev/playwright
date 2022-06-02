from playwright.sync_api import  expect
from pages.BasePage import BasePage
from pages.LoginPage.LoginPageLocators import LoginLocator


class LoginPage(BasePage):

    def create_new_user(self, user):
        self.type(LoginLocator.NAME, user.first_name)
        self.type(LoginLocator.EMAIL, user.email)
        self.click(LoginLocator.SIGN_UP_BUTTON)

    def login_to_account(self, user):
        self.type(LoginLocator.LOGIN_EMAIL, user.email)
        self.type(LoginLocator.PASSWORD, user.password)
        self.click(LoginLocator.LOGIN_BUTTON)

    def login_error_message(self):
        expect(self.page.locator('.login-form p')).to_be_visible()
        expect(self.page.locator('.login-form p')).to_have_text('Your email or password is incorrect!')
        self.attach_screenshot('.login-form p', 'login_error_message')



    def new_user_error_message(self):
        expect(self.page.locator('.signup-form p')).to_be_visible()
        expect(self.page.locator('.signup-form p')).to_have_text('Email Address already exist!')
        self.attach_screenshot('.login-form p', 'new_user_error_message')



