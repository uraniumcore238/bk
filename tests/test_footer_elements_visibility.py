import os
import allure

from pages.base_page import BasePage
from pages.main_page import MainPage


class TestFooterElementsVisibility:

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_elements(self, setup_browser):
        browser = setup_browser
        url = os.getenv('main_url')

        with allure.step('Open page discord.com'):
            browser.open(url)
        with allure.step('Assert title footer visibility'):
            BasePage.assert_element_visibility(self, MainPage.footer_title)
        with allure.step('Assert text in title footer element'):
            BasePage.assert_exact_text_in_element(self, MainPage.footer_title, 'IMAGINE A PLACE')
        with allure.step('Assert texts in elements'):
            BasePage.assert_exact_text_in_element(self, MainPage.download_footer, 'Download')
            BasePage.assert_exact_text_in_element(self, MainPage.nitro_footer, 'Nitro')
            BasePage.assert_exact_text_in_element(self, MainPage.status_footer, 'Status')
            BasePage.assert_exact_text_in_element(self, MainPage.about_footer, 'About')
            BasePage.assert_exact_text_in_element(self, MainPage.jobs_footer, 'Jobs')
            BasePage.assert_exact_text_in_element(self, MainPage.branding_footer, 'Branding')
            BasePage.assert_exact_text_in_element(self, MainPage.newsroom_footer, 'Newsroom')
            BasePage.assert_exact_text_in_element(self, MainPage.college_footer, 'College')
            BasePage.assert_exact_text_in_element(self, MainPage.support_footer, 'Support')
            BasePage.assert_exact_text_in_element(self, MainPage.safety_footer, 'Safety')
            BasePage.assert_exact_text_in_element(self, MainPage.blog_footer, 'Blog')
            BasePage.assert_exact_text_in_element(self, MainPage.feedback_footer, 'Feedback')
            BasePage.assert_exact_text_in_element(self, MainPage.developers_footer, 'Developers')
            BasePage.assert_exact_text_in_element(self, MainPage.streamkit_footer, 'StreamKit')
            BasePage.assert_exact_text_in_element(self, MainPage.terms_footer, 'Terms')
            BasePage.assert_exact_text_in_element(self, MainPage.privacy_footer, 'Privacy')
            BasePage.assert_exact_text_in_element(self, MainPage.cookie_settings_footer, 'Cookie Settings')
            BasePage.assert_exact_text_in_element(self, MainPage.guidelines_footer, 'Guidelines')
            BasePage.assert_exact_text_in_element(self, MainPage.acknowledgements_footer, 'Acknowledgements')
            BasePage.assert_exact_text_in_element(self, MainPage.licenses_footer, 'Licenses')
            BasePage.assert_exact_text_in_element(self, MainPage.moderation_footer, 'Moderation')
        with allure.step('Sign up button visibility'):
            BasePage.assert_element_visibility(self, MainPage.signup_btn)
