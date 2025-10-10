import dataclasses

from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel


@dataclasses.dataclass
class NewsListResponseModel:
    news_list: list[NewsModel]
    pagination: PaginationModel