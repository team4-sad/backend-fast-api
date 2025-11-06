import dataclasses

from src.models.origin_teacher_info_model import OriginTeacherInfoModel
from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class TeacherInfoModel:
    id: str
    teacher: TeacherModel

    @staticmethod
    def from_origin(origin: OriginTeacherInfoModel):
        return TeacherInfoModel(
            id=origin.id,
            teacher=origin.teacher
        )
