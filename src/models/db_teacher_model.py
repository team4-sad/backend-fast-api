import dataclasses

from src.models.origin_teachers_info_model import OriginTeachersInfoModel


@dataclasses.dataclass
class DbTeacherModel:
    id: int
    lastname: str
    firstname: str
    patronymic: str

    @property
    def search_name(self) -> str:
        return f"{self.lastname.lower()} {self.firstname.lower()} {self.patronymic.lower()}"

    @staticmethod
    def from_json(json: dict):
        return DbTeacherModel(
            id=json["id"],
            lastname=json["lastname"],
            firstname=json["firstname"],
            patronymic=json["patronymic"]
        )

    @staticmethod
    def from_origin_teacher_info(origin: OriginTeachersInfoModel):
        return DbTeacherModel(
            id=origin.id,
            lastname=origin.teacher.last_name,
            firstname=origin.teacher.first_name,
            patronymic=origin.teacher.patronymic
        )

    def to_json(self) -> dict:
        _dict = dataclasses.asdict(self)
        _dict["search_name"] = self.search_name
        return _dict

    def to_tuple(self) -> tuple:
        return self.id, self.lastname, self.firstname, self.patronymic, self.search_name

    @staticmethod
    def from_tuple(tpl: tuple):
        return DbTeacherModel(
            id=tpl[0],
            lastname=tpl[1],
            firstname=tpl[2],
            patronymic=tpl[3]
        )
