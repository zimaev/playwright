import requests
import allure


class ProductAPI:

    @staticmethod
    def get_product_list():
        with allure.step(f'получить список всех товаров'):
            url = "https://automationexercise.com/api/productsList"
            return requests.request("GET", url=url)
