import dataclasses


@dataclasses.dataclass
class DbLessonToGroupModel:
    id: int | None
    group_id: int
    lesson_id: str