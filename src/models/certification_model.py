import dataclasses


@dataclasses.dataclass
class CertificationModel:
    exam: bool
    credit_with_rate: bool
    credit: bool
    course_work: bool
    course_project: bool

    @staticmethod
    def from_json(json: dict):
        return CertificationModel(
            exam=json["exam"],
            credit_with_rate=json["credit_with_rate"],
            credit=json["credit"],
            course_work=json["course_work"],
            course_project=json["course_project"]
        )
