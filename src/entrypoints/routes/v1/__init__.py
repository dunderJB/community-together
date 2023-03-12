from fastapi import APIRouter
from src.entrypoints.routes.v1 import customer


router = APIRouter()
router.include_router(customer.router, prefix='/customer')

