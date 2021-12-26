import datetime
import re
from repositories.practice_repository import (
    practice_repository as default_practice_repo
)
from entities.practice import Practice


class InvalidTimeEntryError(Exception):
    pass


class EntryService:
    def __init__(self, practice_repo=default_practice_repo):
        self._practice_repo = practice_repo

    def _validate_time(self, time_input):
        if re.search("^[0-1][0-9]$|^2[0-4]$", time_input):
            return True
        if re.search("^[0-1][0-9]:[0-5][0-9]$|^2[0-4]:[0-5][0-9]$", time_input):
            return True
        return False

    def add_entry(self, entry_date, start, end, notes):
        """Add the journal entry to the database.

        Args:
            entry_date (str): date
            start (str): start time (hh:mm or hh)
            end (str): end time (hh:mm or hh)
            notes (str): notes/comments

        Raises:
            InvalidTimeEntryError: Start/end times are not entered in hh:mm or hh format.
        """

        if self._validate_time(start) and self._validate_time(end):
            if re.search("^[0-1][0-9]$|^2[0-3]$", start):
                start += ":00"
            if re.search("^[0-1][0-9]$|^2[0-3]$", end):
                end += ":00"
            start = datetime.datetime.strptime(start, "%H:%M")
            end = datetime.datetime.strptime(end, "%H:%M")
            practice = Practice(entry_date, start, end, notes)
            self._practice_repo.create(practice)
        else:
            raise InvalidTimeEntryError(
                "Times should be entered in hh:mm format")

    def list_all(self):
        """List all the practice sessions recorded in the journal.

        Returns:
            List of Practice objects.
        """

        return self._practice_repo.list_all()

    def delete_entry(self, entry_id):
        """Deletes a specified entry.

        Args:
            entry_id (str): Id of the entry to be deleted.
        """

        self._practice_repo.delete_entry(entry_id)


entry_service = EntryService()
