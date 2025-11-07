import dataclasses


@dataclasses.dataclass
class OriginGroupsInfoModel:
    group_name: str
    id: int
    current_week_schedule_link: str

    @staticmethod
    def from_json(json: dict):
        return OriginGroupsInfoModel(
            group_name=json["groupName"],
            id=json["id"],
            current_week_schedule_link=json["currentWeekScheduleLink"],
        )
