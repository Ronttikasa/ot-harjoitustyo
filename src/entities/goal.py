import uuid


class Goal:
    """A class that depicts a goal.

    Attributes:
        content (str): Description of the goal.
        reached (bool): A boolean value showing if the goal is reached.
        goal_id (str): Goal id.
    """

    def __init__(self, content: str, reached: bool = False, goal_id=None):
        """Class constructor, creates a new goal.

        Args:
            content (str): Description of the goal.
            reached (bool, optional): The completion status of the goal. Defaults to False.
            goal_id (str, optional): The id of the goal. Defaults to a generated uuid.
        """

        self.content = content
        self.reached = reached
        self.id = goal_id or str(uuid.uuid4())

    def __str__(self):
        if self.reached:
            return f"[x] {self.content}"
        return f"[ ] {self.content}"

    def mark_done(self):
        """Sets the goal status to reached.
        """

        self.reached = True
