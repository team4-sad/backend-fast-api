import abc

from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel


class INewsStorage(abc.ABC):
    def save_single_news(self, single_news: NewsModel):
        pass

    def save_news(self, news: list[NewsModel]):
        pass

    def get_last_saved_news(self) -> NewsModel | None:
        pass

    def get_news_by_date(self, search_date: str) -> list[NewsModel]:
        pass

    def search_news_list(self, search_str: str, page: int = 1) -> NewsListResponseModel:
        pass
