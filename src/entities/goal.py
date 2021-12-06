import uuid


class Goal:
    def __init__(self, content: str, reached: bool = False, goal_id=None):
        self.content = content
        self.reached = reached
        self.id = goal_id or str(uuid.uuid4())

    def __str__(self):
        if self.reached:
            return f"[x] {self.content}"
        return f"[ ] {self.content}"
