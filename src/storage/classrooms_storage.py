from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import SEARCH_CLASSROOM_SQL
from src.interfaces.i_classrooms_storage import IClassroomsStorage
from src.models.db_classroom_model import DbClassroomModel


class ClassroomsStorage(IClassroomsStorage):
    def __init__(self, database: SQLiteDatabase):
        self._db = database

    def override_classrooms(self, classrooms: list[DbClassroomModel]):
        self._db.begin_transaction()
        self._db.delete("classrooms", commit=False)
        self._db.insert_many("classrooms", [i.to_json() for i in classrooms], commit=False)
        self._db.commit()

    def search_classroom(self, search_text: str) -> list[DbClassroomModel]:
        classrooms = self._db.fetch_all(SEARCH_CLASSROOM_SQL, (search_text,))
        return [DbClassroomModel.from_tuple(i) for i in classrooms]

    def get_all_classrooms(self) -> list[DbClassroomModel]:
        classrooms = self._db.select_all("classrooms")
        return [DbClassroomModel.from_tuple(i) for i in classrooms]
