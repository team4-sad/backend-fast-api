from src.parsers.news_parser import NewsParser
from src.repositories.news_repository import NewsRepository
from src.services.news_service import NewsService

news_repository = NewsRepository(
    base_singular_news="https://miigaik.ru/about/news",
    base_news_list_url="https://miigaik.ru/about/news/?PAGEN_2="
)

news_parser = NewsParser(base_link_url="https://miigaik.ru")

news_service = NewsService(
    news_parser=news_parser,
    news_repository=news_repository
)