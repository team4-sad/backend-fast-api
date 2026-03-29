import os
import unittest

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_GROUPS_SQL
from src.models.db_group_model import DbGroupModel
from src.storage.groups_storage import GroupsStorage
from test.utils import TEST_DATABASE_NAME, json_mock


class TestGroupsStorage(unittest.TestCase):
    def setUp(self):
        self.database = SQLiteDatabase(TEST_DATABASE_NAME)
        self.database.connect()

        if not self.database.table_exists("groups"):
            self.database.execute_script(CREATE_TABLE_GROUPS_SQL)
        self.groups_storage = GroupsStorage(database=self.database)

    def tearDown(self):
        self.database.close()
        if os.path.exists(TEST_DATABASE_NAME):
            os.remove(TEST_DATABASE_NAME)

    def fill_up(self, name: str) -> None:
        sample_groups = json_mock(name)
        self.database.insert_many("groups", sample_groups)

    def test_exist_db_file(self):
        self.assertTrue(os.path.exists("test_database.db"))

    def test_search_groups(self):
        self.fill_up("groups-3.json")
        result = self.groups_storage.search_groups("ГФ")
        self.assertEqual(result, [
            DbGroupModel(
                id=950,
                name='2019-ГФ-ПГ-1с(до)',
                year=2019,
                faculty='ГФ',
                department='ПГ',
                group='1с(до)'
            ),
            DbGroupModel(
                id=1380,
                name='2024-ГФ-ГиДЗг-1м',
                year=2024,
                faculty='ГФ',
                department='ГиДЗг',
                group='1м'
            )
        ])

    def test_empty_search_groups(self):
        self.fill_up("groups-3.json")
        result = self.groups_storage.search_groups("2025")
        self.assertEqual(result, [])

    def test_override_empty_groups(self):
        origin_len = len(self.database.select_all("groups"))
        self.assertEqual(origin_len, 0)

        db_model = DbGroupModel(
            id=1380,
            name='2024-ГФ-ГиДЗг-1м',
            year=2024,
            faculty='ГФ',
            department='ГиДЗг',
            group='1м'
        )
        self.groups_storage.override_groups([db_model])

        raw_all_groups = self.database.select_all("groups")
        all_groups = [DbGroupModel.from_tuple(i) for i in raw_all_groups]
        self.assertEqual(all_groups, [db_model])

    def test_override_already_exists_groups(self):
        self.fill_up("groups-1.json")
        origin_len = len(self.database.select_all("groups"))
        self.assertEqual(origin_len, 1)

        models = [
            DbGroupModel(
                id=950,
                name='2019-ГФ-ПГ-1с(до)',
                year=2019,
                faculty='ГФ',
                department='ПГ',
                group='1с(до)'
            ),
            DbGroupModel(
                id=1380,
                name='2024-ГФ-ГиДЗг-1м',
                year=2024,
                faculty='ГФ',
                department='ГиДЗг',
                group='1м'
            )
        ]

        self.groups_storage.override_groups(models)

        raw_all_groups = self.database.select_all("groups")
        all_groups = [DbGroupModel.from_tuple(i) for i in raw_all_groups]
        self.assertEqual(all_groups, models)
