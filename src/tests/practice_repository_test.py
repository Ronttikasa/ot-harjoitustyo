import unittest
from repositories.practice_repository import practice_repository
from entities.practice import Practice


class TestPracticeRepository(unittest.TestCase):
    def setUp(self):
        practice_repository.delete_all()

        self.entry_a = Practice("221121", "11:00", "12:00", "toeloops")
        self.entry_b = Practice("291121", "12:00", "13:00", "flips")
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




