# import logging

from fastapi import FastAPI

from .api import api_router


# logger = logging.getLogger(__name__)
fast_tragos = FastAPI()

# Incluimos el router principal a la instancia de FastAPI
fast_tragos.include_router(api_router)


# @fast_tragos.on_event('startup')
# async def startup_event():
#     logger.debug('API Iniciada')


# @fast_tragos.on_event('shutdown')
# def shutdown_event():
#     logger.debug('API Finalizada')