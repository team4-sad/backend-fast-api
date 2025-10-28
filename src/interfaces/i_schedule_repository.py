import abc

from src.models.response_schedule_model import ResponseScheduleModel


class IScheduleRepository(abc.ABC):
    def fetch_group(self, group_id: int, date_start: str, date_end:str) -> ResponseScheduleModel:
        pass
