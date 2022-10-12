import allure
import selene
from selene.support.shared.jquery_style import ss


@allure.title('Remove cookie banner from the site')
def remove_cookie_banner():
    (
        ss('#onetrust-consent-sdk #onetrust-banner-sdk').with_(timeout=10)
            .should(selene.have.size_greater_than_or_equal(1))
            .perform(selene.command.js.remove)
    )
