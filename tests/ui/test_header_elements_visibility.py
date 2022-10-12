import os

import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from utils import remove_cookie_banner
from utils.open_main_page import open_main_page


class TestHeaderElementsVisibility:

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_logo(self, open_main_page):
        with allure.step('Assert logo visibility'):
            BasePage.assert_element_visibility(self, MainPage.logo)

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_text_in_download(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.download, 'Download')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_text_in_nitro(self, open_main_page):
        with allure.step('Assert texts in elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.nitro, 'Nitro')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_text_in_discover(self, open_main_page):
        with allure.step('Assert logo visibility'):
            BasePage.assert_exact_text_in_element(self, MainPage.discover, 'Discover')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_text_in_safety(self, open_main_page):
        with allure.step('Assert logo visibility'):
            BasePage.assert_exact_text_in_element(self, MainPage.safety, 'Safety')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_text_in_support(self, open_main_page):
        with allure.step('Assert logo visibility'):
            BasePage.assert_exact_text_in_element(self, MainPage.support, 'Support')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_text_in_blog(self, open_main_page):
        with allure.step('Assert logo visibility'):
            BasePage.assert_exact_text_in_element(self, MainPage.blog, 'Blog')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_text_in_careers(self, open_main_page):
        with allure.step('Assert logo visibility'):
            BasePage.assert_exact_text_in_element(self, MainPage.careers, 'Careers')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_login_btn_visibility(self, open_main_page):
        with allure.step('Assert login button visibility'):
            BasePage.assert_element_visibility(self, MainPage.login_btn)

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_logo_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Assert mobile logo visibility'):
            BasePage.assert_element_visibility(self, MainPage.mobile_logo)

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_login_btn_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Assert mobile login button visibility'):
            BasePage.assert_element_visibility(self, MainPage.mobile_login_btn)

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_home_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.home_side_menu, 'Home')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_download_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.download_side_menu, 'Download')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_nitro_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.nitro_side_menu, 'Nitro')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_discover_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.discover_side_menu, 'Discover')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_safety_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.safety_side_menu, 'Safety')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_mod_academy_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.mod_academy_side_menu, 'Mod Academy')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_support_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.support_side_menu, 'Support')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_blog_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.blog_side_menu, 'Blog')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_careers_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
        with allure.step('Assert visibility side menu elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.careers_side_menu, 'Careers')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_mobile_header_download_btn_visibility(self, setup_mobile_browser):
        browser = setup_mobile_browser
        url = os.getenv('main_url')
        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Click on side menu button'):
            BasePage.click_on_element(self, MainPage.side_menu_button)
        with allure.step('Assert side menu visibility'):
            BasePage.assert_element_visibility(self, MainPage.side_menu)
            remove_cookie_banner.remove_cookie_banner()
        with allure.step('Assert download button visibility'):
            BasePage.assert_element_visibility(self, MainPage.download_button)
