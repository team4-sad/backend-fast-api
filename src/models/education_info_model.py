import dataclasses


@dataclasses.dataclass
class EducationInfoModel:
    faculty: str | None = None
    form: str | None = None
    type_form: str | None = None
    level: str | None = None
    direction: str | None = None
    group: str | None = None
    course: str | None = None
    status: str | None = None
    profile: str | None = None

    @staticmethod
    def from_json(json: dict):
        return EducationInfoModel(
            faculty= json["faculty"],
            form= json["form"],
            type_form= json["type_form"],
            level= json["level"],
            direction= json["direction"],
            group= json["group"],
            course= json["course"],
            status= json["status"],
            profile= json["profile"]
        )