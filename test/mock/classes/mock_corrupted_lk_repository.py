from src.exceptions.lk_exception import LkException
from src.interfaces.i_lk_repository import ILkRepository
from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel


class MockCorruptedLkRepository(ILkRepository):
    def get_me(self, access_token: str) -> LkProfileModel:
        raise LkException('mock exception')

    def get_academic_records(self, access_token: str) -> list[LkCourseRecordModel]:
        raise LkException('mock exception')
