from typing import Callable
from bs4 import BeautifulSoup
import re
from src.enums.required_news_fields import RequiredNewsFields
from src.exceptions.invalid_news_html import InvalidNewsHTML
from src.exceptions.invalid_pagination_html import InvalidPaginationHTML
from src.exceptions.invalid_singular_news_html import InvalidSingularNewsHTML
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel
from src.models.singular_news_model import SingularNewsModel


class NewsParser:
    def __init__(
            self,
            base_link_url: str,
            on_not_found_field: Callable[[str, RequiredNewsFields], None] | None = None
    ):
        self.base_link_url = base_link_url
        self.on_not_found_field = on_not_found_field

    def parse_news_list(self, html: str) -> list[NewsModel]:
        soup = BeautifulSoup(html, "html.parser")
        tag_news_list = soup.find(class_="news-list")

        try:
            all_news = tag_news_list.find_all(class_="news-item")
        except AttributeError:
            raise InvalidNewsHTML(html)

        parsed_news = []

        for tag_news in all_news:
            try:
                header = tag_news.find("h3", class_="news-item-header").text.strip()
                header = normalize_spaces(header)
            except AttributeError:
                self.on_not_found_field(str(tag_news), RequiredNewsFields.header)
                continue

            raw_description = tag_news.find("div", class_="news-item-text").text
            description = raw_description.replace(f"\n{header}\n", "").strip()
            if description == "":
                description = None
            else:
                description = normalize_spaces(description)

            try:
                date = tag_news.find("div", class_="news-item-date").text
            except AttributeError:
                self.on_not_found_field(str(tag_news), RequiredNewsFields.date)
                continue

            try:
                short_news_link = tag_news.find("a").get("href")
                news_id = short_news_link.split("/")[-2]
                news_link = self.base_link_url + tag_news.find("a").get("href")
            except AttributeError:
                self.on_not_found_field(str(tag_news), RequiredNewsFields.news_link)
                continue

            try:
                image_link = self.base_link_url + tag_news.find("img").get("src")
            except AttributeError:
                image_link = None

            news = NewsModel(
                id=news_id,
                header=header,
                date_created=date,
                news_link=news_link,
                image_link=image_link,
                description=description
            )
            parsed_news.append(news)

        return parsed_news

    def parse_pagination(self, html: str) -> PaginationModel:
        soup = BeautifulSoup(html, "html.parser")
        page_navigator = soup.find(class_="modern-page-navigation")
        if page_navigator is None:
            raise InvalidPaginationHTML(html)
        is_previous_page = page_navigator.find(class_="modern-page-previous") is not None
        current_page = int(page_navigator.find(class_="modern-page-current").text)
        is_next_page = page_navigator.find(class_="modern-page-next") is not None

        return PaginationModel(is_previous_page, current_page, is_next_page)

    def parse_singular_news(self, html: str) -> SingularNewsModel:
        soup = BeautifulSoup(html, "html.parser")

        try:
            header = normalize_spaces(soup.find("h1").text.strip())
        except AttributeError:
            raise InvalidSingularNewsHTML(html, RequiredNewsFields.header)

        try:
            date = soup.find(class_="news-item-date fl-l mt10").text
        except AttributeError:
            raise InvalidSingularNewsHTML(html, RequiredNewsFields.date)

        try:
            content = soup.find(class_="news-item-text clearfix").decode_contents().strip()
        except AttributeError:
            raise InvalidSingularNewsHTML(html, RequiredNewsFields.content)

        return SingularNewsModel(header, date, content)


def normalize_spaces(text, replace_n: bool = True) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    text = text.replace('\t', ' ')
    text = text.replace('\r', ' ')
    if replace_n:
        text = text.replace('\n', ' ')
    text = re.sub(r' +', ' ', text)
    return text
