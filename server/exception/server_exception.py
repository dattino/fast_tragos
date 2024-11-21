from .base_htttp_exception import BaseHTTPException


class InternalServerError(BaseHTTPException):
    description = 'Error no contemplado contacte al sysadmin'
    status_code = 500


class NotImplemented(BaseHTTPException):
    description = 'Funcionalidad no implementada'
    status_code = 501
