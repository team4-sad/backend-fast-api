import dataclasses
from datetime import datetime, date

from src.common.utils import str2date, str2datetime


@dataclasses.dataclass
class NewsModel:
    id: str
    header: str
    date_created: str
    news_link: str
    image_link: str | None = None
    description: str | None = None

    @staticmethod
    def from_db(db_obj: tuple):
        return NewsModel(
            header=db_obj[1],
            date_created=db_obj[2],
            news_link=db_obj[3],
            image_link=db_obj[4],
            description=db_obj[5],
            id=str(db_obj[6]),
        )

    def to_db(self) -> dict:
        return {
            "header": self.header,
            "date": self.date_created,
            "link": self.news_link,
            "cover_url": self.image_link,
            "description": self.description,
            "news_id": self.id,
            "search_header": self.header.lower(),
        }

    @property
    def date_date_created(self):
        try:
            return str2date(self.date_created)
        except ValueError:
            return str2datetime(self.date_created).date()
