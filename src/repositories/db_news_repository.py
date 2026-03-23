from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import SEARCH_NEWS_SQL, GET_COUNT_NEWS_SQL
from src.interfaces.i_db_news_repository import IDbNewsRepository
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel


class DbNewsRepository(IDbNewsRepository):
    def __init__(self, database: SQLiteDatabase):
        self.database = database