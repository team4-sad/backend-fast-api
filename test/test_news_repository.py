import unittest

from bs4 import BeautifulSoup

from src.repositories.news_repository import NewsRepository


class NewsRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.news_repository = NewsRepository(
            base_singular_news="https://miigaik.ru/about/news",
            base_news_list_url="https://miigaik.ru/about/news/?PAGEN_2="
        )

    def test_get_list_news_html(self):
        news_list = self.news_repository.get_news_list(1)
        BeautifulSoup(news_list, "html.parser")

    def test_invalid_range_page_get_list_news_html(self):
        with self.assertRaises(ValueError):
            self.news_repository.get_news_list(-1)

    def test_get_eq_list_news_html(self):
        news_list_1 = self.news_repository.get_news_list(1)
        news_list_2 = self.news_repository.get_news_list(1)
        self.assertEqual(news_list_1, news_list_2)

    def test_get_different_list_news_html(self):
        news_list_1 = self.news_repository.get_news_list(1)
        news_list_2 = self.news_repository.get_news_list(2)
        self.assertNotEqual(news_list_1, news_list_2)

    def test_get_singular_news_html(self):
        singular_news = self.news_repository.get_singular_news(6624)
        BeautifulSoup(singular_news, "html.parser")

    def test_get_different_singular_news_html(self):
        singular_news_1 = self.news_repository.get_singular_news(6624)
        singular_news_2 = self.news_repository.get_singular_news(6623)
        self.assertNotEqual(singular_news_1, singular_news_2)

if __name__ == '__main__':
    unittest.main()
