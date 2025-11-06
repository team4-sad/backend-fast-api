import unittest

from src.config.config import Config
from src.exceptions.invalid_group_exception import InvalidGroupException
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
