from src.exceptions.code_exception import CodeException
from src.exceptions.lk_exception import LkException
from src.exceptions.lk_not_authorized_exception import LkNotAuthorizedException
from src.interfaces.i_lk_repository import ILkRepository
from src.interfaces.i_lk_service import ILkService
from src.models.course_education_plan_model import CourseEducationPlanModel
from src.models.document_form_model import DocumentFormModel
from src.models.filled_document_form_model import FilledDocumentFormModel
from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel
from src.models.order_document_model import OrderDocumentModel


class LkService(ILkService):
    def __init__(self, lk_repository: ILkRepository):
        self.lk_repository = lk_repository

    def get_me(self, access_token: str) -> LkProfileModel:
        try:
            profile = self.lk_repository.get_me(access_token=access_token)
        except LkException as e:
            raise CodeException(str(e), 503)
        except LkNotAuthorizedException as e:
            raise CodeException(str(e), 401)
        return profile

    def get_academic_records(self, access_token: str) -> list[LkCourseRecordModel]:
        try:
            records = self.lk_repository.get_academic_records(access_token=access_token)
        except LkException as e:
            raise CodeException(str(e), 503)
        except LkNotAuthorizedException as e:
            raise CodeException(str(e), 401)
        return records

    def get_education_plan(self, access_token: str) -> list[CourseEducationPlanModel]:
        try:
            plans = self.lk_repository.get_education_plan(access_token=access_token)
        except LkException as e:
            raise CodeException(str(e), 503)
        except LkNotAuthorizedException as e:
            raise CodeException(str(e), 401)
        return plans

    def get_orders_document(self, access_token: str) -> list[OrderDocumentModel]:
        try:
            documents = self.lk_repository.get_orders_document(access_token=access_token)
        except LkException as e:
            raise CodeException(str(e), 503)
        except LkNotAuthorizedException as e:
            raise CodeException(str(e), 401)
        return documents

    def get_document_forms(self, access_token: str) -> list[DocumentFormModel]:
        try:
            documents = self.lk_repository.get_document_forms(access_token=access_token)
        except LkException as e:
            raise CodeException(str(e), 503)
        except LkNotAuthorizedException as e:
            raise CodeException(str(e), 401)
        return documents

    def send_filled_document_form(self, access_token: str, filled_document_form_model: FilledDocumentFormModel) -> OrderDocumentModel:
        try:
            document = self.lk_repository.send_filled_document_form(
                access_token=access_token,
                filled_document_form_model=filled_document_form_model
            )
        except LkException as e:
            raise CodeException(str(e), 503)
        except LkNotAuthorizedException as e:
            raise CodeException(str(e), 401)
        return document
