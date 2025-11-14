from fastapi import APIRouter

from src import loader
from src.models.classrooms_info_model import ClassroomsInfoModel
from src.models.groups_info_model import GroupsInfoModel
from src.models.response_group_schedule_model import ResponseGroupScheduleModel
from src.models.response_teacher_schedule_model import ResponseTeacherScheduleModel
from src.models.teacher_model import TeacherModel
from src.models.teachers_info_model import TeachersInfoModel

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
    group_schedule = loader.schedule_service.fetch_group(group_id=group_id, date_start=start_date, date_end=end_date)
    return group_schedule


@router.get(
    "/teacher/{teacher_id}",
    tags=["schedule"],
    responses={
        200: {"model": ResponseTeacherScheduleModel, "description": "Расписание преподавателя"},
        404: {"model": str, "description": "Teacher not found"},
        503: {"model": str, "description": "Error getting teacher schedule"}
    },
)
async def get_teacher_schedule(teacher_id: str, start_date: str, end_date: str):
    teacher_schedule = loader.schedule_service.fetch_teacher_schedule(
        teacher_id=teacher_id, date_start=start_date, date_end=end_date
    )
    return teacher_schedule


@router.get(
    "/classroom/{classroom_id}",
    tags=["schedule"],
    responses={
        200: {"model": ResponseTeacherScheduleModel, "description": "Расписание аудитории"},
        404: {"model": str, "description": "Classroom not found"},
        503: {"model": str, "description": "Error getting teacher classroom"}
    },
)
async def get_classroom_schedule(classroom_id: str, start_date: str, end_date: str):
    classroom_schedule = loader.schedule_service.fetch_classroom_schedule(
        classroom_id=classroom_id, date_start=start_date, date_end=end_date
    )
    return classroom_schedule


@router.get(
    "/groups/{group}",
    tags=["schedule"],
    responses={
        200: {"model": list[GroupsInfoModel], "description": "Поиск группы"},
        503: {"model": str, "description": "Error getting group list"}
    },
)
async def get_list_teachers(group: str):
    teachers = loader.schedule_service.fetch_groups_list(group_name=group)
    return teachers


@router.get(
    "/classrooms/{classroom}",
    tags=["schedule"],
    responses={
        200: {"model": list[ClassroomsInfoModel], "description": "Поиск аудиторий"},
        503: {"model": str, "description": "Error getting classrooms list"}
    },
)
async def get_list_classrooms(classroom: str):
    classrooms = loader.schedule_service.fetch_classrooms_list(classroom=classroom)
    return classrooms


@router.get(
    "/teachers/{teacher}",
    tags=["schedule"],
    responses={
        200: {"model": list[TeachersInfoModel], "description": "Поиск преподавателя"},
        503: {"model": str, "description": "Error getting teachers list"}
    },
)
async def get_list_teachers(teacher: str):
    teachers = loader.schedule_service.fetch_teachers_list(teacher_name=teacher)
    return teachers
