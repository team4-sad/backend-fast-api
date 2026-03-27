import abc

from src.models.db_group_model import DbGroupModel


class IGroupsStorage (abc.ABC):
    def search_groups(self, search_text: str) -> list[DbGroupModel]:
        pass

    def override_groups(self, groups: list[DbGroupModel]):
        pass
