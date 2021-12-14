from services.entry_service import EntryService
from services.goal_service import GoalService
from services.stats_service import StatsService


class UI:

    def __init__(self):
        self._entry_service = EntryService()
        self._goal_service = GoalService()
        self._stats_service = StatsService()

    def use(self):
        print("Welcome to your training journal!")
        while True:
            cmd = input("""
            1: journal
            2: goals
            3: training stats
            q: quit
            """)

            if cmd == "1":
                self.journal_ui()
            elif cmd == "2":
                self.goals_ui()
            elif cmd == "3":
                self.stats_ui()
            elif cmd == "q":
                break
            else:
                print("Unknown command")

    def journal_ui(self):
        while True:
            cmd = input("""
            1: add a new entry
            2: view previous entries
            3: delete entry
            q: main menu
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

    def goals_ui(self):
        while True:
            cmd = input("""
            1: add a new skating goal
            2: view goals
            3: mark a goal reached
            q: main menu
            """)
            if cmd == "1":
                self._goal_service.add_goal()
            elif cmd == "2":
                self._goal_service.list_all()
            elif cmd == "3":
                print("Awesome, you reached a goal!")
                self._goal_service.mark_done()
            elif cmd == "q":
                break
            else:
                print("Unknown command")

    def stats_ui(self):
        while True:
            print("Statistics")
            print(f"Average training session: {self._stats_service.average_duration()} hours")
            print(f"{self._stats_service.total_hours()} hours in total")
            break
