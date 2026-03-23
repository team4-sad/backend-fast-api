import dataclasses
from src.models.document_form_field_model import DocumentFormFieldModel
from src.models.document_form_model import DocumentFormModel
from src.models.filled_document_form_field_model import FilledDocumentFormFieldModel
from src.models.interval_model import IntervalModel


@dataclasses.dataclass
class FilledDocumentFormModel(DocumentFormModel):
    user_id: str
    filled_fields: list[FilledDocumentFormFieldModel]

    @staticmethod
    def from_json(json: dict):
        return FilledDocumentFormModel (
            name=json["label"],
            description=json["description"],
            interval_make=IntervalModel.from_json(json["interval_make"]),
            user_id=json["user_id"],
            filled_fields=[FilledDocumentFormFieldModel.from_json(i) for i in json['filled_fields']] if "filled_fields" in json else None,
            fields=[DocumentFormFieldModel.from_json(i) for i in json['fields']] if "fields" in json else None,
        )
