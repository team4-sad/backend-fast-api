import dataclasses


@dataclasses.dataclass
class LkAcademicRecordModel:
    subject: str
    type: str
    rate: str | None
    teachers: list[str] | None

    @staticmethod
    def from_json(json: dict):
        return LkAcademicRecordModel(
            subject=json["subject"],
            teachers=json["teachers"] if "teachers" in json else None,
            type=json["type"],
            rate=json["rate"],
        )
