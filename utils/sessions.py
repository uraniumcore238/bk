import os
from utils.requests_helper import BaseSession


def api_url() -> BaseSession:
    root_url = os.getenv('api_url')
    return BaseSession(base_url=root_url)


# def main_url() -> BaseSession:
#     root_url = os.getenv('main_url')
#     return BaseSession(base_url=root_url)
