

class TragosRepository:
    last_id: int = 0
    fake_db: list[dict] = []

    def create(self, nuevo_trago: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        TragosRepository.last_id += 1
        nuevo_trago.update(
            id=TragosRepository.last_id,
            created_at=now,
            updated_at=now,
        )
        TragosRepository.fake_db.append(nuevo_trago)
        return nuevo_trago

    def get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(TragosRepository.fake_db)
        first_index = min(db_size, offset)
        last_index = min(db_size, (first_index + limit))
        return TragosRepository.fake_db[first_index:last_index]

    def get_by_id(self, id: int) -> dict | None:
        for trago in TragosRepository.fake_db:
            if trago['id'] == id:
                return trago

    def update(self, id, new_data) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_trago = self.get_by_id(id)
        if current_trago is None:
            return
        current_trago.update(**new_data, update_at=now)
        return current_trago

    def delete(self, id: int) -> bool:
        current_trago = self.get_by_id(id)
        if current_trago is None:
            return False
        TragosRepository.fake_db.remove(current_trago)
        return True
