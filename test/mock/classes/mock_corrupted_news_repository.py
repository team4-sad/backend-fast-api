from src.interfaces.i_news_repository import INewsRepository
from test.utils import mock


class MockCorruptedNewsRepository(INewsRepository):

    def get_news_list(self, page: int) -> str:
        return mock("mock/html/news_list_invalid.html")

    def get_singular_news(self, news_id: int) -> str:
        return mock("mock/html/singular_news_invalid_content.html")

