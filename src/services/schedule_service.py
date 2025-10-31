from src.exceptions.code_exception import CodeException
from src.exceptions.invalid_group_exception import InvalidGroupException
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.interfaces.i_schedule_service import IScheduleService
from src.models.response_schedule_model import ResponseScheduleModel


class ScheduleService(IScheduleService):
    def __init__(self, schedule_repository: IScheduleRepository):
        self.schedule_repository = schedule_repository

    def fetch_group_schedule(self, group_id: str, date_start: str, date_end: str) -> ResponseScheduleModel:
        try:
            raw_model = self.schedule_repository.fetch_group(group_id=group_id, date_start=date_start, date_end=date_end)
        except InvalidGroupException:
            raise CodeException(message="Group not found", error_code=404)
        except:
            raise CodeException(message="Error getting group schedule", error_code=503)

        return ResponseScheduleModel.from_origin(raw_model)
