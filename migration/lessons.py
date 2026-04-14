import argparse
import datetime

import urllib3
from urllib3.exceptions import InsecureRequestWarning

from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_LESSONS_SQL
from src.interfaces.i_groups_storage import IGroupsStorage
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.interfaces.i_lessons_storage import ILessonsStorage
from src.models.db_lesson_model import DbLessonModel
from src.repositories.schedule_repository import ScheduleRepository
from src.storage.lessons_storage import LessonsStorage
from src.utils.datetime_utils import get_monday_datetime, get_sunday_datetime, is_prime_week, date2str

urllib3.disable_warnings(InsecureRequestWarning)


def migrate(
    lessons_storage: ILessonsStorage,
    group_storage: IGroupsStorage,
    schedule_repository: IScheduleRepository,
):
    print("Migration starting")

    now = datetime.datetime.now()
    current_monday = get_monday_datetime(now)
    current_sunday = get_sunday_datetime(now)
    current_week_is_prime = is_prime_week(now)
    prev_monday = current_monday - datetime.timedelta(days=7)
    prev_sunday = current_sunday - datetime.timedelta(days=7)
    prev_week_is_prime = is_prime_week(prev_monday)
    print(f"Migration schedule meta-data:\n"
          f"{current_monday=}\n{current_sunday=}\n{current_week_is_prime=}\n"
          f"{prev_monday=}\n{prev_sunday=}\n{prev_week_is_prime=}")

    all_groups = group_storage.get_all_groups()
    print("Success all groups fetched")

    len_ = len(all_groups)

    for index, group in enumerate(all_groups):
        print(f"{index+1}/{len_} Fetch group {group} for current week")
        current_schedule = schedule_repository.fetch_group(str(group.id), date2str(current_monday), date2str(current_sunday))
        prev_schedule = schedule_repository.fetch_group(str(group.id), date2str(prev_monday), date2str(prev_sunday))


    origin_list_of_lessons = schedule_repository.fetch_lessons("")
    list_of_lessons = [DbLessonModel.from_origin_lesson_info(lesson) for lesson in origin_list_of_lessons]
    lessons_storage.override_lessons(list_of_lessons)


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
    storage = LessonsStorage(db)

    with db:
        if not db.table_exists("lessons"):
            db.execute_script(CREATE_TABLE_LESSONS_SQL)
        migrate(storage, repository)

    print("Migration complete")
