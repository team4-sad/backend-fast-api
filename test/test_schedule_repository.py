import unittest

from src.config.config import Config
from src.exceptions.invalid_classroom_exception import InvalidClassroomException
from src.exceptions.invalid_group_exception import InvalidGroupException
from src.exceptions.invalid_teacher_exception import InvalidTeacherException
from src.models.origin_response_group_schedule_model import OriginResponseGroupScheduleModel
from src.models.origin_schedule_model import OriginScheduleModel
from src.repositories.schedule_repository import ScheduleRepository


class ScheduleRepositoryTest(unittest.TestCase):
    def setUp(self):
        config = Config(path_env="../.env")
        self.schedule_repository = ScheduleRepository(base_url=config.base_schedule_api_url)

    def test_get_different_schedules(self):
        schedule1 = self.schedule_repository.fetch_group(group_id="1274", date_start="2025-10-13", date_end="2025-10-19")
        schedule2 = self.schedule_repository.fetch_group(group_id="1286", date_start="2025-10-13", date_end="2025-10-19")
        self.assertNotEqual(schedule1,schedule2)

    def test_get_incorrect_group_schedule(self):
        with self.assertRaises(InvalidGroupException) as e:
            self.schedule_repository.fetch_group(group_id="121", date_start="2025-10-13", date_end="2025-10-19")
        self.assertEqual("121", e.exception.group_id)

    def test_get_empty_group_schedule(self):
        result = self.schedule_repository.fetch_group(group_id="832", date_start="2025-10-13", date_end="2025-10-19")
        self.assertEqual(result, OriginResponseGroupScheduleModel(group_name="2021-ГФ-ГиДЗакс-1б", schedule=OriginScheduleModel()))

    def test_get_groups(self):
        result = self.schedule_repository.fetch_groups(group_name="")
        self.assertNotEqual(result, [])

    def test_get_empty_groups(self):
        result = self.schedule_repository.fetch_groups(group_name="Владимир Путин молодец! Политик лидер и боец!(qwzesxrdtcfvygubnimo)")
        self.assertEqual(result, [])

    def test_get_teachers(self):
        result = self.schedule_repository.fetch_teachers(teacher_name="")
        self.assertNotEqual(result, [])

    def test_get_empty_teachers(self):
        result = self.schedule_repository.fetch_groups(group_name="Наш президент страну поднял! Россию Путин не предал!(zesrxdtcfy guhijokpl)")
        self.assertEqual(result, [])

    def test_get_classrooms(self):
        result = self.schedule_repository.fetch_classrooms(classroom="")
        self.assertNotEqual(result, [])

    def test_get_empty_classrooms(self):
        result = self.schedule_repository.fetch_groups(group_name="В новый век вошла Россия! И вздохнула с новой силой!(ezsxrdctfvygbuhino,p)")
        self.assertEqual(result, [])

    def test_get_teacher_schedule(self):
        result = self.schedule_repository.fetch_teacher(teacher_id="1",date_start="2025-10-27",date_end="2025-11-02")
        self.assertNotEqual(result, [])

    def test_get_invalid_teacher_schedule(self):
        with self.assertRaises(InvalidTeacherException) as e:
            self.schedule_repository.fetch_teacher(teacher_id="-1",date_start="2025-10-27",date_end="2025-11-02")
        self.assertEqual("-1", e.exception.teacher_id)

    def test_get_classroom_schedule(self):
        result = self.schedule_repository.fetch_classroom(classroom_id="422",date_start="2025-10-27",date_end="2025-11-02")
        self.assertNotEqual(result, [])

    def test_get_invalid_classroom_schedule(self):
        with self.assertRaises(InvalidClassroomException) as e:
            self.schedule_repository.fetch_classroom(classroom_id="-1",date_start="2025-10-27",date_end="2025-11-02")
        self.assertEqual("-1", e.exception.classroom_id)