import dataclasses

from src.models.document_form_field_model import DocumentFormFieldModel
from src.models.interval_model import IntervalModel


@dataclasses.dataclass
class DocumentFormModel:
    name: str
    description: str
    interval_make: IntervalModel
    fields: list[DocumentFormFieldModel] | None

    @staticmethod
    def from_json(json: dict):
        return DocumentFormModel(
            name=json["name"],
            description=json["description"],
            interval_make=IntervalModel.from_json(json["interval_make"]),
            fields=[DocumentFormFieldModel.from_json(i) for i in json['fields']] if "fields" in json else None,
        )
