import abc

from src.models.classrooms_info_model import ClassroomsInfoModel
from src.models.groups_info_model import GroupsInfoModel
from src.models.response_classroom_schedule_model import ResponseClassroomScheduleModel
from src.models.response_group_schedule_model import ResponseGroupScheduleModel
from src.models.response_teacher_schedule_model import ResponseTeacherScheduleModel
from src.models.teachers_info_model import TeachersInfoModel


class IScheduleService(abc.ABC):
    def fetch_group_schedule(self, group_id: str, date_start: str, date_end: str) -> ResponseGroupScheduleModel:
        pass

    def fetch_teacher_schedule(self, teacher_id: str, date_start: str, date_end: str) -> ResponseTeacherScheduleModel:
        pass

    def fetch_audience_schedule(self, classroom_id: str, date_start: str, date_end: str) -> ResponseClassroomScheduleModel:
        pass

    def fetch_groups_list(self, group_name: str) -> GroupsInfoModel:
        pass

    def fetch_teachers_list(self, teacher_name: str) -> TeachersInfoModel:
        pass

    def fetch_classrooms_list(self, classroom: str) -> ClassroomsInfoModel:
        pass