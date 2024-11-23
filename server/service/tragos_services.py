from typing import List

from server.schemas.tragos_schemas import NuevoTragoRequest, TragoResponse, TragoRequest
from server.exception import NotFound


class TragosService:
    last_id: int = 0
    fake_db: list[dict] = []

    def __init__(self):
        pass

    def create(self, nuevo_trago: NuevoTragoRequest) -> TragoResponse:
        trago_dict = self.__fake_create(nuevo_trago.model_dump())
        return TragoResponse(**trago_dict)

    def get_list(self, limit: int, offset: int) -> List[TragoResponse]:
        trago_list = self.__fake_get_list(limit, offset)
        return [TragoResponse(**trago) for trago in trago_list]

    def get_by_id(self, id: int) -> TragoResponse:
        trago = self.__fake_get_by_id(id)
        if trago is None:
            raise NotFound(f'Trago con id #{id} no encontrado')
        return TragoResponse(**trago)

    def update(self, id, new_data) -> TragoResponse:
        updated_trago = self.__fake_update(
            id, new_data.model_dump(exclude_none=True))
        if updated_trago is None:
            raise NotFound(f'Trago con id #{id} no encontrado para actualizarse')
        return TragoResponse(**updated_trago)

    def delete(self, id: int) -> None:
        if not self.__fake_delete(id):
            raise NotFound(f'Trago con id #{id} no encontrado para eliminarse')
        

    # FAKE METHODS
    def __fake_create(self, nuevo_trago: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        TragosService.last_id += 1
        nuevo_trago.update(
            id=TragosService.last_id,
            created_at=now,
            updated_at=now,
        )
        TragosService.fake_db.append(nuevo_trago)
        return nuevo_trago

    def __fake_get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(TragosService.fake_db)
        first_index = min(db_size, offset)
        last_index = min((db_size - first_index), limit)
        return TragosService.fake_db[first_index:last_index]

    def __fake_get_by_id(self, id: int) -> dict | None:
        for trago in TragosService.fake_db:
            if trago['id'] == id:
                return trago

    def __fake_update(self, id, new_data) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_trago = self.__fake_get_by_id(id)
        if current_trago is None:
            return
        current_trago.update(**new_data, update_at=now)
        return current_trago

    def __fake_delete(self, id: int) -> bool:
        current_trago = self.__fake_get_by_id(id)
        if current_trago is None:
            return False
        TragosService.fake_db.remove(current_trago)
        return True
