from http import HTTPStatus
from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError, OperationalError, NoResultFound
from starlette.requests import Request
from starlette.responses import JSONResponse


class ExceptionHandler:
    def __init__(self, app: FastAPI):
        app.exception_handler(IntegrityError)(self.integrity_error_handler)
        app.exception_handler(OperationalError)(self.operational_error_handler)
        app.exception_handler(NoResultFound)(self.no_result_found_handler)
        app.exception_handler(Exception)(self.exception_handler)

    @staticmethod
    async def integrity_error_handler(_: Request, exc: IntegrityError):
        error_code = exc.orig.pgcode

        if error_code == "23505":
            return JSONResponse({
                "detail": "Email em uso.",
                "status_code": HTTPStatus.CONFLICT
            }, status_code=HTTPStatus.CONFLICT)

    @staticmethod
    async def operational_error_handler(_: Request, __: OperationalError):
        return JSONResponse({
            "detail": "Erro interno do servidor durante a execução.",
            "status_code": HTTPStatus.INTERNAL_SERVER_ERROR
        }, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

    @staticmethod
    async def no_result_found_handler(_: Request, __: NoResultFound):
        return JSONResponse({
            "detail": "Usuário não encontrado no banco de dados.",
            "status_code": HTTPStatus.NOT_FOUND
        }, status_code=HTTPStatus.NOT_FOUND)

    @staticmethod
    async def exception_handler():
        return JSONResponse({
            "detail": "Erro interno do servidor.",
            "status_code": HTTPStatus.NOT_FOUND
        }, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
