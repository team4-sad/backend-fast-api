import argparse

import urllib3
from urllib3.exceptions import InsecureRequestWarning

from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_TEACHERS_SQL
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.interfaces.i_teacher_storage import ITeachersStorage
from src.models.db_teacher_model import DbTeacherModel
from src.repositories.schedule_repository import ScheduleRepository
from src.storage.teachers_storage import TeachersStorage

urllib3.disable_warnings(InsecureRequestWarning)


def migrate(
    teachers_storage: ITeachersStorage,
    schedule_repository: IScheduleRepository,
):
    print("Migration starting")
    origin_list_of_teachers = schedule_repository.fetch_teachers("")
    print("Success groups fetched")
    list_of_teachers = [DbTeacherModel.from_origin_teacher_info(teacher) for teacher in origin_list_of_teachers]
    teachers_storage.override_teachers(list_of_teachers)


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
    storage = TeachersStorage(db)

    with db:
        if not db.table_exists("teachers"):
            db.execute_script(CREATE_TABLE_TEACHERS_SQL)
        migrate(storage, repository)

    print("Migration complete")
