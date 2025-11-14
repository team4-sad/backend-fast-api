import dataclasses

from src.models.day_model import DayModel
from src.models.origin_response_group_schedule_model import OriginResponseGroupScheduleModel
from src.models.origin_response_teacher_model import OriginResponseTeacherScheduleModel
from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class ResponseTeacherScheduleModel:
    teacher: TeacherModel
    schedule: list[DayModel]

    @staticmethod
    def from_origin(origin: OriginResponseTeacherScheduleModel):
        return ResponseTeacherScheduleModel(
            teacher=origin.teacher,
            schedule=DayModel.from_origin(origin=origin.schedule)
        )
