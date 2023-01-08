import allure
import pytest


@pytest.fixture(scope='class')
def open_main_page(setup_browser):
    browser = setup_browser
    url = 'https://discord.com'
    with allure.step('Open page discord.com'):
        browser.open(url)
