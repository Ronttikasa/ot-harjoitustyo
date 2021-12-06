from repositories.goal_repository import (
    goal_repository as default_goal_repo
)
from entities.goal import Goal


class GoalService:
    def __init__(self, goal_repo=default_goal_repo):
        self._goal_repo = goal_repo

    def add_goal(self):
        print("Let's add a new goal!")
        content = input("My goal is: ")

        goal = Goal(content)
        self._goal_repo.create(goal)

    def list_all(self):
        self._goal_repo.list_all_with_number()

    def mark_done(self):
        all_goals = self._goal_repo.list_all()
        self._goal_repo.list_all_with_number()
        done_index = int(input("Which goal was it: ")) - 1
        if done_index not in range(len(all_goals)):
            print("No such goal found")
            return
        done_id = all_goals[done_index].id
        self._goal_repo.mark_done(done_id)
