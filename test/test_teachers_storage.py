import os
import unittest

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_TEACHERS_SQL
from src.models.db_teacher_model import DbTeacherModel
from src.storage.teachers_storage import TeachersStorage
from test.utils import TEST_DATABASE_NAME, json_mock


class TestTeachersStorage(unittest.TestCase):
    def setUp(self):
        self.database = SQLiteDatabase(TEST_DATABASE_NAME)
        self.database.connect()

        if not self.database.table_exists("teachers"):
            self.database.execute_script(CREATE_TABLE_TEACHERS_SQL)
        self.teachers_storage = TeachersStorage(database=self.database)

    def tearDown(self):
        self.database.close()
        if os.path.exists(TEST_DATABASE_NAME):
            os.remove(TEST_DATABASE_NAME)

    def fill_up(self, name: str) -> None:
        sample_teachers_data = json_mock(name)
        sample_teachers = [DbTeacherModel.from_json(i) for i in sample_teachers_data]
        self.database.insert_many("teachers", [teacher.to_json() for teacher in sample_teachers])

    def test_exist_db_file(self):
        self.assertTrue(os.path.exists("test_database.db"))

    def test_search_teachers(self):
        self.fill_up("teachers-3.json")
        result = self.teachers_storage.search_teacher("ва")
        self.assertEqual(result, [
            DbTeacherModel(
                id=674,
                lastname="Аристархова",
                firstname="Анна",
                patronymic="Вячеславовна"
            ),
            DbTeacherModel(
                id=950,
                lastname="Вавулинская",
                firstname="Дарья",
                patronymic="Дмитриевна"
            )
        ])

    def test_empty_search_teachers(self):
        self.fill_up("teachers-3.json")
        result = self.teachers_storage.search_teacher("ып")
        self.assertEqual(result, [])

    def test_override_empty_teachers(self):
        origin_len = len(self.database.select_all("teachers"))
        self.assertEqual(origin_len, 0)

        db_model = DbTeacherModel(
            id=100,
            lastname="lastname",
            firstname="firstname",
            patronymic="patronymic"
        )
        self.teachers_storage.override_teachers([db_model])

        raw_all_teachers = self.database.select_all("teachers")
        all_teachers = [DbTeacherModel.from_tuple(i) for i in raw_all_teachers]
        self.assertEqual(all_teachers, [db_model])

    def test_override_already_exists_teachers(self):
        self.fill_up("teachers-1.json")
        origin_len = len(self.database.select_all("teachers"))
        self.assertEqual(origin_len, 1)

        models = [
            DbTeacherModel(
                id=100,
                lastname="lastname",
                firstname="firstname",
                patronymic="patronymic"
            ),
            DbTeacherModel(
                id=235,
                lastname="Клыпин",
                firstname="Игорь",
                patronymic="Андреевич"
            )
        ]

        self.teachers_storage.override_teachers(models)

        raw_all_teachers = self.database.select_all("teachers")
        all_teachers = [DbTeacherModel.from_tuple(i) for i in raw_all_teachers]
        self.assertEqual(all_teachers, models)
