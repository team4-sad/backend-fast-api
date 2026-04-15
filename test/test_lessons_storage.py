import os
import unittest

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_LESSONS_SQL
from src.models.db_lesson_model import DbLessonModel
from src.storage.lessons_storage import LessonsStorage
from test.utils import TEST_DATABASE_NAME, json_mock


class TestLessonsStorage(unittest.TestCase):
    def setUp(self):
        self.database = SQLiteDatabase(TEST_DATABASE_NAME)
        self.database.connect()

        if not self.database.table_exists("lessons"):
            self.database.execute_script(CREATE_TABLE_LESSONS_SQL)
        self.lessons_storage = LessonsStorage(database=self.database)

    def tearDown(self):
        self.database.close()
        if os.path.exists(TEST_DATABASE_NAME):
            os.remove(TEST_DATABASE_NAME)

    def fill_up(self, name: str) -> None:
        sample_lessons_data = json_mock(name)
        sample_lessons = [DbLessonModel.from_json(i) for i in sample_lessons_data]
        self.database.insert_many("lessons", [lesson.to_json() for lesson in sample_lessons])

    def test_exist_db_file(self):
        self.assertTrue(os.path.exists("test_database.db"))

    def test_search_lessons(self):
        self.fill_up("lessons-3.json")
        result = self.lessons_storage.search_lessons("ст")
        self.assertEqual(result, [
            DbLessonModel(
                id="950",
                classroom_id=608,
                week_type=1,
                day_of_week=2,
                subject="Операционные системы",
                lesson_type="Лекционные занятия"
            ),
            DbLessonModel(
                week_type=1,
                day_of_week=2,
                id="952",
                classroom_id=608,
                subject="История градостроительства",
                lesson_type="Лекционные занятия"
            )
        ])

    def test_empty_search_lessons(self):
        self.fill_up("lessons-3.json")
        result = self.lessons_storage.search_lessons("ып")
        self.assertEqual(result, [])

    def test_override_empty_lessons(self):
        origin_len = len(self.database.select_all("lessons"))
        self.assertEqual(origin_len, 0)

        db_model = DbLessonModel(
            id="200",
            classroom_id=100,
            day_of_week=2,
            week_type=1,
            subject="subject",
            lesson_type="lesson_type"
        )
        self.lessons_storage.override_lessons([db_model])

        raw_all_lessons = self.database.select_all("lessons")
        all_lessons = [DbLessonModel.from_tuple(i) for i in raw_all_lessons]
        self.assertEqual(all_lessons, [db_model])

    def test_override_already_exists_lessons(self):
        self.fill_up("lessons-1.json")
        origin_len = len(self.database.select_all("lessons"))
        self.assertEqual(origin_len, 1)

        models = [
            DbLessonModel(
                id="202",
                classroom_id=101,
                day_of_week=3,
                week_type=1,
                subject="other_subject",
                lesson_type="other_lesson_type"
            ),
            DbLessonModel(
                id="204",
                classroom_id=102,
                day_of_week=4,
                week_type=0,
                subject="one_another_subject",
                lesson_type="one_another_lesson_type"
            )
        ]

        self.lessons_storage.override_lessons(models)

        raw_all_lessons = self.database.select_all("lessons")
        all_lessons = [DbLessonModel.from_tuple(i) for i in raw_all_lessons]
        self.assertEqual(all_lessons, models)
