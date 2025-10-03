import dataclasses


@dataclasses.dataclass
class SingularNewsModel:
    header: str
    date_created: str
    content_html: str
