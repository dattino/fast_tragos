from fastapi import FastAPI

from .api import api_router

fast_tragos = FastAPI()

fast_tragos.include_router(api_router)
