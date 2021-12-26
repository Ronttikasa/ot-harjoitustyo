import unittest
from datetime import datetime
from services.entry_service import EntryService, InvalidTimeEntryError


class FakePracticeRepository:
    def __init__(self):
        self.entries = []

    def list_all(self):
        return self.entries

    def create(self, entry):
        self.entries.append(entry)

    def delete_all(self):
        self.entries = []

    def delete_entry(self, tbd_id):
        self.entries = [
            entry for entry in self.entries if not entry.id == tbd_id]


class TestEntryService(unittest.TestCase):
    def setUp(self):
        self.practice_repo = FakePracticeRepository()
        self.entry_service = EntryService(self.practice_repo)

        self.date_a = datetime.strptime("11/12/21", "%d/%m/%y")
        self.start_a = "11:00"
        self.end_a = "12:15"
        self.notes_a = "ritti ja piruetteja"

        self.date_b = datetime.strptime("23/12/21", "%d/%m/%y")
        self.start_b = "13"
        self.end_b = "14"
        self.notes_b = ""

    def test_adding_entry(self):
        self.entry_service.add_entry_gui(
            self.date_a, self.start_a, self.end_a, self.notes_a
        )
        entries = self.entry_service.list_all()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].date, self.date_a)

    def test_adding_without_minutes(self):
        self.entry_service.add_entry_gui(
            self.date_b, self.start_b, self.end_b, self.notes_b
        )
        entries = self.entry_service.list_all()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].start, datetime.strptime("13:00", "%H:%M"))

    def test_adding_invalid_time(self):
        self.assertRaises(
            InvalidTimeEntryError,
            lambda: self.entry_service.add_entry_gui(
                self.date_a, "invalid", "1000", "some notes"
            )
        )

    def test_delete_entry(self):
        self.entry_service.add_entry_gui(
            self.date_a, self.start_a, self.end_a, self.notes_a
        )
        self.entry_service.add_entry_gui(
            self.date_b, self.start_b, self.end_b, self.notes_b
        )
        entries = self.entry_service.list_all()
        self.entry_service.delete_entry(entries[0].id)
        entries = self.entry_service.list_all()

        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].date, self.date_b)
