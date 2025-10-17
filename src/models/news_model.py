import dataclasses


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