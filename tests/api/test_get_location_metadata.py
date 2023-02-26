import allure

from schemas.location_metadata import location_metadata
from utils.sessions import api_url
from pytest_voluptuous import S


@allure.title('Api test')
def test_get_location_metadata():
    with allure.step('Send request'):
        response = api_url().get("/auth/location-metadata")
        assert response.status_code == 200
        assert S(location_metadata) == response.json()


