import dataclasses

from src.models.original_group_info_model import OriginGroupInfoModel


@dataclasses.dataclass
class GroupInfoModel:
    group_name: str
    id: int

    @staticmethod
    def from_origin(origin: OriginGroupInfoModel):
        return GroupInfoModel(
            group_name=origin.group_name,
            id=origin.id
        )
