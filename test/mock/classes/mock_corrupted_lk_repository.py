from src.exceptions.lk_exception import LkException
from src.interfaces.i_lk_repository import ILkRepository
from src.models.course_education_plan_model import CourseEducationPlanModel
from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel
from src.models.order_document_model import OrderDocumentModel


class MockCorruptedLkRepository(ILkRepository):
    def get_me(self, access_token: str) -> LkProfileModel:
        raise LkException('mock exception')

    def get_academic_records(self, access_token: str) -> list[LkCourseRecordModel]:
        raise LkException('mock exception')

    def get_education_plan(self, access_token: str) -> list[CourseEducationPlanModel]:
        raise LkException('mock exception')

    def get_orders_document(self, access_token: str) -> list[OrderDocumentModel]:
        raise LkException('mock exception')


