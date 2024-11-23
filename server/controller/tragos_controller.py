from typing import List


from server.schemas.tragos_schemas import NuevoTragoRequest, TragoResponse, TragoRequest
from server.exception import BaseHTTPException, InternalServerError, NotFound
from server.service import TragosService


class TragosController:
    def __init__(self):
        self.service = TragosService()

    def create(self, nuevo_trago: NuevoTragoRequest) -> TragoResponse:
        try:
            return self.service.create(nuevo_trago)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[TragoResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def get_by_id(self, id: int) -> TragoResponse:
        try:
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def update(self, id, new_data) -> TragoResponse:
        try:
            return self.service.update(id, new_data)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            self.service.delete(id)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()
