import traceback
from datetime import datetime

import urllib3
from urllib3.exceptions import InsecureRequestWarning
from src.config.config import Config
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.parsers.news_parser import NewsParser
from src.repositories.news_repository import NewsRepository
from src.database.sqlite_database import SQLiteDatabase

urllib3.disable_warnings(InsecureRequestWarning)

config = Config()

news_repository = NewsRepository(
    base_news_list_url=config.base_news_list_url,
    base_singular_news_url=config.base_singular_news
)
parser = NewsParser(config.base_link_url)

sqlite_db = SQLiteDatabase()
with sqlite_db as db:
    if not sqlite_db.table_exists("news"):
        sqlite_db.execute_script(CREATE_TABLE_NEWS_SQL)

    page = 1
    while True:
        print("PAGE: ", page)
        html = news_repository.get_news_list(page)
        pagination = parser.parse_pagination(html)
        news_list = parser.parse_news_list(html)
        db_news_list = [i.to_db() for i in news_list]
        try:
            sqlite_db.insert_many("news", db_news_list)
        except Exception as e:
            print(f"Ошибка вставки данных - {e}")
            print(traceback.format_exc())
        if not pagination.has_next_page:
            break
        page += 1

    sql_file_name = f"dump-news-{datetime.now().strftime('%d%m%Y-%H%M%S')}.sql"
    print(f"Scrapping finished - {sql_file_name}")
    sqlite_db.dump_to_file(sql_file_name)
