import os
from unittest import TestCase

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel
from src.repositories.db_news_repository import DbNewsRepository
from test.utils import json_mock

TEST_DATABASE_NAME = 'test_database.db'

class DbNewsRepositoryTest(TestCase):
    def setUp(self):
        self.database = SQLiteDatabase(TEST_DATABASE_NAME)
        self.database.connect()
        if not self.database.table_exists("news"):
            self.database.execute_script(CREATE_TABLE_NEWS_SQL)
        self.db_news_repository = DbNewsRepository(database=self.database)

    def tearDown(self):
        self.database.close()
        if os.path.exists(TEST_DATABASE_NAME):
            os.remove(TEST_DATABASE_NAME)

    def fill_up(self, name: str) -> None:
        sample_news = json_mock(name)
        for news_item in sample_news:
            self.database.insert("news", news_item)

    def test_exist_db_file(self):
        self.assertTrue(os.path.exists("test_database.db"))

    def test_search_db(self):
        self.fill_up("news-5.json")
        result = self.db_news_repository.search_news_list("тех")
        self.assertEqual(result, NewsListResponseModel(
            news_list=[
                NewsModel(
                    id="1002",
                    header="Техническое обслуживание серверов",
                    date_created="17.10.2025",
                    description="Запланировано техническое обслуживание на 15 января. Сервис будет недоступен с 02:00 до 06:00.",
                    image_link="https://example.com/images/cover2.jpg",
                    news_link="https://example.com/news/2"
                ),
                NewsModel(
                    id="1003",
                    header="Партнерство с технологическим гигантом",
                    date_created="17.10.2025",
                    description="Заключено стратегическое партнерство с ведущей технологической компанией для развития инноваций.",
                    image_link="https://example.com/images/partnership.jpg",
                    news_link="https://example.com/news/3"
                )
            ],
            pagination=PaginationModel(
                is_previous_page=False,
                is_next_page=False,
                current_page=1
            )
        ))