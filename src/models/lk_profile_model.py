import dataclasses
from datetime import datetime

from src.models.education_info_model import EducationInfoModel
from src.models.item_family_model import ItemFamilyModel


@dataclasses.dataclass
class LkProfileModel:
    first_name: str | None = None
    last_name: str | None = None
    patronymic: str | None = None
    lk_email: str | None = None
    email: str | None = None
    address: str | None = None
    job_place: str | None = None
    job_title: str | None = None
    number_student_card: str | None = None
    datetime_student_card: datetime | None = None
    record_book_number: str | None = None
    education_info: list[EducationInfoModel] | None = None
    family: list[ItemFamilyModel] | None = None

    @staticmethod
    def from_json(json: dict):
        return LkProfileModel(
            first_name = json["first_name"],
            last_name = json["last_name"],
            patronymic = json["patronymic"],
            lk_email = json["lk_email"],
            email = json["email"],
            address = json["address"],
            job_place = json["job_place"],
            job_title = json["job_title"],
            number_student_card = json["number_student_card"],
            datetime_student_card = datetime.strptime(json["datetime_student_card"],"%d.%m.%Y"),
            record_book_number = json["record_book_number"],
            education_info = [EducationInfoModel.from_json(i) for i in json['education_info']] if "education_info" in json else None,
            family = [ItemFamilyModel.from_json(i) for i in json['family']] if "family" in json else None,
        )