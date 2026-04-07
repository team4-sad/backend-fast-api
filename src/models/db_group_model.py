import dataclasses

from src.models.origin_groups_info_model import OriginGroupsInfoModel


@dataclasses.dataclass
class DbGroupModel:
    id: int
    name: str
    year: int
    faculty: str
    department: str
    group: str

    @staticmethod
    def from_json(json: dict):
        return DbGroupModel(
            id=json["id"],
            name=json["name"],
            year=json["year"],
            faculty=json["faculty"],
            department=json["department"],
            group=json["group"]
        )

    @staticmethod
    def from_origin_group_info(origin: OriginGroupsInfoModel):
        parts = origin.group_name.split("-")
        if len(parts) > 4:
            parts[3] = "-".join(parts[3:])
        return DbGroupModel(
            id=origin.id,
            name=origin.group_name,
            year=int(parts[0]),
            faculty=parts[1],
            department=parts[2],
            group=parts[3]
        )

    def to_json(self) -> dict:
        return dataclasses.asdict(self)

    def to_tuple(self) -> tuple:
        return dataclasses.astuple(self)

    @staticmethod
    def from_tuple(tpl: tuple):
        return DbGroupModel(
            id=tpl[0],
            name=tpl[1],
            year=tpl[2],
            faculty=tpl[3],
            department=tpl[4],
            group=tpl[5]
        )
