import requests
from requests import HTTPError

from src.exceptions.invalid_group_exception import InvalidGroupException
from src.exceptions.invalid_schedule_exception import InvalidScheduleException
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.models.origin_response_group_schedule_model import OriginResponseGroupScheduleModel


class ScheduleRepository(IScheduleRepository):

    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_group(self, group_id: str, date_start: str, date_end:str) -> OriginResponseGroupScheduleModel:
        try:
            response = requests.get(f"{self.base_url}group/{group_id}/?dateStart={date_start}&dateEnd={date_end}")
            response.raise_for_status()
        except HTTPError as exception:
            if exception.response.status_code == 404:
                raise InvalidGroupException(group_id=group_id)
            else:
                raise InvalidScheduleException(group_id=group_id, status_code=exception.response.status_code)
        response_schedule = OriginResponseGroupScheduleModel.from_json(response.json())
        return response_schedule
