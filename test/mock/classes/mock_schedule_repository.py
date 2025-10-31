from src.exceptions.invalid_group_exception import InvalidGroupException
from src.exceptions.invalid_schedule_exception import InvalidScheduleException
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.models.origin_response_schedule_model import OriginResponseScheduleModel
from test.utils import json_mock


class  MockScheduleRepository(IScheduleRepository):
    def fetch_group(self, group_id: str, date_start: str, date_end: str) -> OriginResponseScheduleModel:
        return OriginResponseScheduleModel.from_json(json_mock("group-1274.json"))

class CorruptedNotFoundMockScheduleRepository(IScheduleRepository):
    def fetch_group(self, group_id: str, date_start: str, date_end: str) -> OriginResponseScheduleModel:
        raise InvalidGroupException(group_id=group_id)

class CorruptedExceptionMockScheduleRepository(IScheduleRepository):
    def fetch_group(self, group_id: str, date_start: str, date_end: str) -> OriginResponseScheduleModel:
        raise InvalidScheduleException(group_id=group_id, status_code=503)

class EmptyMockScheduleRepository(IScheduleRepository):
    def fetch_group(self, group_id: str, date_start: str, date_end: str) -> OriginResponseScheduleModel:
        return OriginResponseScheduleModel.from_json(json_mock("group-empty-1274.json"))