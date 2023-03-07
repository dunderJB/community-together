from fastapi import APIRouter
from src.entrypoints.routes.health_check import health_router
from src.entrypoints.routes.v1 import router as v1_router
from src.entrypoints.routes.exceptions import ExceptionHandler

router = APIRouter()
router.include_router(health_router, prefix='/health-check')
router.include_router(v1_router, prefix='/v1')
