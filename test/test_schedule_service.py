import unittest

from src.exceptions.code_exception import CodeException
from src.exceptions.invalid_schedule_exception import InvalidScheduleException
from src.models.classrooms_info_model import ClassroomsInfoModel
from src.models.day_model import DayModel
from src.models.groups_info_model import GroupsInfoModel
from src.models.lesson_model import LessonModel
from src.models.response_group_schedule_model import ResponseGroupScheduleModel
from src.models.teacher_model import TeacherModel
from src.models.teachers_info_model import TeachersInfoModel
from src.services.schedule_service import ScheduleService
from test.mock.classes.mock_schedule_repository import MockScheduleRepository, CorruptedNotFoundMockScheduleRepository, \
    CorruptedExceptionMockScheduleRepository, EmptyMockScheduleRepository


class ScheduleServiceTest(unittest.TestCase):
    def setUp(self):
        self.schedule_service = ScheduleService(MockScheduleRepository())
        self.corrupted_not_found_schedule_service = ScheduleService(CorruptedNotFoundMockScheduleRepository())
        self.corrupted_exception_schedule_service = ScheduleService(CorruptedExceptionMockScheduleRepository())
        self.corrupted_empty_schedule_service = ScheduleService(EmptyMockScheduleRepository())

    def test_get_schedule_group(self):
        result = self.schedule_service.fetch_group_schedule("123", "123", "123")
        self.assertEqual(
            result,
            ResponseGroupScheduleModel(
                group_name="2023-ФГиИБ-ПИ-1б",
                schedule=[
                    DayModel(
                        day_of_week=2,
                        name_day_of_week="вторник",
                        date="2025-10-14",
                        lessons=[LessonModel(
                            lesson_order_number=1,
                            classroom_id=390,
                            classroom_floor=1,
                            lesson_start_time="09:00:00",
                            lesson_end_time="10:30:00",
                            lesson_type="Практические занятия",
                            classroom_name="Военный учебный центр",
                            classroom_type="Специализированная лаборатория",
                            classroom_building="Главный корпус",
                            discipline_name="Военная подготовка",
                            teachers=[TeacherModel(
                                first_name="Виктор",
                                last_name="Назаров",
                                patronymic="Георгиевич"
                            )],
                            subgroup="",
                        )]
                    ),
                    DayModel(
                        day_of_week=5,
                        name_day_of_week="пятница",
                        date="2025-10-17",
                        lessons=[LessonModel(
                            lesson_order_number=3,
                            classroom_id=410,
                            classroom_floor=3,
                            lesson_start_time="12:50:00",
                            lesson_end_time="14:20:00",
                            lesson_type="Практические занятия",
                            classroom_name="303 к.2",
                            classroom_type="Компьютерный класс",
                            classroom_building="2-ой корпус",
                            discipline_name="Экономическое обоснование проектов",
                            teachers=[TeacherModel(
                                first_name="Олеся",
                                last_name="Чужина",
                                patronymic="Михайловна"
                            )],
                            subgroup="",
                        )]
                    )
                ],
             )
            )

    def test_get_not_found_group(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_not_found_schedule_service.fetch_group_schedule("0", "11.09.2001", "31.10.2025")
        self.assertEqual(e.exception, CodeException('Group not found', 404))

    def test_get_exception_group(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_exception_schedule_service.fetch_group_schedule("0", "11.09.2001", "31.10.2025")
        self.assertEqual(e.exception, CodeException('Error getting group schedule', 503))

    def test_empty_group_schedule(self):
        result = self.corrupted_empty_schedule_service.fetch_group_schedule("123", "123", "123")
        self.assertEqual(result, ResponseGroupScheduleModel(group_name='2023-ФГиИБ-ПИ-1б', schedule=[]))

    def test_get_groups_list(self):
        result = self.schedule_service.fetch_groups_list(group_name="2023-ГФ-АКС-1асп")
        self.assertEqual(result, [GroupsInfoModel(group_name='2023-ГФ-АКС-1асп', id=1)])

    def test_get_exception_groups_list(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_exception_schedule_service.fetch_groups_list(group_name="2023-ГФ-АКС-1асп")
        self.assertEqual(e.exception, CodeException('Error getting group list', 503))

    def test_empty_groups_list(self):
        result = self.corrupted_empty_schedule_service.fetch_groups_list(group_name="2023-ГФ-АКС-1асп")
        self.assertEqual(result, [])

    def test_get_teachers_list(self):
        result = self.schedule_service.fetch_teachers_list(teacher_name="антон")
        self.assertEqual(result, [TeachersInfoModel(id=1, teacher=TeacherModel(first_name='',last_name='',patronymic=''))])

    def test_get_exception_teachers_list(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_exception_schedule_service.fetch_teachers_list(teacher_name="антон")
        self.assertEqual(e.exception, CodeException('Error getting teachers list', 503))

    def test_empty_teachers_list(self):
        result = self.corrupted_empty_schedule_service.fetch_teachers_list(teacher_name="антон")
        self.assertEqual(result, [])

    def test_get_classrooms_list(self):
        result = self.schedule_service.fetch_classrooms_list(classroom="103")
        self.assertEqual(result, [ClassroomsInfoModel(classroom_id=1, classroom_name='')])

    def test_get_exception_classrooms_list(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_exception_schedule_service.fetch_classrooms_list(classroom="103")
        self.assertEqual(e.exception, CodeException('Error getting classrooms list', 503))

    def test_empty_classrooms_list(self):
        result = self.corrupted_empty_schedule_service.fetch_classrooms_list(classroom="103")
        self.assertEqual(result, [])