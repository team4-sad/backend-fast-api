import dataclasses

from src.models.origin_classrooms_info_model import OriginClassroomsInfoModel


@dataclasses.dataclass
class ClassroomsInfoModel:
    classroom_id: int
    classroom_name: str

    @staticmethod
    def from_origin(origin: OriginClassroomsInfoModel):
        return ClassroomsInfoModel(
            classroom_id=origin.classroom_id,
            classroom_name=origin.classroom_name
        )
