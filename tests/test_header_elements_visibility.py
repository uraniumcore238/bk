import os
import time
import allure
from selene import be

from pages.main_page import MainPage


class TestHeaderElementsVisibility:

    def test_desktop_visibility_header_elements(self, setup_browser):
        browser = setup_browser
        url = os.getenv('main_url')

        with allure.step('Open page discord.com'):
            browser.open(url)

        with allure.step('Assert logo visibility'):
            MainPage.logo.should(be.visible)
            time.sleep(10)
        # with allure.step('Assert text in element'):
        #     BasePage.assert_exact_text_in_element(self, MainPage.download, 'Download')
        # with allure.step('Assert texts in elements'):
        #     BasePage.assert_exact_text_in_element(self, MainPage.nitro, 'Nitro')
        #     BasePage.assert_exact_text_in_element(self, MainPage.discover, 'Discover')
        #     BasePage.assert_exact_text_in_element(self, MainPage.safety, 'Safety')
        #     BasePage.assert_exact_text_in_element(self, MainPage.support, 'Support')
        #     BasePage.assert_exact_text_in_element(self, MainPage.blog, 'Blog')
        #     BasePage.assert_exact_text_in_element(self, MainPage.careers, 'Careers')
        # with allure.step('Assert login button visibility'):
        #     BasePage.assert_element_visibility(self, MainPage.login_btn)


