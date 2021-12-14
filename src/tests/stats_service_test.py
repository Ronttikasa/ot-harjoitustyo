import unittest
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

        self.practice_a = Practice("131221", "11:00", "12:00", "???")
        self.practice_b = Practice("141221", "10:00", "12:00")
        self.practice_c = Practice("111221", "18:25", "19:45")

        self.practice_repo.create(self.practice_a)
        self.practice_repo.create(self.practice_b)
        self.practice_repo.create(self.practice_c)

    def test_correct_average_duration(self):
        self.assertEqual(self.stats_service.average_duration(), 1.44)

    def test_correct_total_hours(self):
        self.assertEqual(self.stats_service.total_hours(), 4.33)

