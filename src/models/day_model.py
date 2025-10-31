import dataclasses

from src.models.lesson_model import LessonModel
from src.models.origin_schedule_model import OriginScheduleModel


@dataclasses.dataclass
class DayModel:
    day_of_week: int
    name_day_of_week: str
    date: str
    lessons: list[LessonModel]

    @staticmethod
    def from_origin(origin: OriginScheduleModel):
        return [
            DayModel(
                lessons=[LessonModel.from_origin(origin_lesson) for origin_lesson in weekday],
                date=weekday[0].get_only_date,
                day_of_week=weekday[0].day_of_week,
                name_day_of_week=weekday[0].get_name_of_week,
            )
            for weekday in origin.get_weekdays()
            if weekday is not None
        ]
