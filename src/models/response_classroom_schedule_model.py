import dataclasses

from src.models.day_model import DayModel
from src.models.origin_response_classroom_schedule_model import OriginResponseClassroomScheduleModel


@dataclasses.dataclass
class ResponseClassroomScheduleModel:
    classroom_name: str
    schedule: list[DayModel]

    @staticmethod
    def from_origin(origin: OriginResponseClassroomScheduleModel):
        return ResponseClassroomScheduleModel(
            classroom_name=origin.classroom_name,
            schedule=DayModel.from_origin(origin=origin.schedule)
        )
