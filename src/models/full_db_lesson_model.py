import dataclasses
import itertools
import uuid

from src.common.datetime_utils import is_prime_week
from src.models.db_lesson_model import DbLessonModel
from src.models.db_lesson_to_group import DbLessonToGroupModel
from src.models.db_lesson_to_teacher import DbLessonToTeacherModel
from src.models.origin_lesson_model import OriginLessonModel
from src.models.origin_schedule_model import OriginScheduleModel


@dataclasses.dataclass
class FullDbLessonModel:
    db_lesson: DbLessonModel
    teachers: list[DbLessonToTeacherModel]
    groups: list[DbLessonToGroupModel]

    @staticmethod
    def from_schedule(
        schedule: OriginScheduleModel,
        groups_to_id: dict[str, int],
        teachers_to_id: dict[str, int],
    ) -> tuple[list['FullDbLessonModel'], list[DbLessonToGroupModel], list[DbLessonToTeacherModel]]:
        lessons: list[OriginLessonModel] = list(itertools.chain.from_iterable([i for i in schedule.get_weekdays() if i is not None]))

        def process(i: OriginLessonModel):
            _id = str(uuid.uuid4())
            lesson_teachers = [
                DbLessonToTeacherModel(
                    id=None,
                    teacher_id=teachers_to_id[j.fio()],
                    lesson_id=_id
                ) for j in i.teachers
            ]
            lesson_groups = [
                DbLessonToGroupModel.new(_id, j, groups_to_id) for j in i.groups
            ]
            return FullDbLessonModel(
                db_lesson=DbLessonModel(
                    id=_id,
                    classroom_id=i.classroom_id,
                    day_of_week=i.day_of_week,
                    week_type=is_prime_week(i.get_date),
                    subject=i.discipline_name,
                    lesson_type=i.lesson_type,
                ),
                teachers=lesson_teachers,
                groups=lesson_groups
            ), lesson_groups, lesson_teachers

        models: list[FullDbLessonModel] = []
        groups: list[DbLessonToGroupModel] = []
        teachers: list[DbLessonToTeacherModel] = []

        for lesson in lessons:
            new_model, new_groups, new_teachers = process(lesson)
            models.append(new_model)
            teachers.extend(new_teachers)
            groups.extend(new_groups)

        return models, groups, teachers
