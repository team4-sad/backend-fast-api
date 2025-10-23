import os
import unittest

from src.database.sqlite_database import SQLiteDatabase
from src.database.sqls import CREATE_TABLE_NEWS_SQL
from src.exceptions.code_exception import CodeException
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel
from src.models.singular_news_model import SingularNewsModel
from src.parsers.news_parser import NewsParser
from src.repositories.db_news_repository import DbNewsRepository
from src.repositories.migration_news_repository import MigrationNewsRepository
from src.services.news_service import NewsService
from test.mock.classes.mock_corrupted_news_repository import MockCorruptedNewsRepository
from test.mock.classes.mock_news_repository import MockNewsRepository
from test.test_db_news_repository import TEST_DATABASE_NAME
from test.utils import html_mock, json_mock


class NewsServiceTest(unittest.TestCase):
    def setUp(self):
        self.database = SQLiteDatabase(TEST_DATABASE_NAME)
        self.database.connect()
        if not self.database.table_exists("news"):
            self.database.execute_script(CREATE_TABLE_NEWS_SQL)
        self.db_news_repository = DbNewsRepository(database=self.database)
        self.news_service = NewsService(
            news_parser=NewsParser(base_link_url="https://miigaik.ru"),
            news_repository=MockNewsRepository(),
            db_news_repository=self.db_news_repository,
            migration_news_repository=MigrationNewsRepository(db=SQLiteDatabase())
        )
        self.corrupted_news_service = NewsService(
            news_parser=NewsParser(base_link_url="https://miigaik.ru"),
            news_repository=MockCorruptedNewsRepository(),
            db_news_repository=self.db_news_repository,
            migration_news_repository=MigrationNewsRepository(db=SQLiteDatabase())
        )

    def fill_up(self, name: str) -> None:
        sample_news = json_mock(name)
        for news_item in sample_news:
            self.database.insert("news", news_item)

    def tearDown(self):
        self.database.close()
        if os.path.exists(TEST_DATABASE_NAME):
            os.remove(TEST_DATABASE_NAME)

    def test_get_list_news(self):
        result = self.news_service.get_news_list(1)
        self.assertEqual(
            result,
            NewsListResponseModel(
                news_list=[
                    NewsModel(id='6614',
                              header='День воссоединения ДНР, '
                                     'ЛНР, Запорожской и '
                                     'Херсонской областей с '
                                     'Российской Федерацией',
                              date_created='30.09.2025',
                              news_link='https://miigaik.ru/about/news/6614/',
                              image_link='https://miigaik.ru/upload/iblock/358/g5xbjld3fng4cl1024pdt9z2hvguhmvz.png',
                              description='Установлен в 2023 году '
                                          'Указом президента РФ'),
                    NewsModel(id='6615',
                              header='В МИИГАиК завершилась '
                                     'проектно-аналитическая '
                                     'сессия в рамках '
                                     'кросс-вузовской экспертизы',
                              date_created='30.09.2025',
                              news_link='https://miigaik.ru/about/news/6615/',
                              image_link='https://miigaik.ru/upload/iblock/aea/vt7uabx3euuz478lw5lxech55n5gi90j.png',
                              description='Завершившаяся сессия '
                                          'стала не только '
                                          'площадкой для '
                                          'выработки решений, но '
                                          'и важным шагом к '
                                          'сплочению коллектива.')
                ],
                pagination=PaginationModel(
                    has_previous_page=False,
                    current_page=1,
                    has_next_page=True
                )
            )

        )

    def test_get_singular_news_html(self):
        result = self.news_service.get_singular_news(1)
        self.assertEqual(
            result,
            SingularNewsModel(
                header='Студенты МИИГАиК на фестивале "Открытый город"',
                date_created='22.09.2025',
                content_html=html_mock("singular_news_content.html")
            )
        )

    def test_get_corrupted_news_list(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_news_service.get_news_list(1)
        self.assertEqual(e.exception, CodeException('Failed to process news list', 424))

    def test_get_corrupted_singular_news(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_news_service.get_singular_news(1)
        self.assertEqual(e.exception, CodeException('Failed to process singular news', 424))

    def test_search_news(self):
        self.fill_up("news-5.json")
        result = self.news_service.search_news(search_text="тех", page=1)
        self.assertEqual(
            result,
            NewsListResponseModel(
                news_list=[
                    NewsModel(
                        id='1002',
                        header='Техническое обслуживание серверов',
                        date_created='17.10.2025',
                        news_link='https://example.com/news/2',
                        image_link='https://example.com/images/cover2.jpg',
                        description='Запланировано техническое обслуживание на 15 января. Сервис будет недоступен с 02:00 до 06:00.'
                    ),
                    NewsModel(
                        id='1003',
                        header='Партнерство с технологическим гигантом',
                        date_created='17.10.2025',
                        news_link='https://example.com/news/3',
                        image_link='https://example.com/images/partnership.jpg',
                        description='Заключено стратегическое партнерство с ведущей технологической компанией для развития инноваций.'
                    )
                ],
                pagination=PaginationModel(
                    has_previous_page=False,
                    current_page=1,
                    has_next_page=False
                )
            )
        )

    def test_search_news_empty(self):
        self.fill_up("news-5.json")
        result = self.news_service.search_news(search_text="бобры", page=1)
        self.assertEqual(
            result,
            NewsListResponseModel(
                news_list=[],
                pagination=PaginationModel(
                    has_previous_page=False,
                    current_page=1,
                    has_next_page=False
                )
            )
        )

    def test_db_news_repository_pagination(self):
        self.fill_up("news-20.json")
        result = self.news_service.search_news("е")
        page = 1
        while result.pagination.has_next_page:
            self.assertEqual(result.pagination, PaginationModel(
                has_previous_page=page != 1,
                has_next_page=True,
                current_page=page
            ))
            page += 1
            result = self.news_service.search_news("а", page)
        self.assertEqual(result.pagination, PaginationModel(
            has_previous_page=True,
            has_next_page=False,
            current_page=page
        ))
