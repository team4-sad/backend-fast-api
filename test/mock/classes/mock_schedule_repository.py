from logging import exception

from src.exceptions.invalid_classroom_exception import InvalidClassroomException
from src.exceptions.invalid_group_exception import InvalidGroupException
from src.exceptions.invalid_schedule_exception import InvalidScheduleException
from src.exceptions.invalid_teacher_exception import InvalidTeacherException
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.models.origin_classrooms_info_model import OriginClassroomsInfoModel
from src.models.origin_groups_info_model import OriginGroupsInfoModel
from src.models.origin_response_classroom_schedule_model import OriginResponseClassroomScheduleModel
from src.models.origin_response_group_schedule_model import OriginResponseGroupScheduleModel
from src.models.origin_response_teacher_model import OriginResponseTeacherScheduleModel
from src.models.origin_teachers_info_model import OriginTeachersInfoModel
from src.models.teacher_model import TeacherModel
from test.utils import json_mock


class MockScheduleRepository(IScheduleRepository):
    def fetch_group(self, group_id: str, date_start: str, date_end: str) -> OriginResponseGroupScheduleModel:
        return OriginResponseGroupScheduleModel.from_json(json_mock("group_schedule.json"))

    def fetch_teacher(self, teacher_id: str, date_start: str, date_end: str) -> OriginResponseTeacherScheduleModel:
        return OriginResponseTeacherScheduleModel.from_json(json_mock("teacher_schedule.json"))

    def fetch_classroom(self, classroom_id: str, date_start: str,
                        date_end: str) -> OriginResponseClassroomScheduleModel:
        return OriginResponseClassroomScheduleModel.from_json(json_mock("classroom_schedule.json"))

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        return [OriginGroupsInfoModel(group_name=group_name, id=1, current_week_schedule_link="")]

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        return [OriginTeachersInfoModel(teacher=TeacherModel(first_name="", last_name="", patronymic=""), id=1,
                                        current_week_schedule_link="")]

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        return [OriginClassroomsInfoModel(classroom_name="", classroom_id=1, current_week_schedule_link="")]


class CorruptedNotFoundMockScheduleRepository(IScheduleRepository):
    def fetch_group(self, group_id: str, date_start: str, date_end: str) -> OriginResponseGroupScheduleModel:
        raise InvalidGroupException(group_id=group_id)

    def fetch_teacher(self, teacher_id: str, date_start: str, date_end: str) -> OriginResponseTeacherScheduleModel:
        raise InvalidTeacherException(teacher_id=teacher_id)

    def fetch_classroom(self, classroom_id: str, date_start: str,
                        date_end: str) -> OriginResponseClassroomScheduleModel:
        raise InvalidClassroomException(classroom_id=classroom_id)

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        raise Exception()

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        raise Exception()

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        raise Exception()


class CorruptedExceptionMockScheduleRepository(IScheduleRepository):
    def fetch_group(self, group_id: str, date_start: str, date_end: str) -> OriginResponseGroupScheduleModel:
        raise InvalidScheduleException.group(payload=group_id, status_code=503)

    def fetch_teacher(self, teacher_id: str, date_start: str, date_end: str) -> OriginResponseTeacherScheduleModel:
        raise InvalidScheduleException.teacher(payload=teacher_id, status_code=503)

    def fetch_classroom(self, classroom_id: str, date_start: str,
                        date_end: str) -> OriginResponseClassroomScheduleModel:
        raise InvalidScheduleException.classroom(payload=classroom_id, status_code=503)

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        raise Exception(503)

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        raise Exception(503)

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        raise Exception(503)


class EmptyMockScheduleRepository(IScheduleRepository):
    def fetch_group(self, group_id: str, date_start: str, date_end: str) -> OriginResponseGroupScheduleModel:
        return OriginResponseGroupScheduleModel.from_json(json_mock("group_schedule_empty.json"))

    def fetch_teacher(self, teacher_id: str, date_start: str, date_end: str) -> OriginResponseTeacherScheduleModel:
        return OriginResponseTeacherScheduleModel.from_json(json_mock("teacher_schedule_empty.json"))

    def fetch_classroom(self, classroom_id: str, date_start: str,
                        date_end: str) -> OriginResponseClassroomScheduleModel:
        return OriginResponseClassroomScheduleModel.from_json(json_mock("classroom_schedule_empty.json"))

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        return []

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        return []

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        return []
