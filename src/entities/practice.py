import uuid
from datetime import datetime


class Practice:
    """A class that depicts a practice journal entry.

    Attributes:
        date (str): Date of the practice
        start (str): Start time
        end (str): End time
        notes (str): Notes about the practice session
        entry_id (str): Entry id
    """

    def __init__(self, date, start, end, notes="", entry_id=None):
        """Class constructor, creates a new practice.

        Args:
            date: Practice date
            start: Start time (hh:mm)
            end: End time (hh:mm)
            notes (str, optional): Notes about the practice session. Defaults to "".
            entry_id (str, optional): Entry id. Defaults to a generated uuid.
        """
        self.date = date
        self.start = start
        self.end = end
        self.notes = notes
        self.id = entry_id or str(uuid.uuid4())

    def __str__(self):
        return f"{self.date.strftime('%d.%m.%Y')}, {self.start.strftime('%H:%M')} - {self.end.strftime('%H:%M')}. Notes: {self.notes}"

    def length(self):
        """Duration of a practice session

        Returns:
            float: Practice duration in hours
        """

        tdelta = self.end - self.start
        return tdelta.seconds / 3600
