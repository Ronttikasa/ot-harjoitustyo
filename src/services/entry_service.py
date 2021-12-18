import datetime
import re
from repositories.practice_repository import (
    practice_repository as default_practice_repo
)
from entities.practice import Practice


class EntryService:
    def __init__(self, practice_repo=default_practice_repo):
        self._practice_repo = practice_repo

    # def add_entry(self):
    #     print("Hey great, you got up and did a workout!")
    #     date = input("Date (ddmmyy): ")
    #     start = input("Start time (hh:mm): ")
    #     end = input("End time (hh:mm): ")
    #     notes = input("Notes / comments: ")

    #     practice = Practice(date, start, end, notes)
    #     self._practice_repo.create(practice)

    def add_entry_gui(self, date, start, end, notes):
        try:
            if re.search("[0-9]|[0-1][0-9]|2[0-3]", start):
                if len(start) == 2:
                    start += ":00"
                elif len(start) == 1:
                    start = "0"+start+":00"
            if re.search("[0-9]|[0-1][0-9]|2[0-3]", end):
                if len(end) == 2:
                    end += ":00"
                elif len(end) == 1:
                    end = "0"+end+":00"
            
            start = datetime.datetime.strptime(start,"%H:%M").time()
            end = datetime.datetime.strptime(end,"%H:%M").time()
            practice = Practice(date, start, end, notes)
            self._practice_repo.create(practice)
        except:
            # todo
            pass
    

    # def list_all(self):
    #     self._practice_repo.list_all_with_number()

    def delete_entry(self):
        entries = self._practice_repo.list_all()
        self._practice_repo.list_all_with_number()
        delete_index = int(input("Entry number to delete: ")) - 1
        delete_id = entries[delete_index].id
        self._practice_repo.delete_entry(delete_id)

entry_service = EntryService()