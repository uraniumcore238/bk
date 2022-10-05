import os

import allure

from pages.base_page import BasePage
from pages.main_page import MainPage


class TestHeaderElementsVisibility:

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_header_elements(self, setup_browser):
        browser = setup_browser
        url = os.getenv('main_url')

        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Assert logo visibility'):
            BasePage.assert_element_visibility(self, MainPage.logo)
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.download, 'Download')
        with allure.step('Assert texts in elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.nitro, 'Nitro')
            BasePage.assert_exact_text_in_element(self, MainPage.discover, 'Discover')
            BasePage.assert_exact_text_in_element(self, MainPage.safety, 'Safety')
            BasePage.assert_exact_text_in_element(self, MainPage.support, 'Support')
            BasePage.assert_exact_text_in_element(self, MainPage.blog, 'Blog')
            BasePage.assert_exact_text_in_element(self, MainPage.careers, 'Careers')
        with allure.step('Assert login button visibility'):
            BasePage.assert_element_visibility(self, MainPage.login_btn)

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_visibility_elements(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')

        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Assert mobile logo visibility'):
            BasePage.assert_element_visibility(self, MainPage.mobile_logo)
        with allure.step('Assert mobile login button visibility'):
            BasePage.assert_element_visibility(self, MainPage.mobile_login_btn)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.home_side_menu, 'Home')
            BasePage.assert_exact_text_in_element(self, MainPage.download_side_menu, 'Download')
            BasePage.assert_exact_text_in_element(self, MainPage.nitro_side_menu, 'Nitro')
            BasePage.assert_exact_text_in_element(self, MainPage.discover_side_menu, 'Discover')
            BasePage.assert_exact_text_in_element(self, MainPage.safety_side_menu, 'Safety')
            BasePage.assert_exact_text_in_element(self, MainPage.mod_academy_side_menu, 'Mod Academy')
            BasePage.assert_exact_text_in_element(self, MainPage.support_side_menu, 'Support')
            BasePage.assert_exact_text_in_element(self, MainPage.blog_side_menu, 'Blog')
            BasePage.assert_exact_text_in_element(self, MainPage.careers_side_menu, 'Careers')
        with allure.step('Assert download button visibility'):
            BasePage.assert_element_visibility(self, MainPage.download_button)
