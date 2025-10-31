from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.parsers.news_parser import NewsParser
from src.repositories.db_news_repository import DbNewsRepository
from src.repositories.migration_news_repository import MigrationNewsRepository
from src.repositories.news_repository import NewsRepository
from src.repositories.schedule_repository import ScheduleRepository
from src.services.news_service import NewsService
from src.services.schedule_service import ScheduleService

config = Config()

database = SQLiteDatabase(config.database_path)
database.connect()

if not database.table_exists("news"):
    database.execute_script(CREATE_TABLE_NEWS_SQL)

news_repository = NewsRepository(
    base_singular_news_url=config.base_singular_news,
    base_news_list_url=config.base_news_list_url
)

migration_repository = MigrationNewsRepository(database=database)
db_news_repository = DbNewsRepository(database=database)

news_parser = NewsParser(
    base_link_url=config.base_link_url
)

news_service = NewsService(
    news_parser=news_parser,
    news_repository=news_repository,
    migration_news_repository=migration_repository,
    db_news_repository=db_news_repository
)

schedule_repository = ScheduleRepository(
    base_url=config.base_schedule_api_url
)

schedule_service = ScheduleService(
    schedule_repository=schedule_repository
)
