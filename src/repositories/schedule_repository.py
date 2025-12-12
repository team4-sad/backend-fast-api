import requests
from requests import HTTPError

from src.exceptions.invalid_classroom_exception import InvalidClassroomException
from src.exceptions.invalid_group_exception import InvalidGroupException
from src.exceptions.invalid_schedule_exception import InvalidScheduleException
from src.exceptions.invalid_teacher_exception import InvalidTeacherException
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.models.origin_response_classroom_schedule_model import OriginResponseClassroomScheduleModel
from src.models.origin_response_group_schedule_model import OriginResponseGroupScheduleModel
from src.models.origin_response_teacher_model import OriginResponseTeacherScheduleModel


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
                raise InvalidScheduleException.group(payload=group_id, status_code=exception.response.status_code)
        response_schedule = OriginResponseGroupScheduleModel.from_json(response.json())
        return response_schedule

    def fetch_teacher(self, teacher_id: str, date_start: str, date_end: str) -> OriginResponseTeacherScheduleModel:
        try:
            response = requests.get(f"{self.base_url}teacher/{teacher_id}/?dateStart={date_start}&dateEnd={date_end}")
            response.raise_for_status()
        except HTTPError as exception:
            if exception.response.status_code == 404:
                raise InvalidTeacherException(teacher_id=teacher_id)
            else:
                raise InvalidScheduleException.teacher(payload=teacher_id, status_code=exception.response.status_code)
        response_schedule = OriginResponseTeacherScheduleModel.from_json(response.json())
        return response_schedule

    def fetch_classroom(self, classroom_id: str, date_start: str, date_end: str) -> OriginResponseClassroomScheduleModel:
        try:
            response = requests.get(f"{self.base_url}classroom/{classroom_id}/?dateStart={date_start}&dateEnd={date_end}")
            response.raise_for_status()
        except HTTPError as exception:
            if exception.response.status_code == 404:
                raise InvalidClassroomException(classroom_id=classroom_id)
            else:
                raise InvalidScheduleException.classroom(payload=classroom_id, status_code=exception.response.status_code)
        response_schedule = OriginResponseClassroomScheduleModel.from_json(response.json())
        return response_schedule