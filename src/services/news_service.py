from src.exceptions.code_exception import CodeException
from src.exceptions.invalid_news_html import InvalidNewsHTML
from src.exceptions.invalid_pagination_html import InvalidPaginationHTML
from src.exceptions.invalid_singular_news_html import InvalidSingularNewsHTML
from src.interfaces.i_news_repository import INewsRepository
from src.models.news_list_response_model import NewsListResponseModel
from src.models.singular_news_model import SingularNewsModel
from src.parsers.news_parser import NewsParser


class NewsService:

    def __init__(self, news_parser: NewsParser, news_repository: INewsRepository):
        self.news_parser = news_parser
        self.news_repository = news_repository

    def get_news_list(self, page_numb: int) -> NewsListResponseModel:
        try:
            html = self.news_repository.get_news_list(page_numb)
        except Exception:
            raise CodeException("Failed to fetch news list", 424)

        try:
            news_models = self.news_parser.parse_news_list(html=html)
        except InvalidNewsHTML:
            raise CodeException("Failed to process news list", 424)

        try:
            pagination = self.news_parser.parse_pagination(html=html)
        except InvalidPaginationHTML:
            raise CodeException("Failed to process pagination", 424)

        return NewsListResponseModel(news_list=news_models, pagination=pagination)

    def get_singular_news(self, news_id: int) -> SingularNewsModel:
        try:
            html = self.news_repository.get_singular_news(news_id)
        except Exception:
            raise CodeException("Failed to fetch singular news", 424)

        try:
            singular_news_model = self.news_parser.parse_singular_news(html)
        except InvalidSingularNewsHTML:
            raise CodeException("Failed to process singular news", 424)

        return singular_news_model
