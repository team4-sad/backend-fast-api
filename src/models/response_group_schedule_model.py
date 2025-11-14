import dataclasses

from src.models.day_model import DayModel
from src.models.origin_response_group_schedule_model import OriginResponseGroupScheduleModel


@dataclasses.dataclass
class ResponseGroupScheduleModel:
    group_name: str
    schedule: list[DayModel]

    @staticmethod
    def from_origin(origin: OriginResponseGroupScheduleModel):
        return ResponseGroupScheduleModel(
            group_name=origin.group_name,
            schedule=DayModel.from_origin(origin=origin.schedule)
        )
