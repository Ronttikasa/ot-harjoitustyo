from entities.goal import Goal
from pathlib import Path
from config import GOALS_FILE_PATH

# luokka tallentaa tietoa toistaiseksi kovakoodattuun tiedostoon training-goals.txt,
# tämä on tarkoitus muuttaa myöhemmin


class GoalRepository:
    """The class responsible for the database operations of goals.
    """

    def __init__(self, file_path):
        self._file_path = file_path

    def create(self, entry: Goal):
        """Adds a new goal in the database.

        Args:
            entry (Goal): The goal to be added to the database.
        """

        self._write([entry])

    def list_all(self):
        """Returns all the goals.

        Returns:
            A list of Goal objects.
        """
        return self._read()

    def list_all_with_number(self):
        """Prints out all the goals with an identifying number.
        """

        for index, entry in enumerate(self.list_all()):
            print(f"{index+1} {entry}")

    def mark_done(self, goal_id):
        """Sets the goal as reached.

        Args:
            goal_id: The id of the goal that was reached
        """

        all_goals = self._read()
        updated_goals = []
        for goal in all_goals:
            if goal.id == goal_id:
                goal.mark_done()
            updated_goals.append(goal)
        self._delete_all()
        self._write(updated_goals)

    def _check_file_exists(self):
        Path(self._file_path).touch()

    def _delete_all(self):
        """Deletes all goals.
        """
        self._check_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            file.write("")

    def _write(self, goals: list):
        self._check_file_exists()

        with open(self._file_path, "a", encoding="utf-8") as file:
            for goal in goals:
                row = f"{goal.id};{goal.content};{goal.reached}"
                file.write(f"{row}\n")

    def _read(self):
        self._check_file_exists()
        
        goals = []
        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.strip()
                if row == "":
                    continue
                parts = row.split(";")
                goal_id = parts[0]
                cont = parts[1]
                reached = (parts[2] == "True")

                goal = Goal(cont, reached, goal_id)
                goals.append(goal)

        return goals


goal_repository = GoalRepository(GOALS_FILE_PATH)
