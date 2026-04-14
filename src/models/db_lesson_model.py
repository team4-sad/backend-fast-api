import dataclasses


@dataclasses.dataclass
class DbLessonModel:
    id: str
    classroom_id: int
    day_of_week: int
    week_type: int
    subject: str
    lesson_type: str


    @staticmethod
    def from_json(json: dict):
        return DbLessonModel(
            id=json["id"],
            classroom_id=json["classroom_id"],
            day_of_week=json["day_of_week"],
            week_type=json["week_type"],
            subject=json["subject"],
            lesson_type=json["lesson_type"]
        )


    def to_json(self) -> dict:
        _dict = dataclasses.asdict(self)
        return _dict

    def to_tuple(self) -> tuple:
        return self.id, self.classroom_id, self.day_of_week, self.week_type, self.subject, self.lesson_type

    @staticmethod
    def from_tuple(tpl: tuple):
        return DbLessonModel(
            id=tpl[0],
            classroom_id=tpl[1],
            day_of_week=tpl[2],
            week_type=tpl[3],
            subject=tpl[4],
            lesson_type=tpl[5]
        )
