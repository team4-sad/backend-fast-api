import urllib3
from urllib3.exceptions import InsecureRequestWarning

from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.parsers.news_parser import NewsParser
from src.repositories.migration_news_repository import MigrationNewsRepository
from src.repositories.news_repository import NewsRepository
from src.services.news_service import NewsService

urllib3.disable_warnings(InsecureRequestWarning)

config = Config()

db = SQLiteDatabase()

news_parser = NewsParser(config.BASE_LINK_URL)
news_repository = NewsRepository(config.BASE_NEWS_LIST_URL, config.BASE_SINGULAR_NEWS)
migration_repository = MigrationNewsRepository(db)
news_service = NewsService(news_parser, news_repository, migration_repository)

with db:
    if not db.table_exists("news"):
        db.execute_script(CREATE_TABLE_NEWS_SQL)
    news_service.migration(
        on_launch_migration_page=lambda page: print(f"{page=}"),
        on_migrated_page=lambda page, new_news: print(f"Complete, added {len(new_news)} news"),
    )

print("Migration complete")