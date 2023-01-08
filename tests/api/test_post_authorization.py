from schemas.success_authorization import success_authorization
from utils.sessions import api_url
from pytest_voluptuous import S

parameters = {
    "login": "",
    "password": "",
    "undelete": False,
    "captcha_key": None,
    "login_source": None,
    "gift_code_sku_id": None
}


def test_post_authorization():
    pass
    # response = api_url().post("/auth/login", json=parameters)
    #
    # assert response.status_code == 200
    # assert S(success_authorization) == response.json()
    # dict_json_data = response.json()
    #
    #
    # # name = parameters['name']
    # # job = parameters['job']
    #
    # assert '380428862334697473' == dict_json_data['user_id']
    # assert 'dark' == dict_json_data['user_settings']['theme']










