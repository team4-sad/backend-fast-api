import dataclasses

from src.models.origin_teachers_info_model import OriginTeachersInfoModel
from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class TeacherInfoModel:
    id: int
    teacher: TeacherModel

    @staticmethod
    def from_origin(origin: OriginTeachersInfoModel):
        return TeacherInfoModel(
            id=origin.id,
            teacher=origin.teacher
        )
