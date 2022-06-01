
from playwright.sync_api import sync_playwright
import allure
from helpers.user import User
from api.UserAPI import UserAPI
import pytest


@allure.step('Запуск браузера, контекста')
@pytest.fixture()
def driver():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True,
                                    devtools=False,
                                    slow_mo=500)
        context = browser.new_context(record_video_dir="./videos",
                                      viewport={'width': 1440,
                                                'height': 1024}
                                      )
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        yield page
        video = page.video.path()
        context.tracing.stop(path="trace.zip")
        page.close()
        browser.close()
        allure.attach.file(f'{video}', attachment_type=allure.attachment_type.WEBM)


@allure.step('Создание тестово пользователя')
@pytest.fixture()
def fake_user():
    user = User()
    return user


@allure.step('Создание тестово пользователя через API')
@pytest.fixture()
def user_api(fake_user):
    return UserAPI.create_new_user(fake_user.JSON_user())
