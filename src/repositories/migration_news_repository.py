from datetime import date, timedelta

from src.common.utils import date2str
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import GET_LAST_NEWS_SQL, GET_DATE_NEWS_SQL
from src.interfaces.i_migration_news_repository import IMigrationNewsRepository
from src.models.news_model import NewsModel


class MigrationNewsRepository(IMigrationNewsRepository):

    def __init__(self, db: SQLiteDatabase):
        self._db = db

    def save_single_news(self, single_news: NewsModel):
        self._db.insert("news", single_news.to_db())

    def save_news(self, news: list[NewsModel]):
        for item in news:
            self.save_single_news(item)

    def get_last_saved_news(self) -> NewsModel | None:
        raw_news = self._db.fetch_one(GET_LAST_NEWS_SQL)
        if raw_news is None:
            return None
        return NewsModel.from_db(raw_news)

    def get_news_by_date(self, search_date: date) -> list[NewsModel]:
        news = self._db.fetch_all(GET_DATE_NEWS_SQL, (date2str(search_date), ))
        return [NewsModel.from_db(i) for i in news]
