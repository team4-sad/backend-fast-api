from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.parsers.news_parser import NewsParser
from src.repositories.news_repository import NewsRepository
from src.repositories.schedule_repository import ScheduleRepository
from src.services.lk_service import LkService
from src.services.news_service import NewsService
from src.services.schedule_service import ScheduleService
from src.storage.news_storage import NewsStorage
from test.mock.classes.mock_lk_repository import MockLkRepository

config = Config()

database = SQLiteDatabase(config.database_path)
database.connect()

if not database.table_exists("news"):
    database.execute_script(CREATE_TABLE_NEWS_SQL)

news_repository = NewsRepository(
    base_singular_news_url=config.base_singular_news,
    base_news_list_url=config.base_news_list_url
)

news_storage = NewsStorage(
    database=database
)

news_parser = NewsParser(
    base_link_url=config.base_link_url
)

news_service = NewsService(
    news_parser=news_parser,
    news_repository=news_repository,
    news_storage=news_storage
)

schedule_repository = ScheduleRepository(
    base_url=config.base_schedule_api_url
)

schedule_service = ScheduleService(
    schedule_repository=schedule_repository
)

lk_repository = MockLkRepository()

lk_service = LkService(
    lk_repository=lk_repository
)
