import abc

from src.models.db_classroom_model import DbClassroomModel


class IClassroomsStorage(abc.ABC):
    def search_classroom(self, search_text: str) -> list[DbClassroomModel]:
        pass

    def override_classrooms(self, classrooms: list[DbClassroomModel]):
        pass
