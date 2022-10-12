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


# @pytest.fixture(scope='class')
# def open_mobile_main_page(setup_mobile_browser):
#     browser = setup_mobile_browser
#     url = os.getenv('main_url')
#     with allure.step('Open page discord.com'):
#         browser.open(url)
#
#
# @pytest.fixture(scope='function')
# def open_side_menu():
#     with allure.step('Click on side menu button'):
#         BasePage().click_on_element(MainPage.side_menu_button)
#     with allure.step('Assert side menu visibility'):
#         BasePage().assert_element_visibility(MainPage.side_menu)
