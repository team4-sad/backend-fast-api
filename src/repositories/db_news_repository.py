import requests

from src.database.sqls import GET_PAGINATED_NEWS_SQL, GET_TOTAL_NEWS_COUNT_SQL
from src.interfaces.i_news_repository import INewsRepository
from src.database.sqlite_database import SQLiteDatabase
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel


class DbNewsRepository(INewsRepository):
    def __init__(self, database: SQLiteDatabase, base_singular_news_url: str):
        self.database = database
        self.base_singular_news = base_singular_news_url


    def get_news_list(self, page: int = 1) -> NewsListResponseModel:

        page_size = 10
        offset = (page - 1) * page_size
        raw_news = self.database.fetch_all(GET_PAGINATED_NEWS_SQL, params=(page_size, offset))
        news = [NewsModel.from_db(raw_item) for raw_item in raw_news]
        raw_count_news = self.database.fetch_one(GET_TOTAL_NEWS_COUNT_SQL)
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

    def get_singular_news(self, news_id: int) -> str:
        singular_news_page = requests.get(f"{self.base_singular_news}/{news_id}/", verify=False)
        singular_news_page.raise_for_status()
        return singular_news_page.text