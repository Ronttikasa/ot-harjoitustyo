import unittest
from datetime import datetime
from entities.practice import Practice


class TestPractice(unittest.TestCase):
    def setUp(self) -> None:
        self.date_a = datetime.strptime("06/12/21", "%d/%m/%y")
        self.start_a = datetime.strptime("16:45", "%H:%M")
        self.end_a = datetime.strptime("18:15", "%H:%M")

        self.date_b = datetime.strptime("22/11/21", "%d/%m/%y")
        self.start_b = datetime.strptime("11:00", "%H:%M")
        self.end_b = datetime.strptime("12:00", "%H:%M")

        self.practice_a = Practice(
            self.date_a, self.start_a, self.end_a, "ritti paranee!"
        )
        self.practice_b = Practice(
            self.date_b, self.start_b, self.end_b
        )

    def test_str(self):
        self.assertEqual(
            str(self.practice_a), "06.12.2021, 16:45 - 18:15. Notes: ritti paranee!"
        )
        self.assertEqual(
            str(self.practice_b), "22.11.2021, 11:00 - 12:00. Notes: "
        )

    def test_length(self):
        self.assertEqual(self.practice_a.length(), 1.5)
        self.assertEqual(self.practice_b.length(), 1.0)
