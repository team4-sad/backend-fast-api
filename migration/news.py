import urllib3
from urllib3.exceptions import InsecureRequestWarning

from src.config.config import Config
from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.interfaces.i_news_repository import INewsRepository
from src.interfaces.i_news_storage import INewsStorage
from src.parsers.news_parser import NewsParser
from src.repositories.news_repository import NewsRepository
from src.storage.news_storage import NewsStorage

urllib3.disable_warnings(InsecureRequestWarning)


def migrate(
    news_repository: INewsRepository,
    news_storage: INewsStorage,
    news_parser: NewsParser
):
    page = 1
    last_db_news = news_storage.get_last_saved_news()
    if last_db_news is not None:
        last_saved_date = last_db_news.date_date_created
        news_with_last_saved_date = news_storage.get_news_by_date(last_saved_date)
    else:
        last_saved_date = None
        news_with_last_saved_date = []
    while True:
        print(f"{page=}")
        has_not_saved_news = False
        html = news_repository.get_news_list(page)
        pagination = news_parser.parse_pagination(html)
        news_list = news_parser.parse_news_list(html)
        inserted_news = []
        for single_news in news_list:
            is_need_save = False
            if last_saved_date is None:
                is_need_save = True
            elif single_news.date_date_created > last_saved_date:
                is_need_save = True
            elif single_news.date_date_created == last_saved_date:
                is_need_save = all([i.id != single_news.id for i in news_with_last_saved_date])
            if is_need_save:
                news_storage.save_single_news(single_news)
                has_not_saved_news = True
                inserted_news.append(single_news)
        print(f"Complete, added {len(inserted_news)} news")
        if not pagination.has_next_page or not has_not_saved_news:
            break
        page += 1


if __name__ == "__main__":
    config = Config()
    db = SQLiteDatabase()
    parser = NewsParser(config.base_link_url)
    repository = NewsRepository(config.base_news_list_url, config.base_singular_news)
    storage = NewsStorage(db)

    with db:
        if not db.table_exists("news"):
            db.execute_script(CREATE_TABLE_NEWS_SQL)
        migrate(repository, storage, parser)

    print("Migration complete")
