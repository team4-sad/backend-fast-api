import dataclasses


@dataclasses.dataclass
class ItemFamilyModel:
    kinship: str | None = None
    fio: str | None = None

    @staticmethod
    def from_json(json: dict):
        return ItemFamilyModel(
            kinship=json["kinship"],
            fio=json["fio"]
        )