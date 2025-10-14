import requests

from src.interfaces.i_news_repository import INewsRepository


class NewsRepository(INewsRepository):
    def __init__(self, base_news_list_url: str, base_singular_news_url: str):
        self.base_news_list_url = base_news_list_url
        self.base_singular_news = base_singular_news_url

    def get_news_list(self, page: int) -> str:
        if page <= 0:
            raise ValueError("page is unavailable range (<=0)")
        news_list_page = requests.get(f"{self.base_news_list_url}{page}", verify=False)
        news_list_page.raise_for_status()
        return news_list_page.text

    def get_singular_news(self, news_id: int) -> str:
        singular_news_page = requests.get(f"{self.base_singular_news}/{news_id}/", verify=False)
        singular_news_page.raise_for_status()
        return singular_news_page.text
