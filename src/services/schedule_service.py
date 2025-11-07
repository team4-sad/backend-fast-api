from src.exceptions.code_exception import CodeException
from src.exceptions.invalid_group_exception import InvalidGroupException
from src.interfaces.i_schedule_repository import IScheduleRepository
from src.interfaces.i_schedule_service import IScheduleService
from src.models.classrooms_info_model import ClassroomsInfoModel
from src.models.groups_info_model import GroupsInfoModel
from src.models.response_classroom_schedule_model import ResponseClassroomScheduleModel
from src.models.response_group_schedule_model import ResponseGroupScheduleModel
from src.models.response_teacher_schedule_model import ResponseTeacherScheduleModel
from src.models.teachers_info_model import TeachersInfoModel


class ScheduleService(IScheduleService):
    def __init__(self, schedule_repository: IScheduleRepository):
        self.schedule_repository = schedule_repository

    def fetch_group_schedule(self, group_id: str, date_start: str, date_end: str) -> ResponseGroupScheduleModel:
        try:
            raw_model = self.schedule_repository.fetch_group(group_id=group_id, date_start=date_start, date_end=date_end)
        except InvalidGroupException:
            raise CodeException(message="Group not found", error_code=404)
        except:
            raise CodeException(message="Error getting group schedule", error_code=503)

        return ResponseGroupScheduleModel.from_origin(raw_model)

    def fetch_teacher_schedule(self, teacher_id: str, date_start: str, date_end: str) -> ResponseTeacherScheduleModel:
        pass

    def fetch_audience_schedule(self, classroom_id: str, date_start: str, date_end: str) -> ResponseClassroomScheduleModel:
        pass

    def fetch_groups_list(self, group_name: str) -> list[GroupsInfoModel]:
        try:
            raw_model = self.schedule_repository.fetch_groups(group_name=group_name)
        except:
            raise CodeException(message="Error getting group list", error_code=503)
        return [GroupsInfoModel.from_origin(obj) for obj in raw_model]

    def fetch_teachers_list(self, teacher_name: str) -> list[TeachersInfoModel]:
        try:
            raw_model = self.schedule_repository.fetch_teachers(teacher_name=teacher_name)
        except:
            raise CodeException(message="Error getting teachers list", error_code=503)
        return [TeachersInfoModel.from_origin(obj) for obj in raw_model]

    def fetch_classrooms_list(self, classroom: str) -> list[ClassroomsInfoModel]:
        try:
            raw_model = self.schedule_repository.fetch_classrooms(classroom=classroom)
        except:
            raise CodeException(message="Error getting classrooms list", error_code=503)
        return [ClassroomsInfoModel.from_origin(obj) for obj in raw_model]
