import pytest
from playwright.sync_api import sync_playwright
import allure
from helpers.user import User


@pytest.fixture()
def driver():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                    devtools=False,
                                    slow_mo=5000)
        context = browser.new_context(record_video_dir="videos/",
                                      viewport={'width': 1280,
                                                'height': 1024}
                                      )
        page = context.new_page()
        yield page
        video = page.video.path()
        page.close()
        browser.close()
        allure.attach.file(f'{video}', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture()
def fake_user():
    user = User()
    return user






