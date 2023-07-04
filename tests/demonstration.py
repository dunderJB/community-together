import pytest
from fastapi.testclient import TestClient
from unittest import mock
from src.entrypoints.routes import health_check
from src.app import app


@pytest.fixture()
def test_client():
    test_client = TestClient(app)
    return test_client


def test_request_health_check_is_working(monkeypatch, test_client):
    # arrange
    randint_mock = mock.MagicMock()
    randint_mock.return_value = 1
    monkeypatch.setattr(health_check, 'randint', randint_mock)

    # act
    response = test_client.get('/community-together/health-check')

    # assert
    assert response.status_code == 200


def test_request_health_check_is_not_working(monkeypatch, test_client):
    # arrange
    randint_mock = mock.MagicMock()
    randint_mock.return_value = 2
    monkeypatch.setattr(health_check, 'randint', randint_mock)

    # act
    response = test_client.get('/community-together/health-check')

    # assert
    assert response.status_code == 500