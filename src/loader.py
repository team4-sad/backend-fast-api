from src.config.config import Config
from src.parsers.news_parser import NewsParser
from src.repositories.news_repository import NewsRepository
from src.services.news_service import NewsService

config = Config()

news_repository = NewsRepository(
    base_singular_news_url=config.BASE_SINGULAR_NEWS,
    base_news_list_url=config.BASE_NEWS_LIST_URL
)

news_parser = NewsParser(base_link_url=config.BASE_LINK_URL)

news_service = NewsService(
    news_parser=news_parser,
    news_repository=news_repository
)
