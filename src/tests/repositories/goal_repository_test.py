import unittest
from repositories.goal_repository import goal_repository
from entities.goal import Goal


class TestGoalRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = goal_repository
        self.repo.delete_all()

        self.goal_a = Goal("loop by end of 2021")
        self.goal_b = Goal("sit spin", True, "123456")
        self.goal_c = Goal("flip by end of 2021")

    def test_create(self):
        self.repo.create(self.goal_a)
        goals = self.repo.list_all()

        self.assertEqual(len(goals), 1)
        self.assertEqual(goals[0].content, self.goal_a.content)
        self.assertEqual(goals[0].status, False)
        self.assertEqual(goals[0].id, self.goal_a.id)

    def test_create_optionals(self):
        self.repo.create(self.goal_b)
        goals = self.repo.list_all()

        self.assertEqual(goals[0].content, self.goal_b.content)
        self.assertEqual(goals[0].status, True)
        self.assertEqual(goals[0].id, "123456")

    def test_list_all(self):
        self.repo.create(self.goal_a)
        self.repo.create(self.goal_b)
        goals = self.repo.list_all()

        self.assertEqual(len(goals), 2)
        self.assertEqual(goals[0].id, self.goal_a.id)
        self.assertEqual(goals[1].id, self.goal_b.id)

    def test_delete_all(self):
        self.repo.create(self.goal_a)
        self.repo.create(self.goal_b)
        self.repo.delete_all()
        goals = self.repo.list_all()

        self.assertEqual(len(goals), 0)

    def test_mark_done(self):
        self.repo.create(self.goal_a)
        self.repo.create(self.goal_c)
        self.repo.mark_done(self.goal_a.id)
        goals = self.repo.list_all()

        self.assertEqual(goals[0].status, True)
        self.assertEqual(goals[1].status, False)
