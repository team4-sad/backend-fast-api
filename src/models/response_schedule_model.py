import dataclasses

from src.models.schedule_model import ScheduleModel


@dataclasses.dataclass
class ResponseScheduleModel:
    group_name: str
    schedule: ScheduleModel = None

    @staticmethod
    def from_json(json_obj: dict):
        return ResponseScheduleModel(
            group_name= json_obj['groupName'],
            schedule = ScheduleModel.from_json(json_obj['schedule'])
        )
