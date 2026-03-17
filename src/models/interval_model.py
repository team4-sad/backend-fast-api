import dataclasses


@dataclasses.dataclass
class IntervalModel:
    start_day: int
    end_day: int

    @staticmethod
    def from_json(json: dict):
        return IntervalModel(
            start_day=json["start_day"],
            end_day=json["end_day"],
        )
