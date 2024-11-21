from fastapi import APIRouter

router = APIRouter(prefix='/tragos')


@router.get('/')
async def get_all() -> list:
    return []

@router.post('/')
async def get_all() -> dict:
    return {}