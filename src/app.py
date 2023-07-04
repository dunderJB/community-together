from fastapi import FastAPI

from src.entrypoints.routes import router
from src.entrypoints.routes.exceptions import ExceptionHandler
import uvicorn

app = FastAPI()

app.include_router(router, prefix='/community-together')
ExceptionHandler(app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=4001)
