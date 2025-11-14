import dataclasses

from src.models.origin_teachers_info_model import OriginTeachersInfoModel
from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class TeachersInfoModel:
    id: int
    teacher: TeacherModel

    @staticmethod
    def from_origin(origin: OriginTeachersInfoModel):
        return TeachersInfoModel(
            id=origin.id,
            teacher=origin.teacher
        )
