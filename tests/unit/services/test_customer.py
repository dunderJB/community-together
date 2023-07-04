import pytest
from starlette.responses import JSONResponse
from src.domain.models import CustomerRequest
from src.services.customer import create_customer, delete_customer, get_customer_by_id, update_customer
from src.services import customer
from unittest import mock


@pytest.fixture()
def session_mock():
    return mock.MagicMock()


@pytest.fixture()
def insert_customer_mock():
    return mock.AsyncMock(return_value=1)


@pytest.fixture()
def delete_customer_mock():
    return mock.AsyncMock()


@pytest.mark.asyncio()
async def test_create_customer_when_request_is_valid(monkeypatch, session_mock, insert_customer_mock):
    # arrange
    monkeypatch.setattr(customer, "Session", session_mock)
    monkeypatch.setattr(customer, "insert_customer_repo", insert_customer_mock)
    valid_customer = CustomerRequest(username="John doe dev", email="johndoedev@teste.com", about="about me")

    # act
    customer_created = await create_customer(customer=valid_customer)

    # assert  
    assert customer_created
    assert isinstance(customer_created, JSONResponse)
    assert customer_created.status_code == 201


@pytest.mark.asyncio()
async def test_delete_customer_when_request_is_valid(monkeypatch, session_mock, delete_customer_mock):
    # arrange
    monkeypatch.setattr(customer, "Session", session_mock)
    monkeypatch.setattr(customer, "delete_customer_repo", delete_customer_mock)

    id_customer = 1

    # act
    customer_deleted = await delete_customer(id_=id_customer)

    # assert
    assert customer_deleted.status_code == 200
    assert isinstance(customer_deleted, JSONResponse)
    assert customer_deleted
