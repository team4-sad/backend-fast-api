from typing import override

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import SEARCH_LESSONS_SQL
from src.interfaces.i_lessons_storage import ILessonsStorage
from src.models.db_lesson_model import DbLessonModel


class LessonsStorage(ILessonsStorage):
    def __init__(self, database: SQLiteDatabase):
        self._db = database

    @override
    def search_lessons(self, search_text: str) -> list[DbLessonModel]:
        list_of_lessons = self._db.fetch_all(SEARCH_LESSONS_SQL, (search_text, ))
        return [DbLessonModel.from_tuple(i) for i in list_of_lessons]

    @override
    def override_lessons(self, lessons: list[DbLessonModel]):
        self._db.begin_transaction()
        self._db.delete("lessons", commit=False)
        self._db.insert_many("lessons", [i.to_json() for i in lessons], commit=False)
        self._db.commit()

