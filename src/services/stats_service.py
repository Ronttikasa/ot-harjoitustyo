from repositories.practice_repository import (
    PracticeRepository,
    practice_repository as default_repo
)
from entities.practice import Practice
from statistics import mean

class StatsService:
    """Class responsible for the statistics
    """

    def __init__(self, practice_repo=default_repo):
        self._practice_repo = practice_repo
        # self._practice_repo = PracticeRepository

    def average_duration(self):
        """Average practice duration

        Returns:
            float: average duration in hours
        """
        sessions = self._practice_repo.list_all()
        durations = []
        for session in sessions:
            durations.append(session.length())
        return round(mean(durations), 2)

    def total_hours(self):
        """Total time spent practicing

        Returns:
            float: total hours
        """

        all_hours = 0
        for session in self._practice_repo.list_all():
            all_hours += session.length()
        return round(all_hours, 2)