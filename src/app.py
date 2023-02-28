from fastapi import FastAPI
from src.entrypoints.routes import health_router
import uvicorn


app = FastAPI()

app.include_router(health_router, prefix='/community-together')

if __name__ == '__main__':

    uvicorn.run(app, host='0.0.0.0', port=4001)


