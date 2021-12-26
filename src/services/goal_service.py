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

        Returns:
            List of Goal objects.
        """

        return self._goal_repo.list_all()

    def list_all_unreached(self):
        """Lists all goals that are not reached.

        Returns:
            List of Goal objects.
        """

        goals = self._goal_repo.list_all()
        return [goal for goal in goals if not goal.status]

    def mark_done(self, goal_id):
        """Sets the status of a specified goal to reached.

        Args:
            goal_id (str): Id of the goal.
        """

        self._goal_repo.mark_done(goal_id)


goal_service = GoalService()
