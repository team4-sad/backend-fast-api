import dataclasses


@dataclasses.dataclass
class DbLessonToGroupModel:
    id: int | None
    group_id: int
    subgroup: str | None
    lesson_id: str

    @staticmethod
    def new(lesson_id: str, group_name: str, group_name_to_id: dict[str, int]) -> 'DbLessonToGroupModel':
        parts = group_name.split(' ')
        group_name = parts[0]
        subgroup = None if len(parts) == 1 else " ".join(parts[1:])
        return DbLessonToGroupModel(
            id=None,
            lesson_id=lesson_id,
            subgroup=subgroup,
            group_id=group_name_to_id[group_name],
        )

    def to_json(self):
        return {
            'id': self.id,
            'id_group': self.group_id,
            'id_lesson': self.lesson_id,
            'subgroup': self.subgroup,
        }