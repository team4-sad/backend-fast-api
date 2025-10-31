import dataclasses

from src.models.origin_lesson_model import OriginLessonModel


@dataclasses.dataclass
class OriginScheduleModel:
    monday: list[OriginLessonModel] = None
    tuesday: list[OriginLessonModel] = None
    wednesday: list[OriginLessonModel] = None
    thursday: list[OriginLessonModel] = None
    friday: list[OriginLessonModel] = None
    saturday: list[OriginLessonModel] = None
    sunday: list[OriginLessonModel] = None

    @staticmethod
    def from_json(json_obj: dict):
        return OriginScheduleModel(
            monday = [OriginLessonModel.from_json(i) for i in json_obj['понедельник']] if 'понедельник' in json_obj else None,
            tuesday = [OriginLessonModel.from_json(i) for i in json_obj['вторник']] if 'вторник' in json_obj else None,
            wednesday = [OriginLessonModel.from_json(i) for i in json_obj['среда']] if 'среда' in json_obj else None,
            thursday = [OriginLessonModel.from_json(i) for i in json_obj['четверг']] if 'четверг' in json_obj else None,
            friday = [OriginLessonModel.from_json(i) for i in json_obj['пятница']] if 'пятница' in json_obj else None,
            saturday = [OriginLessonModel.from_json(i) for i in json_obj['суббота']] if 'суббота' in json_obj else None,
            sunday = [OriginLessonModel.from_json(i) for i in json_obj['воскресенье']] if 'воскресенье' in json_obj else None
        )
    
    def get_weekdays(self):
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday]