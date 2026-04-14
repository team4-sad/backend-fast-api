import argparse

import urllib3
from urllib3.exceptions import InsecureRequestWarning

from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_CLASSROOMS_SQL
from src.interfaces.i_classrooms_storage import IClassroomsStorage
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.models.db_classroom_model import DbClassroomModel
from src.repositories.schedule_repository import ScheduleRepository
from src.storage.classrooms_storage import ClassroomsStorage

urllib3.disable_warnings(InsecureRequestWarning)


def migrate(
    classrooms_storage: IClassroomsStorage,
    schedule_repository: IScheduleRepository,
):
    print("Migration starting")
    row_classrooms = schedule_repository.fetch_classrooms("")
    print("Success groups fetched")
    classrooms = [DbClassroomModel.from_origin(classroom) for classroom in row_classrooms]
    classrooms_storage.override_classrooms(classrooms)


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
    storage = ClassroomsStorage(db)

    with db:
        if not db.table_exists("classrooms"):
            db.execute_script(CREATE_TABLE_CLASSROOMS_SQL)
        migrate(storage, repository)

    print("Migration complete")
