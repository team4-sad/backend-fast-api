from src.exceptions.lk_not_authorized_exception import LkNotAuthorizedException
from src.interfaces.i_lk_repository import ILkRepository
from src.models.course_education_plan_model import CourseEducationPlanModel
from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel
from test.utils import json_mock


class MockLkRepository(ILkRepository):
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
