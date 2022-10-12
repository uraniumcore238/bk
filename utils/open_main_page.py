import os
import allure
import pytest


@pytest.fixture(scope='class')
def open_main_page(setup_browser):
    browser = setup_browser
    url = os.getenv('main_url')
    with allure.step('Open page discord.com'):
        browser.open(url)
