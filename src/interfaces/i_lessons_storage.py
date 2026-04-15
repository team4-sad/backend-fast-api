import abc

from src.models.db_lesson_model import DbLessonModel
from src.models.db_lesson_to_group import DbLessonToGroupModel
from src.models.db_lesson_to_teacher import DbLessonToTeacherModel
from src.models.full_db_lesson_model import FullDbLessonModel


class ILessonsStorage(abc.ABC):
    def search_lessons(self, search_text: str) -> list[DbLessonModel]:
        pass

    def override_lessons(self, lessons: list[FullDbLessonModel], link_groups: list[DbLessonToGroupModel], link_teachers: list[DbLessonToTeacherModel]):
        pass
