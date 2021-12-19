from repositories.goal_repository import (
    goal_repository as default_goal_repo
)
from entities.goal import Goal


class GoalService:
    """The class responsible for the application logic.
    """

    def __init__(self, goal_repo=default_goal_repo):
        self._goal_repo = goal_repo

    def add_goal(self, content):
        """Creates a new goal.
        """

        goal = Goal(content)
        self._goal_repo.create(goal)

    def list_all(self):
        """Lists all the goals.
        """
        # self._goal_repo.list_all_with_number()
        return self._goal_repo.list_all()

    def list_all_unreached(self):
        goals = self._goal_repo.list_all()
        return [goal for goal in goals if not goal.reached]

    # tästä puolet käyttöliittymään?
    # def mark_done(self):
    #     """Sets a goal status to reached.
    #     """

    #     all_goals = self._goal_repo.list_all()
    #     self._goal_repo.list_all_with_number()
    #     done_index = int(input("Which goal was it: ")) - 1
    #     if done_index not in range(len(all_goals)):
    #         print("No such goal found, try again!")
    #         return
    #     done_id = all_goals[done_index].id
    #     self._goal_repo.mark_done(done_id)

    def mark_done(self, goal_id):
        return self._goal_repo.mark_done(goal_id)


goal_service = GoalService()
