import abc

from src.models.response_schedule_model import ResponseScheduleModel


class IScheduleService(abc.ABC):
    def fetch_group_schedule(self, group_id: str, date_start: str, date_end: str) -> ResponseScheduleModel:
        pass
