from typing import List

from fastapi import HTTPException


from server.schemas.tragos_schemas import NuevoTragoRequest, TragoResponse, TragoRequest
from server.exception import BaseHTTPException, InternalServerError, NotFound


class TragosController:
    def __init__(self):
        pass

    def create(self, nuevo_trago: NuevoTragoRequest) -> TragoResponse:
        try:
            return TragoResponse(id=1, **nuevo_trago.model_dump())
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[TragoResponse]:
        try:
            return
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def get_by_id(self, id: int) -> TragoResponse:
        try:
            raise NotFound(f'Trago #{id} no encontrado')
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def update(self, id, new_data) -> TragoResponse:
        try:
            return TragoResponse(id=id, **new_data.model_dump())
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            return
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()
