from src.interfaces.i_signature_repository import ISignatureRepository
from src.models.origin_classrooms_info_model import OriginClassroomsInfoModel
from src.models.origin_groups_info_model import OriginGroupsInfoModel
from src.models.origin_teachers_info_model import OriginTeachersInfoModel
from src.models.teacher_model import TeacherModel


class MockSignatureRepository(ISignatureRepository):
    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        return [OriginGroupsInfoModel(group_name=group_name, id=1, current_week_schedule_link="")]

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        return [OriginTeachersInfoModel(teacher=TeacherModel(first_name="", last_name="", patronymic=""), id=1,
                                        current_week_schedule_link="")]

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        return [OriginClassroomsInfoModel(classroom_name="", classroom_id=1, current_week_schedule_link="")]

class CorruptedNotFoundMockSignatureRepository(ISignatureRepository):

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        raise Exception()

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        raise Exception()

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        raise Exception()


class CorruptedExceptionMockSignatureRepository(ISignatureRepository):

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        raise Exception(503)

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        raise Exception(503)

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        raise Exception(503)


class EmptyMockSignatureRepository(ISignatureRepository):

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        return []

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        return []

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        return []