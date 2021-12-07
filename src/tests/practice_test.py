import unittest
from entities.practice import Practice


class TestPractice(unittest.TestCase):
    def setUp(self) -> None:
        self.practice_a = Practice(
            "061221", "16:45", "18:15", "ritti paranee!")
        self.practice_b = Practice("221121", "11:00", "12:00")

    def test_str(self):
        self.assertEqual(
            str(self.practice_a), "061221, from 16:45 to 18:15. Notes: ritti paranee!"
        )
        self.assertEqual(
            str(self.practice_b), "221121, from 11:00 to 12:00. Notes: "
        )
