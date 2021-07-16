import unittest
from Timify import TimeConverter


class Test(unittest.TestCase):

    def test_to_seconds(self):
        result = TimeConverter(seconds=10, minutes=1, hours=1).to_seconds()
        self.assertEqual(result, 3670.0)

    def test_to_milliseconds(self):
        result = TimeConverter(seconds=10).to_milliseconds()
        self.assertEqual(result, 10000.0)

    def test_to_minutes(self):
        result = TimeConverter(seconds=90, minutes=14, hours=3, days=23).to_minutes()
        self.assertEqual(result, 33315.5)

    def test_to_hours(self):
        result = TimeConverter(seconds=90, minutes=14, hours=3, days=2).to_hours()
        self.assertEqual(result, 51.25833333333333)

    def test_to_days(self):
        result = TimeConverter(seconds=90, minutes=14, hours=3, days=2, months=1, years=1).to_days()
        self.assertEqual(result, 397.59872685185184)

    def test_to_months(self):
        result = TimeConverter(seconds=90, minutes=14, hours=3, days=2, months=1, years=2).to_months()
        self.assertEqual(result, 25.421500771604936)

    def test_to_years(self):
        result = TimeConverter(months=50, years=2).to_years()
        self.assertEqual(result, 6.252572016460906)
