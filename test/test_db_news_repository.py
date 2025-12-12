import os
from unittest import TestCase

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel
from src.repositories.db_news_repository import DbNewsRepository
from test.utils import json_mock
from src.config.config import Config


TEST_DATABASE_NAME = 'test_database.db'

class DbNewsRepositoryTest(TestCase):
    def setUp(self):
        self.database = SQLiteDatabase(TEST_DATABASE_NAME)
        self.database.connect()
        if not self.database.table_exists("news"):
            self.database.execute_script(CREATE_TABLE_NEWS_SQL)
        config = Config(path_env="../.env")
        self.db_news_repository = DbNewsRepository(database=self.database, base_singular_news_url=config.base_singular_news)

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

    def test_get_news_from_db(self):
        self.fill_up("news-5.json")
        result = self.db_news_repository.get_news_list(page=1)
        self.assertEqual(result, NewsListResponseModel(news_list=[NewsModel(id='1002',
                                           header='Техническое обслуживание '
                                                  'серверов',
                                           date_created='17.10.2025',
                                           news_link='https://example.com/news/2',
                                           image_link='https://example.com/images/cover2.jpg',
                                           description='Запланировано '
                                                       'техническое '
                                                       'обслуживание на 15 '
                                                       'января. Сервис будет '
                                                       'недоступен с 02:00 до '
                                                       '06:00.'),
                                 NewsModel(id='1003',
                                           header='Партнерство с '
                                                  'технологическим гигантом',
                                           date_created='17.10.2025',
                                           news_link='https://example.com/news/3',
                                           image_link='https://example.com/images/partnership.jpg',
                                           description='Заключено '
                                                       'стратегическое '
                                                       'партнерство с ведущей '
                                                       'технологической '
                                                       'компанией для развития '
                                                       'инноваций.'),
                                 NewsModel(id='1004',
                                           header='Итоги года и новые '
                                                  'горизонты',
                                           date_created='17.10.2025',
                                           news_link='https://example.com/news/4',
                                           image_link=None,
                                           description='Подводим итоги '
                                                       'уходящего года и '
                                                       'делимся планами по '
                                                       'развитию на следующий '
                                                       'год.'),
                                 NewsModel(id='1005',
                                           header='Новые вакансии в отделе '
                                                  'разработки',
                                           date_created='17.10.2025',
                                           news_link='https://example.com/news/5',
                                           image_link='https://example.com/images/career.jpg',
                                           description='Мы расширяем команду '
                                                       'разработки и ищем '
                                                       'талантливых Python и '
                                                       'JavaScript '
                                                       'разработчиков.'),
                                 NewsModel(id='1020',
                                           header='Планы по развитию облачной '
                                                  'инфраструктуры',
                                           date_created='17.10.2025',
                                           news_link='https://example.com/news/20',
                                           image_link='https://example.com/images/cloud-infrastructure.jpg',
                                           description='Анонсируем масштабное '
                                                       'расширение облачной '
                                                       'инфраструктуры в новых '
                                                       'регионах.')],
                      pagination=PaginationModel(has_previous_page=False,
                                                 current_page=1,
                                                 has_next_page=False))
        )


    def test_pagination(self):
        self.fill_up("news-20.json")
        page = 1
        result = self.db_news_repository.get_news_list(page=page)
        while result.pagination.has_next_page:
            self.assertEqual(result.pagination, PaginationModel(
                has_previous_page=page != 1,
                has_next_page=True,
                current_page=page
            ))
            page += 1
            result = self.db_news_repository.get_news_list(page=page)
        self.assertEqual(result.pagination, PaginationModel(
            has_previous_page=True,
            has_next_page=False,
            current_page=page
        ))

    def test_get_different_pages(self):
        self.fill_up("news-20.json")
        first_page = self.db_news_repository.get_news_list(page=1)
        second_page = self.db_news_repository.get_news_list(page=2)
        self.assertNotEqual(first_page,second_page)

    def test_incorrect_pagination(self):
        self.fill_up("news-20.json")
        page = 99999
        result = self.db_news_repository.get_news_list(page=page)
        self.assertEqual(result, NewsListResponseModel(news_list=[],
                      pagination=PaginationModel(has_previous_page=True,
                                                 current_page=page,
                                                 has_next_page=False)))