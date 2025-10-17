import dataclasses


@dataclasses.dataclass
class PaginationModel:
    has_previous_page: bool
    current_page: int
    has_next_page: bool
