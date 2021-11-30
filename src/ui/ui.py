from services.entry_service import EntryService

class UI:

    def __init__(self):
        self._entry_service = EntryService()

    def use(self):
        print("Welcome to your training journal!")
        while True:
            cmd = input("""
            1: add a new entry
            2: view previous entries
            3: delete entry
            q: quit
            """)

            if cmd == "1":
                self._entry_service.add_entry()
            elif cmd == "2":
                self._entry_service.list_all()
            elif cmd == "3":
                self._entry_service.delete_entry()
            elif cmd == "q":
                break
            else:
                print("Unknown command")
