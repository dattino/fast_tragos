from typing import List

from server.schemas.tragos_schemas import NuevoTragoRequest, TragoResponse, TragoRequest
from server.exception import NotFound
from server.repository import TragosRepository


class TragosService:

    def __init__(self):
        self.trago_repo = TragosRepository()

    def create(self, nuevo_trago: NuevoTragoRequest) -> TragoResponse:
        trago_dict = self.trago_repo.create(nuevo_trago.model_dump())
        return TragoResponse(**trago_dict)

    def get_list(self, limit: int, offset: int) -> List[TragoResponse]:
        trago_list = self.trago_repo.get_list(limit, offset)
        return [TragoResponse(**trago) for trago in trago_list]

    def get_by_id(self, id: int) -> TragoResponse:
        trago = self.trago_repo.get_by_id(id)
        if trago is None:
            raise NotFound(f'Trago con id #{id} no encontrado')
        return TragoResponse(**trago)

    def update(self, id, new_data) -> TragoResponse:
        updated_trago = self.trago_repo.update(
            id, new_data.model_dump(exclude_none=True)
        )
        if updated_trago is None:
            raise NotFound(
                f'Trago con id #{id} no encontrado para actualizarse'
            )
        return TragoResponse(**updated_trago)

    def delete(self, id: int) -> None:
        if not self.trago_repo.delete(id):
            raise NotFound(
                f'Trago con id #{id} no encontrado para eliminarse'
            )
