import requests
import allure


class UserAPI:

    def create_new_user(self, json):
        with allure.step(f'POST запрос к эндпоинту:  c телом запроса {json}'):
            url = "https://automationexercise.com/api/createAccount"
            return requests.request("POST", url=url, json=json)
