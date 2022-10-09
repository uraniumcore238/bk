import os
from utils.requests_helper import BaseSession


def api_url() -> BaseSession:
    root_url = os.getenv('api_url')
    return BaseSession(base_url=root_url)


def boards_api_url() -> BaseSession:
    root_url = os.getenv('boards_api_url')
    return BaseSession(base_url=root_url)
