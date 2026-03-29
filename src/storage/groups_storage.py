from typing import override

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import SEARCH_GROUPS_SQL
from src.interfaces.i_groups_storage import IGroupsStorage
from src.models.db_group_model import DbGroupModel


class GroupsStorage(IGroupsStorage):
    def __init__(self, database: SQLiteDatabase):
        self._db = database

    @override
    def search_groups(self, search_text: str) -> list[DbGroupModel]:
        list_of_groups = self._db.fetch_all(SEARCH_GROUPS_SQL, (search_text, ))
        return [DbGroupModel.from_tuple(i) for i in list_of_groups]

    @override
    def override_groups(self, groups: list[DbGroupModel]):
        self._db.begin_transaction()
        self._db.delete("groups", commit=False)
        self._db.insert_many("groups", [i.to_json() for i in groups])
        self._db.commit()
