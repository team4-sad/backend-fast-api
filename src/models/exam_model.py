import dataclasses


@dataclasses.dataclass
class ExamModel:
    id: int
    student_group_id: int
    classroom_id: int
    classroom_name: str
    classroom_floor: int
    classroom_building_name: str
    classroom_type_name: str
    discipline_id: int
    discipline_name: str
    date_and_time: str
    examiner_id: int
    examiner_first_name: str
    examiner_last_name: str
    examiner_patronymic: str

    @staticmethod
    def from_json(json: dict):
        return ExamModel(
            id=json["id"],
            student_group_id=json["studentGroupId"],
            classroom_id=json["classroomId"],
            classroom_name=json["classroomName"],
            classroom_floor=json["classroomFloor"],
            classroom_building_name=json["classroomBuildingName"],
            classroom_type_name=json["classroomTypeName"],
            discipline_id=json["disciplineId"],
            discipline_name=json["disciplineName"],
            date_and_time=json["dateAndTime"],
            examiner_id=json["examinerId"],
            examiner_first_name=json["examinerFirstName"],
            examiner_last_name=json["examinerLastName"],
            examiner_patronymic=json["examinerPatronymic"],
        )
