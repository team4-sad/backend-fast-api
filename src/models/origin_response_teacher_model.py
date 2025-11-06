import dataclasses

from src.models.origin_schedule_model import OriginScheduleModel
from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class OriginResponseTeacherScheduleModel:
    teacher: TeacherModel
    schedule: OriginScheduleModel = None

    @staticmethod
    def from_json(json_obj: dict):
        return OriginResponseTeacherScheduleModel(
            teacher=TeacherModel.from_json(json_obj["teacher"]),
            schedule=OriginScheduleModel.from_json(json_obj['schedule'])
        )
