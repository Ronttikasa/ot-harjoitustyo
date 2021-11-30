from repositories.practice_repository import (
    practice_repository as default_practice_repo
)
from entities.practice import Practice


class EntryService:
    def __init__(self, practice_repo=default_practice_repo):
        self._practice_repo = practice_repo

    def add_entry(self):
        print("Hey great, you got up and did a workout!")
        date = input("Date (ddmmyy): ")
        start = input("Start time (hh:mm): ")
        end = input("End time (hh:mm): ")
        notes = input("Notes / comments: ")

        practice = Practice(date, start, end, notes)
        self._practice_repo.create(practice)

    def list_all(self):
        self._practice_repo.list_all_with_number()

    def delete_entry(self):
        entries = self._practice_repo.list_all()
        self._practice_repo.list_all_with_number()
        delete_index = int(input("Entry number to delete: ")) - 1
        delete_id = entries[delete_index].id
        self._practice_repo.delete_entry(delete_id)
