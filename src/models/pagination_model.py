import dataclasses


@dataclasses.dataclass
class PaginationModel:
    is_previous_page: bool
    current_page: int
    is_next_page: bool
