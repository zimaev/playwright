import requests
import allure


class UserAPI:

    @staticmethod
    def create_new_user(json):
        with allure.step(f'Создание пользователя через API'):
            url = "https://automationexercise.com/api/createAccount"
            return requests.request("POST", url=url, data=json)
        # with allure.step(f'POST запрос к эндпоинту:  c телом запроса {json}'):
        #     url = "https://automationexercise.com/api/createAccount"
        #     return requests.request("POST", url=url, json=json)
