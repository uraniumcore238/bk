import allure
from selene import be, have
from selene.core.entity import Element


class BasePage:

    def assert_element_visibility(self, el: Element):
        with allure.step(f'Element {el} should be visible'):
            el.should(be.visible)

    def assert_exact_text_in_element(self, el: Element, text: str):
        with allure.step(f'Element {el} should have text - {text}'):
            el.should(have.exact_text(text))

    def click_on_element(self, el: Element):
        el.should(be.visible).click()
