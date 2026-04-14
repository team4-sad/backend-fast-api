import datetime
import unittest
from src.utils import datetime_utils


class TestLessonsStorage(unittest.TestCase):
    def test_get_monday_datetime(self):
       dt = datetime.datetime(2026, 4, 14, 23, 50, 48)
       dt_monday = datetime_utils.get_monday_datetime(dt)
       self.assertEqual(dt_monday, datetime.date(2026, 4, 13))

    def test_get_sunday_datetime(self):
       dt = datetime.datetime(2026, 4, 14, 23, 50, 48)
       dt_monday = datetime_utils.get_sunday_datetime(dt)
       self.assertEqual(dt_monday, datetime.date(2026, 4, 19))

    def test_true_is_prime_week(self):
       dt = datetime.datetime(2026, 4, 14, 23, 50, 48)
       is_prime_week = datetime_utils.is_prime_week(dt)
       self.assertTrue(is_prime_week)

    def test_last_day_prime_week_is_prime(self):
       dt = datetime.datetime(2026, 4, 19, 23, 50, 48)
       is_prime_week = datetime_utils.is_prime_week(dt)
       self.assertTrue(is_prime_week)

    def test_false_is_prime_week(self):
       dt = datetime.datetime(2026, 4, 20, 23, 50, 48)
       is_prime_week = datetime_utils.is_prime_week(dt)
       self.assertFalse(is_prime_week)

    def test_last_day_not_prime_week_is_not_prime(self):
       dt = datetime.datetime(2026, 4, 26, 23, 50, 48)
       is_prime_week = datetime_utils.is_prime_week(dt)
       self.assertFalse(is_prime_week)

    def test_date2str(self):
       dt = datetime.datetime(2026, 4, 26, 23, 50, 48)
       str_dt = datetime_utils.date2str(dt)
       self.assertEqual(str_dt, "2026-04-26")

