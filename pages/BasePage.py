import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_site(self):
        self.page.goto('https://automationexercise.com/', wait_until="domcontentloaded")

    @allure.step('Клик на элемент - {locator}')
    def click(self, locator: str):
        self.page.click(locator)

    @allure.step('Установка чек-бокса locator - {locator}')
    def check(self, locator: str):
        self.page.check(locator)

    @allure.step('Uncheck checkbox locator - {locator}')
    def uncheck(self, locator: str):
        self.page.check(locator)

    @allure.step('Hover(наведение курсова) locator - {locator}')
    def hover(self, locator: str):
        self.page.hover(locator)

    @allure.step('Вводе текста - {text} into locator - {locator}')
    def type(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    @allure.step('Select option - {option} in locator - {locator}')
    def select_option(self, locator: str, option: str):
        self.page.select_option(locator, option)




