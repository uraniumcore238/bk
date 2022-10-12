import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from utils.open_main_page import open_main_page


class TestFooterElementsVisibility:

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_download(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.download_footer, 'Download')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_nitro(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.nitro_footer, 'Nitro')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_status(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.status_footer, 'Status')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_about(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.about_footer, 'About')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_jobs(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.jobs_footer, 'Jobs')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_branding(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.branding_footer, 'Branding')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_newsroom(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.newsroom_footer, 'Newsroom')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_college(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.college_footer, 'College')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_support(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.support_footer, 'Support')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_safety(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.safety_footer, 'Safety')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_blog(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.blog_footer, 'Blog')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_feedback(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.feedback_footer, 'Feedback')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_developers(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.developers_footer, 'Developers')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_streamkit(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.streamkit_footer, 'StreamKit')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_terms(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.terms_footer, 'Terms')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_privacy(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.privacy_footer, 'Privacy')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_cookie_settings(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.cookie_settings_footer, 'Cookie Settings')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_guidelines(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.guidelines_footer, 'Guidelines')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_acknowledgements(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.acknowledgements_footer, 'Acknowledgements')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_licenses(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.licenses_footer, 'Licenses')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_moderation(self, open_main_page):
        with allure.step('Assert text in element'):
            BasePage.assert_exact_text_in_element(self, MainPage.moderation_footer, 'Moderation')

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_signup_button(self, open_main_page):
        with allure.step('Sign up button visibility'):
            BasePage.assert_element_visibility(self, MainPage.signup_btn)

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_title(self, open_main_page):
        with allure.step('Assert title footer visibility'):
            BasePage().assert_element_visibility(MainPage.footer_title)

    @allure.severity('Blocker')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Visibility elements on discord.com page')
    def test_desktop_visibility_footer_title_text(self, open_main_page):
        with allure.step('Assert text in title footer element'):
            BasePage().assert_exact_text_in_element(MainPage.footer_title, 'IMAGINE A PLACE')
