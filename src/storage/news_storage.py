from datetime import date
from typing import override
from src.common.utils import date2str
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import GET_LAST_NEWS_SQL, GET_DATE_NEWS_SQL, SEARCH_NEWS_SQL, GET_COUNT_NEWS_SQL
from src.interfaces.i_news_storage import INewsStorage
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel


class NewsStorage(INewsStorage):
    def __init__(self, database: SQLiteDatabase):
        self._db = database

    @override
    def save_single_news(self, single_news: NewsModel):
        self._db.insert("news", single_news.to_db())

    @override
    def save_news(self, news: list[NewsModel]):
        for item in news:
            self.save_single_news(item)

    @override
    def get_last_saved_news(self) -> NewsModel | None:
        raw_news = self._db.fetch_one(GET_LAST_NEWS_SQL)
        if raw_news is None:
            return None
        return NewsModel.from_db(raw_news)

    @override
    def get_news_by_date(self, search_date: date) -> list[NewsModel]:
        news = self._db.fetch_all(GET_DATE_NEWS_SQL, (date2str(search_date), ))
        return [NewsModel.from_db(i) for i in news]

    @override
    def search_news_list(self, search_str: str, page: int = 1) -> NewsListResponseModel:
        search_str = search_str.lower()
        page_size = 10
        offset = (page - 1) * page_size
        found_raw_news = self._db.fetch_all(SEARCH_NEWS_SQL, params=(search_str, page_size, offset))
        news = [NewsModel.from_db(raw_item) for raw_item in found_raw_news]
        raw_count_news = self._db.fetch_one(GET_COUNT_NEWS_SQL, params=(search_str,))
        count_news = int(raw_count_news[0])
        left_news = count_news - page_size - offset
        pagination = PaginationModel(
            has_previous_page=page != 1,
            has_next_page=left_news > 0,
            current_page=page
        )
        return NewsListResponseModel(
            news_list=news,
            pagination=pagination
        )
