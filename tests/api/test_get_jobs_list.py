from schemas.jobs_list import jobs_list
from utils.sessions import boards_api_url
from pytest_voluptuous import S


def test_get_jobs_list():
    response = boards_api_url().get('/jobs?content=true')
    assert response.status_code == 200
    assert S(jobs_list) == response.json()

