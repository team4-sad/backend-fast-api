from src.exceptions.lk_exception import LkException
from src.interfaces.i_lk_repository import ILkRepository
from src.models.course_education_plan_model import CourseEducationPlanModel
from src.models.document_form_model import DocumentFormModel
from src.models.filled_document_form_model import FilledDocumentFormModel
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

    def get_document_forms(self, access_token: str) -> list[DocumentFormModel]:
        raise LkException('mock exception')

    def send_filled_document_form(self, access_token: str, filled_document_form_model: FilledDocumentFormModel) -> OrderDocumentModel:
        raise LkException('mock exception')
