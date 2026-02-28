import dataclasses

from src.models.lk_semester_record_model import LkSemesterRecordModel


@dataclasses.dataclass
class LkCourseRecordModel:
    course: int
    records: list[LkSemesterRecordModel] | None

    @staticmethod
    def from_json(json: dict):
        return LkCourseRecordModel(
            course=int(json["course"]),
            records=[LkSemesterRecordModel.from_json(i) for i in json['records']] if "records" in json else None,
        )
