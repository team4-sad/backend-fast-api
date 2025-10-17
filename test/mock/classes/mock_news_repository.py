from src.interfaces.i_news_repository import INewsRepository
from test.utils import html_mock


class MockNewsRepository(INewsRepository):

    def get_news_list(self, page: int) -> str:
        return html_mock("news_list_first_page.html")

    def get_singular_news(self, news_id: int) -> str:
        return html_mock("singular_news.html")

