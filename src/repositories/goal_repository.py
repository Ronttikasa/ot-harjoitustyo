from entities.goal import Goal


class GoalRepository:

    def __init__(self):
        pass

    def create(self, entry: Goal):
        self._write([entry])

    def list_all(self):
        return self._read()

    def list_all_with_number(self):
        for index, entry in enumerate(self.list_all()):
            print(f"{index+1} {entry}")

    def mark_done(self, goal_id):
        all_goals = self._read()
        updated_goals = []
        for goal in all_goals:
            if goal.id == goal_id:
                goal.reached = True
            updated_goals.append(goal)
        self.delete_all()
        self._write(updated_goals)

    def delete_all(self):
        with open("training-goals.txt", "w", encoding="utf-8") as file:
            file.write("")

    def _write(self, goals: list):
        with open("training-goals.txt", "a", encoding="utf-8") as file:
            for goal in goals:
                row = f"{goal.id};{goal.content};{goal.reached}"
                file.write(f"{row}\n")

    def _read(self):
        goals = []
        with open("training-goals.txt", encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                if row == "":
                    continue
                parts = row.split(";")
                goal_id = parts[0]
                cont = parts[1]
                reached = (parts[2] == "True")

                goal = Goal(cont, reached, goal_id)
                goals.append(goal)

        return goals


goal_repository = GoalRepository()
