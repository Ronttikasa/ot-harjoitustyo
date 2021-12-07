from entities.goal import Goal
import unittest


class TestGoal(unittest.TestCase):
    def setUp(self):
        self.goal_a = Goal("loop in 2021")
        self.goal_b = Goal("scratch spin in 2021", True, "123456")
        self.goal_c = Goal("flip in 2021", goal_id="987654")

    def test_str(self):
        self.assertEqual(str(self.goal_a), "[ ] loop in 2021")
        self.assertEqual(str(self.goal_b), "[x] scratch spin in 2021")

# todo: muuta goal reached -tilaa luokan metodilla
