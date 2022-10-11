import os
import allure
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage


@pytest.fixture(scope='class')
def open_main_page(setup_browser):
    browser = setup_browser
    url = os.getenv('main_url')

    with allure.step('Open page discord.com'):
        browser.open(url)
    with allure.step('Assert title footer visibility'):
        BasePage().assert_element_visibility(MainPage.footer_title)
    with allure.step('Assert text in title footer element'):
        BasePage().assert_exact_text_in_element(MainPage.footer_title, 'IMAGINE A PLACE')
