import requests
import allure


class ProductAPI:

    @staticmethod
    def get_product_list():
        with allure.step(f'получить список всех товаров'):
            url = "https://automationexercise.com/api/productsList"
            return requests.request("GET", url=url)

    @staticmethod
    def search_product(name):
        with allure.step(f'поиск продукта'):
            url = "https://automationexercise.com/api/searchProduct"
            payload = {'search_product': name}
            return requests.post(url=url, data=payload)


