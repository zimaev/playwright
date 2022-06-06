import requests
import allure


class BrandAPI:

    @staticmethod
    def get_brand_list():
        with allure.step(f'получить список всех брендов'):
            url = "https://automationexercise.com/api/brandsList"
            brand_list_raw = requests.request("GET", url=url).json()['brands']
            brand_list = []
            for i in brand_list_raw:
                brand_list.append(i['brand'])
            return set(brand_list)

