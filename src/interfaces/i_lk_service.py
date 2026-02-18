import abc

from src.models.lk_profile_model import LkProfileModel


class ILkService(abc.ABC):

    def get_me(self, access_token: str) -> LkProfileModel:
        pass