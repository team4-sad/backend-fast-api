import requests

from src.interfaces.i_signature_repository import ISignatureRepository
from src.models.origin_classrooms_info_model import OriginClassroomsInfoModel
from src.models.origin_groups_info_model import OriginGroupsInfoModel
from src.models.origin_teachers_info_model import OriginTeachersInfoModel


class SignatureRepository(ISignatureRepository):

    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_groups(self, group_name: str) -> list[OriginGroupsInfoModel]:
        response = requests.get(f"{self.base_url}search/group?groupName={group_name}")
        groups_list = [OriginGroupsInfoModel.from_json(obj) for obj in response.json()]
        return groups_list

    def fetch_teachers(self, teacher_name: str) -> list[OriginTeachersInfoModel]:
        response = requests.get(f"{self.base_url}search/teacher?teacherFullName={teacher_name}")
        teachers_list = [OriginTeachersInfoModel.from_json(obj) for obj in response.json()]
        return teachers_list

    def fetch_classrooms(self, classroom: str) -> list[OriginClassroomsInfoModel]:
        response = requests.get(f"{self.base_url}search/classroom?classroomName={classroom}")
        classrooms_list = [OriginClassroomsInfoModel.from_json(obj) for obj in response.json()]
        return classrooms_list