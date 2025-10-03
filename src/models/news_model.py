import dataclasses


@dataclasses.dataclass
class NewsModel:
    id: str
    header: str
    date_created: str
    news_link: str
    image_link: str | None = None
    description: str | None = None