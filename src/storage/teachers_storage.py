from typing import override

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import SEARCH_TEACHERS_SQL
from src.interfaces.i_teachers_storage import ITeachersStorage
from src.models.db_teacher_model import DbTeacherModel


class TeachersStorage(ITeachersStorage):
    def __init__(self, database: SQLiteDatabase):
        self._db = database

    @override
    def search_teacher(self, search_text: str) -> list[DbTeacherModel]:
        list_of_teachers = self._db.fetch_all(SEARCH_TEACHERS_SQL, (search_text, ))
        return [DbTeacherModel.from_tuple(i) for i in list_of_teachers]

    @override
    def override_teachers(self, teachers: list[DbTeacherModel]):
        self._db.begin_transaction()
        self._db.delete("teachers", commit=False)
        self._db.insert_many("teachers", [i.to_json() for i in teachers], commit=False)
        self._db.commit()
