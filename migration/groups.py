import argparse

import urllib3
from urllib3.exceptions import InsecureRequestWarning

from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_GROUPS_SQL
from src.interfaces.i_groups_storage import IGroupsStorage
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.models.db_group_model import DbGroupModel
from src.repositories.schedule_repository import ScheduleRepository
from src.storage.groups_storage import GroupsStorage

urllib3.disable_warnings(InsecureRequestWarning)


def migrate(
    groups_storage: IGroupsStorage,
    schedule_repository: IScheduleRepository,
):
    print("Migration starting")
    origin_list_of_groups = schedule_repository.fetch_groups("")
    print("Success groups fetched")
    list_of_groups = [DbGroupModel.from_origin_group_info(group) for group in origin_list_of_groups]
    groups_storage.override_groups(list_of_groups)


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser("default")
    args_parser.add_argument(
        "--config",
        help="path to config file (default=\".env\")",
        default=".env"
    )
    args = args_parser.parse_args()

    config = Config(path_env=args.config)
    db = SQLiteDatabase(db_path=config.database_path)
    repository = ScheduleRepository(config.base_schedule_api_url)
    storage = GroupsStorage(db)

    with db:
        if not db.table_exists("groups"):
            db.execute_script(CREATE_TABLE_GROUPS_SQL)
        migrate(storage, repository)

    print("Migration complete")
