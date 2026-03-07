import dataclasses

from src.models.certification_model import CertificationModel


@dataclasses.dataclass
class EducationPlanModel:
    index: str
    discipline: str
    academic_hours: int
    credit_units: int
    certification: CertificationModel
    department: str
    count_lectures: int
    count_laboratories: int
    count_independent_work: int
    count_practical: int
    exist_essay: bool

    @staticmethod
    def from_json(json: dict):
        return EducationPlanModel(
            index=json["index"],
            discipline=json["discipline"],
            academic_hours= int(json["academic_hours"]),
            credit_units= int(json["credit_units"]),
            certification= CertificationModel.from_json(json["certification"]),
            department= json["department"],
            count_lectures= int(json["count_lectures"]),
            count_laboratories= int(json["count_laboratories"]),
            count_independent_work= int(json["count_independent_work"]),
            count_practical= int(json["count_practical"]),
            exist_essay= json["exist_essay"]
        )
