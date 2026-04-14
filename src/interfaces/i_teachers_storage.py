import abc

from src.models.db_teacher_model import DbTeacherModel


class ITeachersStorage (abc.ABC):
    def search_teacher(self, search_text: str) -> list[DbTeacherModel]:
        pass

    def override_teachers(self, teachers: list[DbTeacherModel]):
        pass
