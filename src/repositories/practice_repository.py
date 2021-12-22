import datetime
from pathlib import Path
from entities.practice import Practice
from config import JOURNAL_FILE_PATH


class PracticeRepository:
    """The class responsible for the database operations of practice journal entries.
    """

    def __init__(self, file_path):
        self._file_path = file_path

    def create(self, entry: Practice):
        """Adds a new practice entry to the database.

        Args:
            entry (Practice): The entry to be added to the database.
        """

        self._write([entry])

    def list_all(self):
        """Returns all the practice journal entries.

        Returns:
            A list of Practice objects.
        """

        return self._read()

    def delete_all(self):
        """Deletes all the entries in the database.
        """
        self._check_file_exists()
        with open(self._file_path, "w", encoding="utf-8") as file:
            file.write("")

    def delete_entry(self, tbd_id):
        """Deletes a practice journal entry.

        Args:
            tbd_id: Id of the entry to be deleted
        """
        entries = self._read()
        entries = [entry for entry in entries if entry.id != tbd_id]
        self.delete_all()
        self._write(entries)

    def _check_file_exists(self):
        Path(self._file_path).touch()

    def _write(self, entries: list):
        self._check_file_exists()

        with open(self._file_path, "a", encoding="utf-8") as file:
            for entry in entries:
                row = (
                    f"{entry.id};{entry.date.strftime('%m/%d/%y')};"\
                    f"{entry.start.strftime('%H:%M')};"\
                    f"{entry.end.strftime('%H:%M')};{entry.notes}"
                )
                file.write(f"{row}\n")

    def _read(self):
        self._check_file_exists()

        entries = []
        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                if row == "":
                    continue
                parts = row.split(";")

                prac_id = parts[0]
                entry_date = datetime.datetime.strptime(
                    parts[1], "%m/%d/%y").date()
                start = datetime.datetime.strptime(parts[2], "%H:%M").time()
                end = datetime.datetime.strptime(parts[3], "%H:%M").time()
                notes = parts[4]

                entries.append(
                    Practice(entry_date, start, end, notes, prac_id))

        return entries


practice_repository = PracticeRepository(JOURNAL_FILE_PATH)
