from fastapi import FastAPI

from src.infra.adapters.orm.database.settings import engine, Base
from src.entrypoints.routes import router
from src.infra.adapters.orm.models.customer import Customer
from src.entrypoints.routes.exceptions import ExceptionHandler

import uvicorn


Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(router, prefix='/community-together')
ExceptionHandler(app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=4001)
