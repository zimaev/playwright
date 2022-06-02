import requests
import allure


class BrandAPI:

    @staticmethod
    def get_brand_list():
        with allure.step(f'получить список всех брендов'):
            url = "https://automationexercise.com/api/brandsList"
            return requests.request("GET", url=url)
