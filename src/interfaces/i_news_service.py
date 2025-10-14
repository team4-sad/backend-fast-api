import abc

from src.models.news_list_response_model import NewsListResponseModel
from src.models.singular_news_model import SingularNewsModel


class INewsService(abc.ABC):

    def get_news_list(self, page_numb: int) -> NewsListResponseModel:
        pass

    def get_singular_news(self, news_id: int) -> SingularNewsModel:
        pass
