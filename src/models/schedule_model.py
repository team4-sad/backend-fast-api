import dataclasses

from src.models.lesson_model import LessonModel


@dataclasses.dataclass
class ScheduleModel:
    monday: list[LessonModel] = None
    tuesday: list[LessonModel] = None
    wednesday: list[LessonModel] = None
    thursday: list[LessonModel] = None
    friday: list[LessonModel] = None
    saturday: list[LessonModel] = None
    sunday: list[LessonModel] = None

    @staticmethod
    def from_json(json_obj: dict):
        return ScheduleModel(
            monday = [LessonModel.from_json(i) for i in json_obj['понедельник']] if 'понедельник' in json_obj else None,
            tuesday = [LessonModel.from_json(i) for i in json_obj['вторник']] if 'вторник' in json_obj else None,
            wednesday = [LessonModel.from_json(i) for i in json_obj['среда']] if 'среда' in json_obj else None,
            thursday = [LessonModel.from_json(i) for i in json_obj['четверг']] if 'четверг' in json_obj else None,
            friday = [LessonModel.from_json(i) for i in json_obj['пятница']] if 'пятница' in json_obj else None,
            saturday = [LessonModel.from_json(i) for i in json_obj['суббота']] if 'суббота' in json_obj else None,
            sunday = [LessonModel.from_json(i) for i in json_obj['воскресенье']] if 'воскресенье' in json_obj else None
        )