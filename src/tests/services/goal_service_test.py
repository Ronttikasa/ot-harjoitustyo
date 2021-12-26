import unittest
from services.goal_service import GoalService


class FakeGoalRepository:
    def __init__(self):
        self.goals = []

    def create(self, goal):
        self.goals.append(goal)

    def list_all(self):
        return self.goals

    def mark_done(self, goal_id):
        for goal in self.goals:
            if goal.id == goal_id:
                goal.mark_done()

    def delete_all(self):
        self.goals = []


class TestGoalService(unittest.TestCase):
    def setUp(self):
        self.goal_repo = FakeGoalRepository()
        self.goal_service = GoalService(self.goal_repo)

        self.goal_service.add_goal("loop in 2021")
        self.goal_service.add_goal("flip in 2021")

        self.entries = self.goal_service.list_all()

    def test_add_goal(self):
        self.assertEqual(len(self.entries), 2)
        self.assertEqual(self.entries[0].content, "loop in 2021")
        self.assertEqual(self.entries[0].status, False)

    def test_mark_done(self):
        self.goal_service.mark_done(self.entries[0].id)
        self.entries = self.goal_service.list_all()

        self.assertEqual(len(self.entries), 2)
        self.assertEqual(self.entries[0].status, True)

    def test_list_unreached(self):
        self.goal_service.mark_done(self.entries[0].id)
        unreached = self.goal_service.list_all_unreached()

        self.assertEqual(len(unreached), 1)
        self.assertEqual(unreached[0].content, "flip in 2021")
