from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.tragos_schemas import NuevoTragoRequest, TragoResponse, TragoRequest
from server.controller import TragosController
from server.exception import InternalServerError, NotFound

router = APIRouter(prefix='/tragos')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = TragosController()


@router.post(
    '',
    status_code=201,
    responses={
        201: {'description': 'Trago Creado'},
    },
    description='Crea una nueva bebida para hacer tragos, con los campos pasado por BODY Param. Falla si faltan algunos campos obligatorios',
)
async def create(nuevo_trago: NuevoTragoRequest) -> TragoResponse:
    return controller.create(nuevo_trago)


@router.get(
    '',
    status_code=200,
    responses={
        200: {'description': 'Listado de tragos'}
    },
    description='Retorna una lista paginada con los proyectos del usuario. Si no hay proyectos para mostrar, retorna una lista vacía',
)
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[TragoResponse]:
    print(f'Paginado límite {limit} y offset {offset}')
    return controller.get_list(limit, offset)


@router.get(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Bebida encontrada'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Retorna un trago por ID. Falla si el ID no existe',
)
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> TragoResponse:
    return controller.get_by_id(id)


@router.patch(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Bebida actualizada'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Actualiza un trago con la información por Body Param. Falla si el ID no existe',
)
async def update(id: Annotated[int, Path(ge=1)], trago: TragoRequest) -> TragoResponse:
    return controller.update(id, trago)


@router.delete(
    '/{id}',
    status_code=204,
    responses={
        204: {'description': 'Trago eliminado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Elimina un proyecto con id pasado por Path Param. Falla si el ID no existe',
)
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    controller.delete(id)
