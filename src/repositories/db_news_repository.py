from datetime import datetime, date, timedelta

from src.common.utils import date2str
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import SEARCH_NEWS_SQL, GET_COUNT_NEWS_SQL, GET_DATE_NEWS_SQL
from src.interfaces.i_db_news_repository import IDbNewsRepository
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel


class DbNewsRepository(IDbNewsRepository):
    def __init__(self, database: SQLiteDatabase):
        self.database = database

    def search_news_list(self, search_str: str, page: int = 1) -> NewsListResponseModel:
        search_str = search_str.lower()
        page_size = 10
        offset = (page - 1) * page_size
        found_raw_news = self.database.fetch_all(SEARCH_NEWS_SQL, params=(search_str, page_size, offset))
        news = [NewsModel.from_db(raw_item) for raw_item in found_raw_news]
        raw_count_news = self.database.fetch_one(GET_COUNT_NEWS_SQL, params=(search_str,))
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
