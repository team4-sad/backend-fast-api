import dataclasses


@dataclasses.dataclass
class OriginClassroomsInfoModel:
    classroom_name: str
    classroom_id: int
    current_week_schedule_link: str

    @staticmethod
    def from_json(json: dict):
        return OriginClassroomsInfoModel(
            classroom_name=json["classroomName"],
            current_week_schedule_link=json["currentWeekScheduleLink"],
            classroom_id=json["classroomId"]
        )
