from fastapi import APIRouter

router = APIRouter(prefix='/tragos')


@router.get(
    '',
    status_code=200,
    responses={
        200: {'description': 'Listado de tragos'}
    },
    description='Retorna una lista paginada con los proyectos del usuario. Si no hay proyectos para mostrar, retorna una lista vacía'
)
async def get_list() -> list:
    return []


@router.post(
    '',
    status_code=201,
    responses={
        201: {'description': 'Trago Creado'},
    },
    description='Crea una nueva bebida para hacer tragos, con los campos pasado por BODY Param. Falla si faltan algunos campos obligatorios'
)
async def create() -> dict:
    return {}


@router.get(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Bebida encontrada'},
        422: {'description': 'ID no es un entero válido'},
    },
    description='Retorna un trago por ID. Falla si el ID no existe'
)
async def get_by_id(id: int) -> dict:
    return {'id': id}


@router.patch(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Bebida actualizada'},
        422: {'description': 'ID no es un entero válido'},
    },
    description='Actualiza un trago con la información por Body Param. Falla si el ID no existe'
)
async def update(id: int) -> dict:
    return {'id': id}


@router.delete(
    '/{id}',
    status_code=204,
    responses={
        204: {'description': 'Trago eliminado'},
        422: {'description': 'ID no es un entero válido'},
    },
    description='Elimina un proyecto con id pasado por Path Param. Falla si el ID no existe'
)
async def delete(id: int) -> None:
    return None
