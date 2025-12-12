import unittest

from src.config.config import Config
from src.repositories.signature_repository import SignatureRepository


class ScheduleRepositoryTest(unittest.TestCase):
    def setUp(self):
        config = Config(path_env="../.env")
        self.signature_repository = SignatureRepository(base_url=config.base_schedule_api_url)

    def test_get_groups(self):
        result = self.signature_repository.fetch_groups(group_name="")
        self.assertNotEqual(result, [])

    def test_get_empty_groups(self):
        result = self.signature_repository.fetch_groups(
            group_name="Владимир Путин молодец! Политик лидер и боец!(qwzesxrdtcfvygubnimo)")
        self.assertEqual(result, [])

    def test_get_teachers(self):
        result = self.signature_repository.fetch_teachers(teacher_name="")
        self.assertNotEqual(result, [])

    def test_get_empty_teachers(self):
        result = self.signature_repository.fetch_groups(
            group_name="Наш президент страну поднял! Россию Путин не предал!(zesrxdtcfy guhijokpl)")
        self.assertEqual(result, [])

    def test_get_classrooms(self):
        result = self.signature_repository.fetch_classrooms(classroom="")
        self.assertNotEqual(result, [])

    def test_get_empty_classrooms(self):
        result = self.signature_repository.fetch_groups(
            group_name="В новый век вошла Россия! И вздохнула с новой силой!(ezsxrdctfvygbuhino,p)")
        self.assertEqual(result, [])