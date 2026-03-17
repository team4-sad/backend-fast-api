from fastapi import APIRouter, Header

from src import loader
from src.models.course_education_plan_model import CourseEducationPlanModel
from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel
from src.models.order_document_model import OrderDocumentModel

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


@router.get(
    "/academic_records",
    tags=["lk"],
    responses={
        200: {"model": list[LkCourseRecordModel], "description": "Список моделей курсов"},
        401: {"model": str, "description": "Ошибка при взаимодействии со сторонним ресурсом"},
        503: {},
    },
)
async def get_academic_records(access_token: str = Header(alias="Authorization")):
    result = loader.lk_service.get_academic_records(access_token=access_token)
    return result


@router.get(
    "/education_plan",
    tags=["lk"],
    responses={
        200: {"model": list[CourseEducationPlanModel], "description": "Список моделей планов обучения на курс"},
        401: {"model": str, "description": "Ошибка при взаимодействии со сторонним ресурсом"},
        503: {},
    },
)
async def get_academic_records(access_token: str = Header(alias="Authorization")):
    result = loader.lk_service.get_education_plan(access_token=access_token)
    return result

@router.get(
    "/document/orders",
    tags=["lk"],
    responses={
        200: {"model": list[OrderDocumentModel], "description": "Список моделей заказов документов"},
        401: {"model": str, "description": "Ошибка при взаимодействии со сторонним ресурсом"},
        503: {},
    },
)
async def get_orders_document(access_token: str = Header(alias="Authorization")):
    result = loader.lk_service.get_orders_document(access_token=access_token)
    return result
