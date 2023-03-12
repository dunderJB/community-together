from http import HTTPStatus
from fastapi.responses import JSONResponse
from src.domain.models.customer import CustomerRequest, CustomerResponse
from src.infra.repository.customer import insert_customer_repo, delete_customer_repo, get_customer_by_id_repo, update_customer_repo


async def create_customer(customer: CustomerRequest) -> JSONResponse:
    customer_id = await insert_customer_repo(customer=customer)
    customer_response = CustomerResponse(**customer.dict(), id=customer_id)
    return JSONResponse(content=customer_response.dict(), status_code=HTTPStatus.CREATED)


async def delete_customer(id_: int) -> JSONResponse:
    await delete_customer_repo(id_)
    return JSONResponse(content={}, status_code=HTTPStatus.OK)


async def get_customer_by_id(id_: int) -> JSONResponse:
    customer = await get_customer_by_id_repo(id_)
    customer_response = CustomerResponse(id=customer.id, username=customer.username, email=customer.email)
    return JSONResponse(content=customer_response.dict(), status_code=HTTPStatus.OK)


async def update_customer(id_: int, customer: CustomerRequest) -> JSONResponse:
    await update_customer_repo(id_=id_, customer=customer)
    customer_response = CustomerResponse(id=id_, username=customer.username, email=customer.email)
    return JSONResponse(content=customer_response.dict(), status_code=HTTPStatus.OK)
