from playwright.sync_api import sync_playwright
import allure
from helpers.user import User
from api.UserAPI import UserAPI
import pytest


@allure.step('Запуск браузера, контекста')
@pytest.fixture(autouse=True)
def driver():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                    devtools=False,
                                    slow_mo=000,
                                    timeout=60000)

        context = browser.new_context(record_video_dir="./videos",
                                      viewport={'width': 1440,
                                                'height': 1024}
                                      )
        context.tracing.start(screenshots=True, snapshots=False)
        page = context.new_page()
        yield page
        video = page.video.path()

        # context.tracing.stop(path="trace.zip")
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    test_result = outcome.get_result()

    if test_result.when in ["setup", "call"]:
        xfail = hasattr(test_result, 'wasxfail')
        if test_result.failed or (test_result.skipped and xfail):
            global PAGE
            if PAGE:
                allure.attach(PAGE.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)
                allure.attach(PAGE.content(), name='html_source', attachment_type=allure.attachment_type.HTML)
