import dataclasses
from datetime import datetime

from src.enums.order_document_status import OrderDocumentStatus
from src.models.interval_model import IntervalModel


@dataclasses.dataclass
class OrderDocumentModel:
    id: int
    number: str
    name: str
    created_at: datetime
    interval: IntervalModel
    status: OrderDocumentStatus
    comment: str

    @staticmethod
    def from_json(json: dict):
        return OrderDocumentModel(
            id=json["id"],
            number=json["number"],
            name=json["name"],
            created_at=datetime.fromisoformat(json["created_at"]),
            interval=IntervalModel.from_json(json["interval"]),
            status=OrderDocumentStatus(json["status"]),
            comment=json["comment"]
        )
