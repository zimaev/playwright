from playwright.sync_api import  expect
from pages.BasePage import BasePage


class AccountCreatedPage(BasePage):

    def account_created_message(self):
        expect(self.page.locator('[data-qa="account-created"]')).to_have_text('Account Created!')

    def click_continue(self):
        self.click('[data-qa="continue-button"]')










