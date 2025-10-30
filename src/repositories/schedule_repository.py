import requests
from requests import HTTPError

from src.exceptions.invalid_group import InvalidGroup
from src.exceptions.invalid_schedule import InvalidSchedule
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.models.response_schedule_model import ResponseScheduleModel


class ScheduleRepository(IScheduleRepository):

    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_group(self, group_id: int, date_start: str, date_end:str) -> ResponseScheduleModel:
        try:
            response = requests.get(f"{self.base_url}group/{group_id}/?dateStart={date_start}&dateEnd={date_end}")
            response.raise_for_status()
        except HTTPError as exception:
            if exception.response.status_code == 404:
                raise InvalidGroup(group_id=group_id)
            else:
                raise InvalidSchedule(group_id=group_id, status_code=exception.response.status_code)
        response_schedule = ResponseScheduleModel.from_json(response.json())
        return response_schedule
