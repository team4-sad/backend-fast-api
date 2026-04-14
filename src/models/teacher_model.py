import dataclasses


@dataclasses.dataclass
class TeacherModel:
    first_name: str
    last_name: str
    patronymic: str

    @staticmethod
    def from_json(json_obj: dict):
        return TeacherModel(
            first_name=json_obj['firstName'],
            last_name=json_obj['lastName'],
            patronymic=json_obj['patronymic']
        )

    def fio(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
