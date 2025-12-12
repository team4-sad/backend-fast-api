from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL, CREATE_TABLE_SCHEDULES_SQL
from src.parsers.news_parser import NewsParser
from src.repositories.db_news_repository import DbNewsRepository
from src.repositories.db_search_news_repository import DbSearchNewsRepository
from src.repositories.migration_news_repository import MigrationNewsRepository
from src.repositories.schedule_repository import ScheduleRepository
from src.repositories.signature_repository import SignatureRepository
from src.services.news_service import NewsService
from src.services.schedule_service import ScheduleService

config = Config()

database = SQLiteDatabase(config.database_path)
database.connect()

if not database.table_exists("news"):
    database.execute_script(CREATE_TABLE_NEWS_SQL)
if not database.table_exists("schedules"):
    database.execute_script(CREATE_TABLE_SCHEDULES_SQL)

news_repository = DbNewsRepository(database=database, base_singular_news_url=config.base_singular_news)

migration_repository = MigrationNewsRepository(database=database)
db_news_repository = DbSearchNewsRepository(database=database)

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

signature_repository = SignatureRepository(
    base_url=config.base_schedule_api_url
)

schedule_service = ScheduleService(
    schedule_repository=schedule_repository,
    signature_repository=signature_repository
)
