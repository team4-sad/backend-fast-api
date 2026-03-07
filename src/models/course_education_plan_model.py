import dataclasses

from src.models.semester_education_plan_model import SemesterEducationPlanModel


@dataclasses.dataclass
class CourseEducationPlanModel:
    course: int
    semesters: list[SemesterEducationPlanModel] | None

    @staticmethod
    def from_json(json: dict):
        return CourseEducationPlanModel(
            course=int(json["course"]),
            semesters=[SemesterEducationPlanModel.from_json(i) for i in json['semesters']] if "semesters" in json else None,
        )
