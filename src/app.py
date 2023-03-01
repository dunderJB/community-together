from fastapi import FastAPI
from src.entrypoints.routes import health_router
from src.infra.adapters.orm.database.settings import engine, Base
import uvicorn


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(health_router, prefix='/community-together')

if __name__ == '__main__':

    uvicorn.run(app, host='0.0.0.0', port=4001)


