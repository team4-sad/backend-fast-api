import dataclasses

from src.models.origin_schedule_model import OriginScheduleModel


@dataclasses.dataclass
class OriginResponseClassroomScheduleModel:
    classroom_name: str
    schedule: OriginScheduleModel = None

    @staticmethod
    def from_json(json_obj: dict):
        return OriginResponseClassroomScheduleModel(
            classroom_name= json_obj['classroomName'],
            schedule = OriginScheduleModel.from_json(json_obj['schedule'])
        )
