import abc

from src.models.db_lesson_model import DbLessonModel


class ILessonsStorage (abc.ABC):
    def search_lessons(self, search_text: str) -> list[DbLessonModel]:
        pass

    def override_lessons(self, teachers: list[DbLessonModel]):
        pass
