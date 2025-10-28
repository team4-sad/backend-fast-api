import urllib3
from urllib3.exceptions import InsecureRequestWarning

from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.parsers.news_parser import NewsParser
from src.repositories.db_news_repository import DbNewsRepository
from src.repositories.migration_news_repository import MigrationNewsRepository
from src.repositories.news_repository import NewsRepository
from src.services.news_service import NewsService

urllib3.disable_warnings(InsecureRequestWarning)

config = Config()

db = SQLiteDatabase()

news_parser = NewsParser(config.base_link_url)
news_repository = NewsRepository(config.base_news_list_url, config.base_singular_news)
migration_repository = MigrationNewsRepository(db)
db_news_repository = DbNewsRepository(database=db)
news_service = NewsService(news_parser, news_repository, migration_repository, db_news_repository)

with db:
    if not db.table_exists("news"):
        db.execute_script(CREATE_TABLE_NEWS_SQL)
    news_service.migration(
        on_launch_migration_page=lambda page: print(f"{page=}"),
        on_migrated_page=lambda page, new_news: print(f"Complete, added {len(new_news)} news"),
    )

print("Migration complete")
