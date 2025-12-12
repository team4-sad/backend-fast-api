import abc

from src.models.news_list_response_model import NewsListResponseModel


class IDbSearchNewsRepository(abc.ABC):

    def search_news_list(self, search_str: str, page: int = 1) -> NewsListResponseModel:
        pass