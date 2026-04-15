from typing import override

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import SEARCH_LESSONS_SQL
from src.interfaces.i_lessons_storage import ILessonsStorage
from src.models.db_lesson_model import DbLessonModel
from src.models.db_lesson_to_group import DbLessonToGroupModel
from src.models.db_lesson_to_teacher import DbLessonToTeacherModel
from src.models.full_db_lesson_model import FullDbLessonModel


class LessonsStorage(ILessonsStorage):
    def __init__(self, database: SQLiteDatabase):
        self._db = database

    @override
    def search_lessons(self, search_text: str) -> list[DbLessonModel]:
        list_of_lessons = self._db.fetch_all(SEARCH_LESSONS_SQL, (search_text, ))
        return [DbLessonModel.from_tuple(i) for i in list_of_lessons]

    @override
    def override_lessons(self, lessons: list[FullDbLessonModel], link_groups: list[DbLessonToGroupModel], link_teachers: list[DbLessonToTeacherModel]):
        self._db.begin_transaction()
        self._db.delete("lessons", commit=False)
        self._db.delete("lesson_to_groups", commit=False)
        self._db.delete("lesson_to_teachers", commit=False)

        self._db.insert_many("lessons", [i.db_lesson.to_json() for i in lessons], commit=False)
        self._db.insert_many("lesson_to_groups", [i.to_json() for i in link_groups], commit=False)
        self._db.insert_many("lesson_to_teachers", [i.to_json() for i in link_teachers], commit=False)

        self._db.commit()

