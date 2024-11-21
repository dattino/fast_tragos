from fastapi import APIRouter

from .tragos_routes import router as tragos_router


router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(tragos_router, tags=['Projects'])
