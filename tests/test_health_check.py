import pytest
import requests
from requests_mock.mocker import Mocker
from fastapi.testclient import TestClient
from src.app import app


# teste diretamente no cliente para as rotas adicionadas ao objeto app ex: get('/community-together/health-check')
def test_request_health_check_is_working():
    test_app = TestClient(app)

    response = test_app.get('/community-together/health-check')

    assert response.status_code == 200


