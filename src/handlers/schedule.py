from fastapi import APIRouter

from src import loader
from src.models.news_list_response_model import NewsListResponseModel
from src.models.response_group_schedule_model import ResponseGroupScheduleModel
from src.models.singular_news_model import SingularNewsModel

router = APIRouter(prefix='/schedule')


@router.get(
    "/group/{group_id}",
    tags=["schedule"],
    responses={
        200: {"model": ResponseGroupScheduleModel, "description": "Расписание группы"},
        404: {"model": str, "description": "Group not found"},
        503: {"model": str, "description": "Error getting group schedule"}
    },
)
async def get_group_schedule(group_id: str, start_date: str, end_date: str):
    group_schedule = loader.schedule_service.fetch_group_schedule(group_id=group_id,date_start=start_date, date_end=end_date)
    return group_schedule


