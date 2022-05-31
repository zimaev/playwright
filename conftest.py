import random
from playwright.sync_api import sync_playwright
import allure
from helpers.user import User
from api.UserAPI import UserAPI
import pytest
import requests


@pytest.fixture()
def driver():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                    devtools=False,
                                    slow_mo=500)
        context = browser.new_context(record_video_dir="tests/videos",
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


@pytest.fixture()
def fake_user():
    user = User()
    return user


@pytest.fixture()
def user_api(fake_user):

    data = {
        "name": fake_user.first_name,
        "email": fake_user.email,
        "password": fake_user.password,
        "title": random.choice(['Mr', 'Ms']),
        "birth_date": str(random.randint(1, 31)),
        "birth_month": str(random.randint(1, 12)),
        "birth_year":  str(random.randint(1900, 2021)),
        "firstname": fake_user.first_name,
        "lastname": fake_user.last_name,
        "company": fake_user.last_name,
        "address1": fake_user.address1,
        "country": fake_user.country,
        "zipcode": fake_user.zipcode,
        "state": fake_user.state,
        "city": fake_user.state,
        "mobile_number": fake_user.mobile_number
    }

    return UserAPI.create_new_user(data)











