import dataclasses

from src.models.origin_classroom_info_model import OriginClassroomInfoModel


@dataclasses.dataclass
class ClassroomInfoModel:
    classroom_id: int
    classroom_name: str

    @staticmethod
    def from_origin(origin: OriginClassroomInfoModel):
        return ClassroomInfoModel(
            classroom_id=origin.classroom_id,
            classroom_name=origin.classroom_name
        )
