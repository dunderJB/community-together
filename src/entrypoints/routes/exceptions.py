from http import HTTPStatus
import re
from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError, OperationalError, NoResultFound
from starlette.requests import Request
from starlette.responses import JSONResponse


def get_field_error(field_error: str):
    field = re.search(r'\((.*?)\)', field_error)
    return field.group(0)


class ExceptionHandler:
    def __init__(self, app: FastAPI):
        app.exception_handler(IntegrityError)(self.integrity_error_handler)
        app.exception_handler(OperationalError)(self.operational_error_handler)
        app.exception_handler(NoResultFound)(self.no_result_found_handler)
        app.exception_handler(Exception)(self.exception_handler)

    @staticmethod
    async def integrity_error_handler(_: Request, exc: IntegrityError):
        error_code = exc.orig.pgcode
        field_error = get_field_error(exc.orig.diag.message_detail)
        if error_code == "23505":
            return JSONResponse({
                "detail":  f'{field_error} em uso.',
                "status_code": HTTPStatus.CONFLICT
            }, status_code=HTTPStatus.CONFLICT)

        return JSONResponse({
            "detail": "Erro ao inserir dados.",
            "status_code": HTTPStatus.INTERNAL_SERVER_ERROR
        }, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

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

