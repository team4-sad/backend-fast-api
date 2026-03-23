import dataclasses

from src.enums.document_form_field_type import DocumentFormFieldType
from src.models.document_form_field_model import DocumentFormFieldModel


@dataclasses.dataclass
class FilledDocumentFormFieldModel (DocumentFormFieldModel):
    value: str | None

    @staticmethod
    def from_json(json: dict):
        return FilledDocumentFormFieldModel(
            label=json["label"],
            type=DocumentFormFieldType(json["type"]),
            is_required=json["is_required"],
            options=json["options"],
            value=json["value"] if "value" in json else None,
        )
