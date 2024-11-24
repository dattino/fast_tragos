# from server.external_interface import tragos_api_client
from server.database import db_connection
from server.database.models import TragoModel


class TragosRepository:
    # last_id: int = 0
    # fake_db: list[dict] = []
    def __init__(self):
        self.db = db_connection.session

    def create(self, nuevo_trago_dict: dict) -> dict:
        # from datetime import datetime
        # now = datetime.now()
        # TragosRepository.last_id += 1
        # nuevo_trago.update(
        #    id=TragosRepository.last_id,
        #    created_at=now,
        #    updated_at=now,
        # )
        # TragosRepository.fake_db.append(nuevo_trago)
        # return nuevo_trago

        nuevo_trago = TragoModel(**nuevo_trago_dict)
        self.db.add(nuevo_trago)
        self.db.commit()
        self.db.refresh(nuevo_trago)
        return self.__to_dict(nuevo_trago)

    def get_list(self, limit: int, offset: int) -> list[dict]:
        # db_size = len(TragosRepository.fake_db)
        # first_index = min(db_size, offset)
        # last_index = min(db_size, (first_index + limit))
        # return TragosRepository.fake_db[first_index:last_index]

        # return tragos_api_client.get_list(limit, offset)

        tragos = self.db.query(TragoModel).order_by(
            'id').limit(limit).offset(limit * offset).all()
        return [self.__to_dict(trago) for trago in tragos]

    def get_by_id(self, trago_id: int) -> dict | None:
        # for trago in TragosRepository.fake_db:
        #    if trago['id'] == id:
        #        return trago

        trago = self.__get_one(trago_id)
        if trago is None:
            return
        return self.__to_dict(trago)

    def update(self, id: int, new_data: dict) -> dict | None:
        # from datetime import datetime
        # now = datetime.now()
        # current_trago = self.get_by_id(id)
        # if current_trago is None:
        #    return
        # current_trago.update(**new_data, update_at=now)
        # return current_trago

        trago = self.__get_one(id)
        if trago is None:
            return
        for field in new_data.keys():
            setattr(trago, field, new_data[field])
        self.db.commit()
        self.db.refresh(trago)
        return self.__to_dict(trago)

    def delete(self, id: int) -> bool:
        # current_trago = self.get_by_id(id)
        # if current_trago is None:
        #    return False
        # TragosRepository.fake_db.remove(current_trago)
        # return True

        trago = self.__get_one(id)
        if trago is None:
            return False
        self.db.delete(trago)
        self.db.commit()
        return True

    def __get_one(self, trago_id: int) -> TragoModel | None:
        return self.db.query(TragoModel).filter_by(id=trago_id).first()

    def __to_dict(self, trago: TragoModel) -> dict:
        return {
            column.name: getattr(trago, column.name)
            for column in TragoModel.__table__.columns
        }
