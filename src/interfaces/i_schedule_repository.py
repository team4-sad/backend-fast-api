import abc

from src.models.origin_classrooms_info_model import OriginClassroomsInfoModel
from src.models.origin_groups_info_model import OriginGroupsInfoModel
from src.models.origin_response_classroom_schedule_model import OriginResponseClassroomScheduleModel
from src.models.origin_response_group_schedule_model import OriginResponseGroupScheduleModel
from src.models.origin_response_teacher_model import OriginResponseTeacherScheduleModel
from src.models.origin_teachers_info_model import OriginTeachersInfoModel


class IScheduleRepository(abc.ABC):
    def fetch_group(self, group_id: str, date_start: str, date_end:str) -> OriginResponseGroupScheduleModel:
        pass

    def fetch_teacher(self, teacher_id: str, date_start: str, date_end: str) -> OriginResponseTeacherScheduleModel:
        pass

    def fetch_classroom(self, classroom_id: str, date_start: str, date_end: str) -> OriginResponseClassroomScheduleModel:
        pass

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        pass

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        pass

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        pass
