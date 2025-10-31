import dataclasses

from src.models.teacher_model import TeacherModel


@dataclasses.dataclass
class OriginLessonModel:
    day_of_week: int
    lesson_order_number: int
    classroom_id: int
    classroom_floor: int
    group_name: str
    lesson_date: str
    lesson_start_time: str
    lesson_end_time: str
    lesson_type: str
    classroom_name: str
    classroom_type: str
    classroom_building: str
    discipline_name: str
    teachers: list[TeacherModel]
    subgroup: str = ""
    link: str = ""

    @property
    def get_name_of_week(self):
        return ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"][self.day_of_week - 1]

    @property
    def get_only_date(self):
        return self.lesson_date.split("T")[0]

    @staticmethod
    def from_json(json_obj: dict):
        return OriginLessonModel(
            day_of_week=json_obj["dayOfWeek"],
            lesson_order_number=json_obj["lessonOrderNumber"],
            classroom_id=json_obj["classroomId"],
            classroom_floor=json_obj["classroomFloor"],
            group_name=json_obj["groupName"],
            lesson_date=json_obj["lessonDate"],
            lesson_start_time=json_obj["lessonStartTime"],
            lesson_end_time=json_obj["lessonEndTime"],
            lesson_type=json_obj["lessonType"],
            classroom_name=json_obj["classroomName"],
            classroom_type=json_obj["classroomType"],
            classroom_building=json_obj["classroomBuilding"],
            discipline_name=json_obj["disciplineName"],
            teachers=[TeacherModel.from_json(i) for i in json_obj['teachers']],
            subgroup=json_obj["subgroup"],
            link=json_obj["link"],
        )
