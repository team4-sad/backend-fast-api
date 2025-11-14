import dataclasses

from src.models.origin_groups_info_model import OriginGroupsInfoModel


@dataclasses.dataclass
class GroupsInfoModel:
    group_name: str
    id: int

    @staticmethod
    def from_origin(origin: OriginGroupsInfoModel):
        return GroupsInfoModel(
            group_name=origin.group_name,
            id=origin.id
        )
