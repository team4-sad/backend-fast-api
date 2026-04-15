import argparse
import datetime
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from src.common.datetime_utils import *
from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_LESSONS_SQL, CREATE_TABLE_LESSON_TO_TEACHERS_SQL, \
    CREATE_TABLE_LESSON_TO_GROUPS_SQL
from src.interfaces.i_classrooms_storage import IClassroomsStorage
from src.interfaces.i_groups_storage import IGroupsStorage
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.interfaces.i_lessons_storage import ILessonsStorage
from src.interfaces.i_teachers_storage import ITeachersStorage
from src.models.full_db_lesson_model import FullDbLessonModel
from src.repositories.schedule_repository import ScheduleRepository
from src.storage.classrooms_storage import ClassroomsStorage
from src.storage.groups_storage import GroupsStorage
from src.storage.lessons_storage import LessonsStorage
from src.storage.teachers_storage import TeachersStorage

urllib3.disable_warnings(InsecureRequestWarning)


def migrate(
    lessons_storage: ILessonsStorage,
    group_storage: IGroupsStorage,
    teachers_storage: ITeachersStorage,
    classrooms_storage: IClassroomsStorage,
    schedule_repository: IScheduleRepository,
):
    now = datetime.now()
    current_monday = get_monday_datetime(now)
    current_sunday = get_sunday_datetime(now)
    current_week_is_prime = is_prime_week(now)
    prev_monday = current_monday - timedelta(days=7)
    prev_sunday = current_sunday - timedelta(days=7)
    prev_week_is_prime = is_prime_week(prev_monday)

    print(f"Migration will take place from {date2strDMY(prev_monday)} to {date2strDMY(current_sunday)}")
    print(f"Migration schedule metadata:\n"
          f"{current_monday=}\n{current_sunday=}\n{current_week_is_prime=}\n"
          f"{prev_monday=}\n{prev_sunday=}\n{prev_week_is_prime=}")

    all_groups = group_storage.get_all_groups()
    print("Success all groups fetched")
    group_name_to_id = {i.name: i.id for i in all_groups}

    all_teachers = teachers_storage.get_all_teachers()
    print("Success all teachers fetched")
    fio_to_id = {i.fio: i.id for i in all_teachers}

    all_classrooms = classrooms_storage.get_all_classrooms()
    print("Success all classrooms fetched")

    len_ = len(all_classrooms)

    new_lessons = []
    new_link_groups = []
    new_link_teachers = []

    for index, classroom in enumerate(all_classrooms):
        print(f"{index + 1}/{len_} Fetch classroom '{classroom.name}'")

        current_schedule = schedule_repository.fetch_classroom(
            str(classroom.id),
            date2strYMD(current_monday),
            date2strYMD(current_sunday)
        ).schedule
        current_lessons, current_link_groups, current_link_teachers = FullDbLessonModel.from_schedule(current_schedule, group_name_to_id, fio_to_id)
        new_lessons.extend(current_lessons)
        new_link_groups.extend(current_link_groups)
        new_link_teachers.extend(current_link_teachers)
        print(f"(current week) Added {len(current_lessons)} lessons, current size={len(new_lessons)}")

        prev_schedule = schedule_repository.fetch_classroom(
            str(classroom.id),
            date2strYMD(prev_monday),
            date2strYMD(prev_sunday)
        ).schedule
        prev_lessons, prev_link_groups, prev_link_teachers = FullDbLessonModel.from_schedule(prev_schedule, group_name_to_id, fio_to_id)
        new_lessons.extend(prev_lessons)
        new_link_groups.extend(prev_link_groups)
        new_link_teachers.extend(prev_link_teachers)
        print(f"(previous week) Added {len(prev_lessons)} lessons, current size={len(new_lessons)}")

    print("Start override lessons")
    lessons_storage.override_lessons(new_lessons, new_link_groups, new_link_teachers)
    print("Finish override lessons")


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

    lessons = LessonsStorage(db)
    teachers = TeachersStorage(db)
    classrooms = ClassroomsStorage(db)
    groups = GroupsStorage(db)

    with db:
        if not db.table_exists("lessons"):
            db.execute_script(CREATE_TABLE_LESSONS_SQL)
        if not db.table_exists("lessons_to_teachers"):
            db.execute_script(CREATE_TABLE_LESSON_TO_TEACHERS_SQL)
        if not db.table_exists("lessons_to_groups"):
            db.execute_script(CREATE_TABLE_LESSON_TO_GROUPS_SQL)

        print("Migration starting")
        migrate(
            group_storage=groups,
            lessons_storage=lessons,
            teachers_storage=teachers,
            classrooms_storage=classrooms,
            schedule_repository=repository,
        )

    print("Migration complete")
