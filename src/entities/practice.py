import uuid


class Practice:
    def __init__(self, date, start, end, notes=None, review=None, entry_id=None):
        self.date = date
        self.start = start
        self. end = end
        self.notes = notes
        self.review = review
        self.id = entry_id or str(uuid.uuid4())

    def __str__(self):
        return f"{self.date}, from {self.start} to {self.end}. Notes: {self.notes}"
