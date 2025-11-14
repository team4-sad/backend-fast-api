import dataclasses

from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class OriginTeachersInfoModel:
    id: int
    teacher: TeacherModel
    current_week_schedule_link: str

    @staticmethod
    def from_json(json: dict):
        return OriginTeachersInfoModel(
            id=json["id"],
            teacher=TeacherModel.from_json(json["teacher"]),
            current_week_schedule_link=json["currentWeekScheduleLink"]
        )
