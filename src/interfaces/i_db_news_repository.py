import abc

from src.models.news_model import NewsModel


class IDbNewsRepository(abc.ABC):

    def get_searched_news_list(self, search_str: str) -> list[NewsModel]:
        pass