import abc

from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel


class ILkRepository(abc.ABC):
    def get_me(self, access_token: str) -> LkProfileModel:
        pass

    def get_academic_records(self, access_token: str) ->  list[LkCourseRecordModel]:
        pass