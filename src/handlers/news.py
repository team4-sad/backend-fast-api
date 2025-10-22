from fastapi import APIRouter

from src import loader
from src.models.news_list_response_model import NewsListResponseModel
from src.models.singular_news_model import SingularNewsModel

router = APIRouter(prefix='/news')


@router.get(
    "/",
    tags=["news"],
    responses={
        200: {"model": NewsListResponseModel, "description": "Список новостей с состоянием пагинации"},
        424: {"model": str, "description": "Ошибка при взаимодействии со сторонним ресурсом"},
    },
)
async def get_news_list(page: int = 1):
    news_list = loader.news_service.get_news_list(page_numb=page)
    return news_list


@router.get(
    "/{news_id}",
    tags=["news"],
    responses={
        200: {"model": SingularNewsModel, "description": "Одна новость"},
        424: {"model": str, "description": "Ошибка при взаимодействии со сторонним ресурсом"},
    },
)
async def get_singular_news(news_id: int):
    singular_news = loader.news_service.get_singular_news(news_id=news_id)
    return singular_news
