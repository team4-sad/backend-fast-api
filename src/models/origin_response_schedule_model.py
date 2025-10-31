import dataclasses

from src.models.origin_schedule_model import OriginScheduleModel


@dataclasses.dataclass
class OriginResponseScheduleModel:
    group_name: str
    schedule: OriginScheduleModel = None

    @staticmethod
    def from_json(json_obj: dict):
        return OriginResponseScheduleModel(
            group_name= json_obj['groupName'],
            schedule = OriginScheduleModel.from_json(json_obj['schedule'])
        )
