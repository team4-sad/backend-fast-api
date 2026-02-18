from src.exceptions.lk_not_authorized_exception import LkNotAuthorizedException
from src.interfaces.i_lk_repository import ILkRepository
from src.models.lk_profile_model import LkProfileModel
from test.utils import json_mock


class MockLkRepository(ILkRepository):

    def get_me(self, access_token: str) -> LkProfileModel:
        if access_token == "":
            raise LkNotAuthorizedException()
        else:
            return LkProfileModel.from_json(json_mock("lk_profile_mock.json"))