import os
import unittest

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_CLASSROOMS_SQL
from src.models.db_classroom_model import DbClassroomModel
from src.storage.classrooms_storage import ClassroomsStorage
from test.utils import TEST_DATABASE_NAME, json_mock


class TestClassroomsStorage(unittest.TestCase):
    def setUp(self):
        self.database = SQLiteDatabase(TEST_DATABASE_NAME)
        self.database.connect()

        if not self.database.table_exists("classrooms"):
            self.database.execute_script(CREATE_TABLE_CLASSROOMS_SQL)
        self.classrooms_storage = ClassroomsStorage(database=self.database)

    def tearDown(self):
        self.database.close()
        if os.path.exists(TEST_DATABASE_NAME):
            os.remove(TEST_DATABASE_NAME)

    def fill_up(self, name: str) -> None:
        sample_classrooms = json_mock(name)
        self.database.insert_many("classrooms", sample_classrooms)

    def test_exist_db_file(self):
        self.assertTrue(os.path.exists("test_database.db"))

    def test_search_classrooms(self):
        self.fill_up("classrooms-3.json")
        result = self.classrooms_storage.search_classroom("50")
        self.assertEqual(result, [
            DbClassroomModel(
                id=336,
                name='450'
            ),
            DbClassroomModel(
                id=411,
                name='507 к.2'
            )
        ])

    def test_empty_search_classrooms(self):
        self.fill_up("classrooms-3.json")
        result = self.classrooms_storage.search_classroom("600")
        self.assertEqual(result, [])

    def test_override_empty_classrooms(self):
        origin_len = len(self.database.select_all("classrooms"))
        self.assertEqual(origin_len, 0)

        db_model = DbClassroomModel(
            id=1380,
            name='600'
        )
        self.classrooms_storage.override_classrooms([db_model])

        raw_all_classrooms = self.database.select_all("classrooms")
        all_classrooms = [DbClassroomModel.from_tuple(i) for i in raw_all_classrooms]
        self.assertEqual(all_classrooms, [db_model])

    def test_override_already_exists_classrooms(self):
        self.fill_up("classrooms-1.json")
        origin_len = len(self.database.select_all("classrooms"))
        self.assertEqual(origin_len, 1)

        models = [
            DbClassroomModel(
                id=336,
                name='450'
            ),
            DbClassroomModel(
                id=411,
                name='507 к.2'
            )
        ]

        self.classrooms_storage.override_classrooms(models)

        raw_all_classrooms = self.database.select_all("classrooms")
        all_classrooms = [DbClassroomModel.from_tuple(i) for i in raw_all_classrooms]
        self.assertEqual(all_classrooms, models)
