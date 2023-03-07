from fastapi import APIRouter
from datetime import datetime

health_router = APIRouter()


@health_router.get('/')
async def health_check():
    time_now = datetime.now()
    return {
        "Status": "Working!",
        "time_now": time_now
    }

