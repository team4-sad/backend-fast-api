import dataclasses


@dataclasses.dataclass
class DbLessonToTeacherModel:
    id: int | None
    teacher_id: int
    lesson_id: str