import unittest
from datetime import datetime
from repositories.practice_repository import practice_repository
from entities.practice import Practice


class TestPracticeRepository(unittest.TestCase):
    def setUp(self):
        practice_repository.delete_all()

        self.date_a = datetime.strptime("06/12/21", "%d/%m/%y")
        self.start_a = datetime.strptime("16:45", "%H:%M")
        self.end_a = datetime.strptime("18:15", "%H:%M")

        self.date_b = datetime.strptime("22/11/21", "%d/%m/%y")
        self.start_b = datetime.strptime("11:00", "%H:%M")
        self.end_b = datetime.strptime("12:00", "%H:%M")

        self.entry_a = Practice(
            self.date_a, self.start_a, self.end_a, "toeloops")
        self.entry_b = Practice(self.date_b, self.start_b, self.end_b, "flips")
        self.entries = [self.entry_a, self.entry_b]

    def test_create(self):
        practice_repository.create(self.entry_a)
        practices = practice_repository.list_all()

        self.assertEqual(len(practices), 1)
        self.assertEqual(practices[0].date, self.entry_a.date)
        self.assertEqual(practices[0].start, self.entry_a.start)
        self.assertEqual(practices[0].end, self.entry_a.end)
        self.assertEqual(practices[0].notes, self.entry_a.notes)

    def test_list_all(self):
        practice_repository.create(self.entry_a)
        practice_repository.create(self.entry_b)
        practices = practice_repository.list_all()

        self.assertEqual(len(practices), 2)
        self.assertEqual(practices[0].date, self.entry_a.date)
        self.assertEqual(practices[1].date, self.entry_b.date)

    def test_delete_all(self):
        practice_repository.create(self.entry_a)
        practice_repository.create(self.entry_b)
        practice_repository.delete_all()
        practices = practice_repository.list_all()

        self.assertEqual(len(practices), 0)

    def test_delete_entry(self):
        practice_repository.create(self.entry_a)
        practice_repository.create(self.entry_b)
        practice_repository.delete_entry(self.entry_a.id)
        practices = practice_repository.list_all()

        self.assertEqual(len(practices), 1)
        self.assertEqual(practices[0].date, self.entry_b.date)
