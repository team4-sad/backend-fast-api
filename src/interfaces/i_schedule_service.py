import abc

from src.models.response_group_schedule_model import ResponseGroupScheduleModel


class IScheduleService(abc.ABC):
    def fetch_group_schedule(self, group_id: str, date_start: str, date_end: str) -> ResponseGroupScheduleModel:
        pass
