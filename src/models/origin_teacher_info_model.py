import dataclasses

from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class OriginTeacherInfoModel:
    id: str
    teacher: TeacherModel
    current_week_schedule_link: str

    @staticmethod
    def from_json(json: dict):
        return OriginTeacherInfoModel(
            id=json["id"],
            teacher=TeacherModel.from_json(json),
            current_week_schedule_link=json["currentWeekScheduleLink"]
        )
