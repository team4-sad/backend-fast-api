from unittest import TestCase

from src.config.config import Config
from src.enums.required_news_fields import RequiredNewsFields
from src.exceptions.invalid_news_html import InvalidNewsHTML
from src.exceptions.invalid_pagination_html import InvalidPaginationHTML
from src.exceptions.invalid_singular_news_html import InvalidSingularNewsHTML
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel
from src.models.singular_news_model import SingularNewsModel
from src.parsers.news_parser import NewsParser
from test.utils import html_mock


class ParserTest(TestCase):

    def setUp(self):
        self.news_list_html = html_mock("news_list_first_page.html")
        self.news_list_without_optional_fields_html = html_mock("news_list_without_optional_fields.html")
        self.news_list_invalid_header_html = html_mock("news_list_invalid_header.html")
        self.news_list_invalid_date_html = html_mock("news_list_invalid_date.html")
        self.news_list_invalid_news_link_html = html_mock("news_list_invalid_news_link.html")
        self.news_list_invalid_html = html_mock("news_list_invalid.html")
        self.news_list_last_page_html = html_mock("news_list_last_page.html")
        self.news_list_invalid_pagination_html = html_mock("news_list_invalid_pagination.html")

        self.singular_news_html = html_mock("singular_news.html")
        self.singular_news_content_html = html_mock("singular_news_content.html")
        self.singular_news_invalid_header_html = html_mock("singular_news_invalid_header.html")
        self.singular_news_invalid_date_html = html_mock("singular_news_invalid_date.html")
        self.singular_news_invalid_content_html = html_mock("singular_news_invalid_content.html")


        config = Config(path_env="../.env")
        self.parser = NewsParser(base_link_url=config.base_link_url)

    def test_parse_news_list(self):
        result = self.parser.parse_news_list(self.news_list_html)
        self.assertEqual(
            result,
            [
                NewsModel(
                    id="6614",
                    header='День воссоединения ДНР, ЛНР, Запорожской и Херсонской областей с Российской Федерацией',
                    date_created="30.09.2025",
                    news_link="https://miigaik.ru/about/news/6614/",
                    image_link="https://miigaik.ru/upload/iblock/358/g5xbjld3fng4cl1024pdt9z2hvguhmvz.png",
                    description="Установлен в 2023 году Указом президента РФ"
                ),
                NewsModel(
                    id="6615",
                    header='В МИИГАиК завершилась проектно-аналитическая сессия в рамках кросс-вузовской экспертизы',
                    date_created="30.09.2025",
                    news_link="https://miigaik.ru/about/news/6615/",
                    image_link="https://miigaik.ru/upload/iblock/aea/vt7uabx3euuz478lw5lxech55n5gi90j.png",
                    description="Завершившаяся сессия стала не только площадкой для выработки решений, но и важным шагом к сплочению коллектива."
                ),
            ]
        )

    def test_parse_news_list_without_optional_fields(self):
        result = self.parser.parse_news_list(self.news_list_without_optional_fields_html)
        self.assertEqual(
            result,
            [
                NewsModel(
                    id="6600",
                    header='Куликовская битва',
                    date_created="21.09.2025",
                    news_link="https://miigaik.ru/about/news/6600/",
                    image_link="https://miigaik.ru/upload/iblock/3a5/tjryh90l274uerst9k32v5pvhb03bqgc.png",
                ),
                NewsModel(
                    id="6408",
                    header='В МИИГАиК началось обучение специалистов в рамках федерального проекта «Кадры для беспилотных авиационных систем»',
                    date_created="01.07.2025",
                    news_link="https://miigaik.ru/about/news/6408/",
                    description="Университет МИИГАиК стал одним из победителей открытого отбора образовательных организаций по подготовке специалистов в рамках федерального проекта «Кадры для беспилотных авиационных систем» в 2024 году."
                ),
                NewsModel(
                    id="6409",
                    header='В МИИГАиК началось обучение специалистов в рамках федерального проекта «Кадры для беспилотных авиационных систем»',
                    date_created="01.07.2025",
                    news_link="https://miigaik.ru/about/news/6409/"
                ),
            ]
        )

    def test_news_list_incorrect_header(self):
        self.parser.on_not_found_field = lambda _, e: self.assertEqual(e, RequiredNewsFields.header)
        result = self.parser.parse_news_list(self.news_list_invalid_header_html)
        self.assertTrue(len(result) == 2)

    def test_news_list_incorrect_date(self):
        self.parser.on_not_found_field = lambda _, e: self.assertEqual(e, RequiredNewsFields.date)
        result = self.parser.parse_news_list(self.news_list_invalid_date_html)
        self.assertTrue(len(result) == 2)

    def test_news_list_incorrect_news_link(self):
        self.parser.on_not_found_field = lambda _, e: self.assertEqual(e, RequiredNewsFields.news_link)
        result = self.parser.parse_news_list(self.news_list_invalid_news_link_html)
        self.assertTrue(len(result) == 2)

    def test__news_list_invalid(self):
        with self.assertRaises(InvalidNewsHTML):
            self.parser.parse_news_list(self.news_list_invalid_html)

    def test_instance_pagination(self):
        result = self.parser.parse_pagination(self.news_list_html)
        self.assertIsInstance(result, PaginationModel)

    def test_current_pagination(self):
        result = self.parser.parse_pagination(self.news_list_html)
        self.assertEqual(result.current_page, 1)

    def test_prev_pagination(self):
        result = self.parser.parse_pagination(self.news_list_html)
        self.assertEqual(result.has_previous_page, False)

    def test_next_pagination(self):
        result = self.parser.parse_pagination(self.news_list_html)
        self.assertEqual(result.has_next_page, True)

    def test_last_page_previous_pagination(self):
        result = self.parser.parse_pagination(self.news_list_last_page_html)
        self.assertEqual(result.has_previous_page, True)

    def test_last_page_next_pagination(self):
        result = self.parser.parse_pagination(self.news_list_last_page_html)
        self.assertEqual(result.has_next_page, False)

    def test_invalid_pagination_html(self):
        with self.assertRaises(InvalidPaginationHTML):
            self.parser.parse_pagination(self.news_list_invalid_pagination_html)

    def test_instance_singular_news(self):
        result = self.parser.parse_singular_news(self.singular_news_html)
        self.assertIsInstance(result, SingularNewsModel)

    def test_parse_singular_news(self):
        result = self.parser.parse_singular_news(self.singular_news_html)
        self.assertEqual(result, SingularNewsModel(
            header='Студенты МИИГАиК на фестивале "Открытый город"',
            date_created="22.09.2025",
            content_html=self.singular_news_content_html
        ))

    def test_invalid_singular_news_header_html(self):
        with self.assertRaises(InvalidSingularNewsHTML) as e:
            self.parser.parse_singular_news(self.singular_news_invalid_header_html)
        self.assertEqual(e.exception.field, RequiredNewsFields.header)

    def test_invalid_singular_news_date_html(self):
        with self.assertRaises(InvalidSingularNewsHTML) as e:
            self.parser.parse_singular_news(self.singular_news_invalid_date_html)
        self.assertEqual(e.exception.field, RequiredNewsFields.date)

    def test_invalid_singular_news_content_html(self):
        with self.assertRaises(InvalidSingularNewsHTML) as e:
            self.parser.parse_singular_news(self.singular_news_invalid_content_html)
        self.assertEqual(e.exception.field, RequiredNewsFields.content)
