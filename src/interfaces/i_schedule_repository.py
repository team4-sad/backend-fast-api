import abc

from src.models.origin_response_schedule_model import OriginResponseScheduleModel


class IScheduleRepository(abc.ABC):
    def fetch_group(self, group_id: str, date_start: str, date_end:str) -> OriginResponseScheduleModel:
        pass
