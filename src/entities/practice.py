import uuid


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
            date (str): Practice date (ddmmyy)
            start (str): Start time (hh:mm)
            end (str): End time (hh:mm)
            notes (str, optional): Notes about the practice session. Defaults to "".
            entry_id (str, optional): Entry id. Defaults to a generated uuid.
        """
        self.date = date
        self.start = start
        self.end = end
        self.notes = notes
        self.id = entry_id or str(uuid.uuid4())

    def __str__(self):
        return f"{self.date}, from {self.start} to {self.end}. Notes: {self.notes}"
