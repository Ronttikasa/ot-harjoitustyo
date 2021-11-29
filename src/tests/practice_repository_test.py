import unittest
from repositories.practice_repository import practice_repository


class TestPracticeRepository(unittest.TestCase):
    def setUp(self):
        practice_repository.delete_all()

        self.practice = "221121;11:00;12:00;toeloops"

    def test_create(self):
        practice_repository.create(self.practice)
        practices = practice_repository.get_all()

        self.assertEqual(len(practices), 1)
        self.assertEqual(practices[0], "221121, from 11:00 to 12:00, toeloops")
