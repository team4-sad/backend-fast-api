import datetime

from src.enums.order_document_status import OrderDocumentStatus
from src.exceptions.lk_not_authorized_exception import LkNotAuthorizedException
from src.interfaces.i_lk_repository import ILkRepository
from src.models.course_education_plan_model import CourseEducationPlanModel
from src.models.document_form_model import DocumentFormModel
from src.models.filled_document_form_model import FilledDocumentFormModel
from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel
from src.models.order_document_model import OrderDocumentModel
from test.utils import json_mock


class MockLkRepository(ILkRepository):
    def __init__(self):
        self.cache = []

    def get_me(self, access_token: str) -> LkProfileModel:
        if access_token == "":
            raise LkNotAuthorizedException()
        else:
            return LkProfileModel.from_json(json_mock("lk_profile_mock.json"))

    def get_academic_records(self, access_token: str) -> list[LkCourseRecordModel]:
        if access_token == "":
            raise LkNotAuthorizedException()
        else:
            return [LkCourseRecordModel.from_json(i) for i in json_mock("lk_academic_records_mock.json")]

    def get_education_plan(self, access_token: str) -> list[CourseEducationPlanModel]:
        if access_token == "":
            raise LkNotAuthorizedException()
        else:
            return [CourseEducationPlanModel.from_json(i) for i in json_mock("course_education_plan_mock.json")]

    def get_orders_document(self, access_token: str) -> list[OrderDocumentModel]:
        if access_token == "":
            raise LkNotAuthorizedException()
        else:
            return [OrderDocumentModel.from_json(i) for i in json_mock("lk_document_orders.json")]

    def get_document_forms(self, access_token: str) -> list[DocumentFormModel]:
        if access_token == "":
            raise LkNotAuthorizedException()
        return [DocumentFormModel.from_json(i) for i in json_mock("document_forms_mock.json")]

    def send_filled_document_form(
        self,
        access_token: str,
        filled_document_form_model: FilledDocumentFormModel
    ) -> OrderDocumentModel:
        if access_token == "":
            raise LkNotAuthorizedException()

        mock_order_document_model = OrderDocumentModel(
            id=len(self.cache),
            number="2026-" + str(len(self.cache)).rjust(10, '0'),
            name=filled_document_form_model.name,
            created_at=datetime.datetime.now(),
            interval=filled_document_form_model.interval_make,
            status=OrderDocumentStatus.in_progress,
            comment=""
        )

        self.cache.append(mock_order_document_model)
        return mock_order_document_model
