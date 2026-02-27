import dataclasses

from src.models.lk_academic_record_model import LkAcademicRecordModel


@dataclasses.dataclass
class LkSemesterRecordModel:
    number: int
    records: list[LkAcademicRecordModel] | None

    @staticmethod
    def from_json(json: dict):
        return LkSemesterRecordModel(
            number=int(json["number"]),
            records=[LkAcademicRecordModel.from_json(i) for i in
                            json['records']] if "records" in json else None,
        )
