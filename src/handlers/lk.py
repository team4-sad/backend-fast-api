from fastapi import APIRouter, Header

from src import loader
from src.models.lk_profile_model import LkProfileModel


router = APIRouter(prefix='/lk')

@router.get(
    "/me",
    tags=["lk"],
    responses={
        200: {"model": LkProfileModel, "description": "Модель профиля"},
        401: {"model": str, "description": "Ошибка при взаимодействии со сторонним ресурсом"},
        503: {},
    },
)
async def get_me(access_token: str = Header(alias="Authorization")):
    result = loader.lk_service.get_me(access_token=access_token)
    return result
