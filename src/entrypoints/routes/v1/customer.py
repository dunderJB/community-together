from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.domain.models.customer import CustomerRequest
from src.services.customer import create_customer, delete_customer, get_customer, update_customer

router = APIRouter()


@router.post('/')
async def _create_customer(customer: CustomerRequest) -> JSONResponse:
    return await create_customer(customer=customer)


@router.get('/{id_}')
async def _get_customer(id_: int) -> JSONResponse:
    return await get_customer(id_=id_)


@router.delete('/{id_}')
async def _delete_customer(id_: int) -> JSONResponse:
    return await delete_customer(id_=id_)


@router.put('/{id_}')
async def _update_customer(id_: int, customer: CustomerRequest) -> JSONResponse:
    return await update_customer(id_=id_, customer=customer)
