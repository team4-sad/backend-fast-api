from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.parsers.news_parser import NewsParser
from src.repositories.db_news_repository import DbNewsRepository
from src.repositories.migration_news_repository import MigrationNewsRepository
from src.repositories.news_repository import NewsRepository
from src.services.news_service import NewsService

config = Config()

database = SQLiteDatabase(config.DATABASE_PATH)
database.connect()

if not database.table_exists("news"):
    database.execute_script(CREATE_TABLE_NEWS_SQL)

news_repository = NewsRepository(
    base_singular_news_url=config.BASE_SINGULAR_NEWS,
    base_news_list_url=config.BASE_NEWS_LIST_URL
)

news_parser = NewsParser(base_link_url=config.BASE_LINK_URL)

news_service = NewsService(
    news_parser=news_parser,
    news_repository=news_repository,
    migration_news_repository=MigrationNewsRepository(db=database),
    db_news_repository=DbNewsRepository(database)
)
