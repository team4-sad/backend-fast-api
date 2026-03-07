import dataclasses

from src.models.education_plan_model import EducationPlanModel


@dataclasses.dataclass
class SemesterEducationPlanModel:
    semester: int
    plan: list[EducationPlanModel]

    @staticmethod
    def from_json(json: dict):
        return SemesterEducationPlanModel(
            semester=int(json["semester"]),
            plan=[EducationPlanModel.from_json(i) for i in json['plan']] if "plan" in json else None
        )
