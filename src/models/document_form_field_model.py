import dataclasses

from src.enums.document_form_field_type import DocumentFormFieldType


@dataclasses.dataclass
class DocumentFormFieldModel:
    label: str
    type: DocumentFormFieldType
    is_required: bool
    options: list[str] | None

    @staticmethod
    def from_json(json: dict):
        return DocumentFormFieldModel(
            label=json["label"],
            type=DocumentFormFieldType(json["type"]),
            is_required=json["is_required"],
            options=json.get('options'),
        )
