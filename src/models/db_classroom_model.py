import dataclasses
from src.models.origin_classrooms_info_model import OriginClassroomsInfoModel


@dataclasses.dataclass
class DbClassroomModel:
    id: int
    name: str

    def to_json(self):
        return dataclasses.asdict(self)

    @staticmethod
    def from_origin(origin: OriginClassroomsInfoModel):
        return DbClassroomModel(
            id=origin.classroom_id,
            name=origin.classroom_name
        )

    @staticmethod
    def from_tuple(tpl: tuple):
        return DbClassroomModel(id=tpl[0], name=tpl[1])
