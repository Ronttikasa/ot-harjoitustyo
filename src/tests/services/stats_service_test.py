import unittest
from datetime import datetime
from services.stats_service import StatsService
from entities.practice import Practice


class FakePracticeRepository:
    def __init__(self):
        self.entries = []

    def list_all(self):
        return self.entries

    def create(self, entry):
        self.entries.append(entry)


class TestStatsService(unittest.TestCase):

    def setUp(self):
        self.practice_repo = FakePracticeRepository()
        self.stats_service = StatsService(self.practice_repo)

        self.date_a = datetime.strptime("06/12/21", "%d/%m/%y")
        self.start_a = datetime.strptime("18:25", "%H:%M")
        self.end_a = datetime.strptime("19:45", "%H:%M")

        self.date_b = datetime.strptime("22/11/21", "%d/%m/%y")
        self.start_b = datetime.strptime("11:00", "%H:%M")
        self.end_b = datetime.strptime("12:00", "%H:%M")

        self.date_c = datetime.strptime("14/12/21", "%d/%m/%y")
        self.start_c = datetime.strptime("12:00", "%H:%M")
        self.end_c = datetime.strptime("14:00", "%H:%M")

        self.practice_a = Practice(
            self.date_a, self.start_a, self.end_a, "???")
        self.practice_b = Practice(self.date_b, self.start_b, self.end_b)
        self.practice_c = Practice(self.date_c, self.start_c, self.end_c)

        self.practice_repo.create(self.practice_a)
        self.practice_repo.create(self.practice_b)
        self.practice_repo.create(self.practice_c)

    def test_correct_average_duration(self):
        self.assertEqual(self.stats_service.average_duration(), 1.44)

    def test_correct_total_hours(self):
        self.assertEqual(self.stats_service.total_hours(), 4)
