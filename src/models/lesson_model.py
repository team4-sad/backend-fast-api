import dataclasses

from src.models.origin_lesson_model import OriginLessonModel
from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class LessonModel:
    lesson_order_number: int
    classroom_id: int
    classroom_floor: int
    lesson_start_time: str
    lesson_end_time: str
    lesson_type: str
    classroom_name: str
    classroom_type: str
    classroom_building: str
    discipline_name: str
    teachers: list[TeacherModel]
    groups: list[str] | None = None
    subgroup: str = ""

    @staticmethod
    def from_origin(origin: OriginLessonModel):
        return LessonModel(
            lesson_order_number=origin.lesson_order_number,
            classroom_id=origin.classroom_id,
            classroom_floor=origin.classroom_floor,
            lesson_start_time=origin.lesson_start_time,
            lesson_end_time=origin.lesson_end_time,
            lesson_type=origin.lesson_type,
            classroom_name=origin.classroom_name,
            classroom_type=origin.classroom_type,
            classroom_building=origin.classroom_building,
            discipline_name=origin.discipline_name,
            teachers=origin.teachers,
            subgroup=origin.subgroup,
            groups=origin.groups
        )
