import allure
from playwright.sync_api import TimeoutError as TError
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_site(self):
        self.page.goto('https://automationexercise.com/')

    @allure.step('Click locator - {locator}')
    def click(self, locator: str):
        self.page.click(locator)

    @allure.step('Check checkbox locator - {locator}')
    def check(self, locator: str):
        self.page.check(locator)

    @allure.step('Uncheck checkbox locator - {locator}')
    def uncheck(self, locator: str):
        self.page.check(locator)

    @allure.step('Hover locator - {locator}')
    def hover(self, locator: str):
        self.page.hover(locator)

    @allure.step('Type text - {text} into locator - {locator}')
    def type(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    @allure.step('Select option - {option} in locator - {locator}')
    def select_option(self, locator: str, option: str):
        self.page.select_option(locator, option)

    @allure.step('Is element - {locator} present')
    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator)
            return True
        except TError:
            return False

    @allure.step('Is element - {locator} hidden')
    def is_element_hidden(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, state='hidden')
            return True
        except TError:
            return False

    def attach_screenshot(self, locator, name):
        allure.attach(
            self.page.locator(locator).screenshot(path="screenshot.png"),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )


