from fastapi import APIRouter
from src.entrypoints.routes.health_check import health_router

router = APIRouter()
router.include_router(health_router)

