from src.interfaces.i_news_repository import INewsRepository
from test.utils import mock


class MockNewsRepository(INewsRepository):

    def get_news_list(self, page: int) -> str:
        return mock("news_list_first_page.html")

    def get_singular_news(self, news_id: int) -> str:
        return mock("singular_news.html")

