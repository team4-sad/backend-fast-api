import abc

from src.models.origin_classrooms_info_model import OriginClassroomsInfoModel
from src.models.origin_groups_info_model import OriginGroupsInfoModel
from src.models.origin_teachers_info_model import OriginTeachersInfoModel


class ISignatureRepository(abc.ABC):
    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        pass

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        pass

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        pass