import dataclasses

from src.models.day_model import DayModel
from src.models.origin_response_schedule_model import OriginResponseScheduleModel


@dataclasses.dataclass
class ResponseScheduleModel:
    group_name: str
    schedule: list[DayModel]

    @staticmethod
    def from_origin(origin: OriginResponseScheduleModel):
        return ResponseScheduleModel(
            group_name=origin.group_name,
            schedule=DayModel.from_origin(origin=origin.schedule)
        )
