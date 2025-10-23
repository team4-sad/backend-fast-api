from collections.abc import Callable
from functools import reduce

from src.exceptions.code_exception import CodeException
from src.exceptions.invalid_news_html import InvalidNewsHTML
from src.exceptions.invalid_pagination_html import InvalidPaginationHTML
from src.exceptions.invalid_singular_news_html import InvalidSingularNewsHTML
from src.interfaces.i_db_news_repository import IDbNewsRepository
from src.interfaces.i_migration_news_repository import IMigrationNewsRepository
from src.interfaces.i_news_repository import INewsRepository
from src.interfaces.i_news_service import INewsService
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.singular_news_model import SingularNewsModel
from src.parsers.news_parser import NewsParser


class NewsService(INewsService):

    def __init__(
        self,
        news_parser: NewsParser,
        news_repository: INewsRepository,
        migration_news_repository: IMigrationNewsRepository,
        db_news_repository: IDbNewsRepository
    ):
        self.news_parser = news_parser
        self.news_repository = news_repository
        self.migration_news_repository = migration_news_repository,
        self.db_news_repository = db_news_repository

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

    def migration(
        self,
        on_launch_migration_page: Callable[[int], None] | None = None,
        on_migrated_page: Callable[[int, list[NewsModel]], None] | None = None,
    ):
        page = 1
        last_db_news = self.migration_news_repository.get_last_saved_news()
        if last_db_news is not None:
            last_saved_date = last_db_news.date_date_created
            news_with_last_saved_date = self.migration_news_repository.get_news_by_date(last_saved_date)
        else:
            last_saved_date = None
            news_with_last_saved_date = []
        while True:
            if on_launch_migration_page is not None:
                on_launch_migration_page(page)
            has_not_saved_news = False
            html = self.news_repository.get_news_list(page)
            pagination = self.news_parser.parse_pagination(html)
            news_list = self.news_parser.parse_news_list(html)
            inserted_news = []
            for single_news in news_list:
                is_need_save = False
                if last_saved_date is None:
                    is_need_save = True
                elif single_news.date_date_created > last_saved_date:
                    is_need_save = True
                elif single_news.date_date_created == last_saved_date:
                    is_need_save = all([i.id != single_news.id for i in news_with_last_saved_date])
                if is_need_save:
                    self.migration_news_repository.save_single_news(single_news)
                    has_not_saved_news = True
                    inserted_news.append(single_news)
            if on_migrated_page is not None:
                on_migrated_page(page, inserted_news)
            if not pagination.has_next_page or not has_not_saved_news:
                break
            page += 1

    def search_news(
            self,
            search_text: str,
            page: int = 1
    )->NewsListResponseModel:
        try:
            news_list_response_model = self.db_news_repository.search_news_list(search_str=search_text, page=page)
        except:
            raise CodeException(message="something went wrong", error_code=503)
        return news_list_response_model