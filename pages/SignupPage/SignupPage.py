from pages.BasePage import BasePage
from pages.SignupPage.SignupLocators import SignupLocators
import random


class SignupPage(BasePage):

    def enter_account_information(self, user):
        self.click(random.choice([SignupLocators.MR, SignupLocators.MRS]))
        self.type(SignupLocators.PASSWORD, user.password)
        self.select_option(SignupLocators.DAYS, user.days)
        self.select_option(SignupLocators.MONTHS, user.months)
        self.select_option(SignupLocators.YEAR, user.years)
        self.click(SignupLocators.NEWS)
        self.type(SignupLocators.FIRST_NAME, user.first_name)
        self.type(SignupLocators.LAST_NAME, user.last_name)
        self.type(SignupLocators.COMPANY, user.company)
        self.type(SignupLocators.ADDRESS1, user.address1)
        self.select_option(SignupLocators.COUNTRY, user.country)
        self.type(SignupLocators.STATE, user.state)
        self.type(SignupLocators.CITY, user.city)
        self.type(SignupLocators.ZIP, user.zipcode)
        self.type(SignupLocators.MOBILE, user.mobile_number)
        self.click(SignupLocators.CREATE_ACCOUNT_BUTTON)








