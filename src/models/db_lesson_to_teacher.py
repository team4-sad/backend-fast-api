import dataclasses


@dataclasses.dataclass
class DbLessonToTeacherModel:
    id: int | None
    teacher_id: int
    lesson_id: str

    def to_json(self):
        return {
            "id": self.id,
            "id_teacher": self.teacher_id,
            "id_lesson": self.lesson_id,
        }
