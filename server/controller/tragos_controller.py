import logging
from typing import List


from server.schemas.tragos_schemas import NuevoTragoRequest, TragoResponse, TragoRequest
from server.exception import BaseHTTPException, InternalServerError, NotFound
from server.service import TragosService


logger = logging.getLogger(__name__)

class TragosController:
    def __init__(self):
        self.service = TragosService()

    def create(self, nuevo_trago: NuevoTragoRequest) -> TragoResponse:
        try:
            logger.debug(f'Crear trago {nuevo_trago.title}')
            return self.service.create(nuevo_trago)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.create()')
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[TragoResponse]:
        try:
            logger.debug(f'Lista de tragos con limit = {limit} y offset = {offset}')
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.get_list()' + str(ex))
            raise InternalServerError()

    def get_by_id(self, id: int) -> TragoResponse:
        try:
            logger.debug(f'Buscar trago #{id}')
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.get_by_id()')
            raise InternalServerError()

    def update(self, id, new_data) -> TragoResponse:
        try:
            logger.debug(f'Actualizar trago #{id}')
            return self.service.update(id, new_data)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.update()')
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            logger.debug(f'Borrar trago #{id}')
            self.service.delete(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.delete()')
            raise InternalServerError()
        
    def  __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >=500:
            logger.critical(f'Error en el servidor con status code {ex.status_code}: {ex.description}')
        else:
            logger.error(f'Error {ex.status_code}: {ex.description}')            
        raise ex
