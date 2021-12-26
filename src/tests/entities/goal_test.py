from entities.goal import Goal
import unittest


class TestGoal(unittest.TestCase):
    def setUp(self):
        self.goal_a = Goal("loop in 2021")
        self.goal_b = Goal("scratch spin in 2021", True, "123456")
        self.goal_c = Goal("flip in 2021", goal_id="987654")

    def test_mark_done(self):
        self.goal_a.mark_done()
        self.assertEqual(self.goal_a.status, True)

    def test_new_goal_status(self):
        self.assertEqual(self.goal_a.status, False)
        self.assertEqual(self.goal_b.status, True)
