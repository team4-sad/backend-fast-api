import dataclasses

from src.models.lk_semester_record_model import LkSemesterRecordModel


@dataclasses.dataclass
class LkCourseRecordModel:
    number: int
    records: list[LkSemesterRecordModel] | None

    @staticmethod
    def from_json(json: dict):
        return LkCourseRecordModel(
            number=int(json["number"]),
            records=[LkSemesterRecordModel.from_json(i) for i in
                            json['records']] if "records" in json else None,
        )
