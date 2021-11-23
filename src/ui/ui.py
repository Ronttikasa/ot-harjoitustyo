from repositories.practice_repository import (
    practice_repository as default_practice_repo
)

class UI:

    def __init__(self, practice_repo = default_practice_repo):
        self._practice_repo = practice_repo

    # tästä pitää säätää vielä
    def use(self):
        print("Welcome to your training journal!")
        while True:
            cmd = input("""
            1: add a new entry
            2: view previous entries
            q: quit
            """)

            if cmd == "1":
                print("Hey great, you got up and did a workout!")
                date = input("Date (ddmmyy): ")
                start = input("Start time (hh:mm): ")
                end = input("End time (hh:mm): ")
                notes = input("Notes / comments: ")

                practice = f"{date};{start};{end};{notes}"
                self._practice_repo.create(practice)

            elif cmd == "2":
                print(self._practice_repo.get_all())

            elif cmd == "q":
                break
            else:
                print("Unknown command")