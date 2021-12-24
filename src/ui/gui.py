from tkinter import Tk
from ui.journal_view import JournalView
from ui.main_view import MainView
from ui.goals_view import GoalsView
from ui.journal_list_view import JournalListView
from ui.stats_view import StatsView


class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._root.minsize(width=500, height=500)

    def start(self):
        self._show_main_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._show_journal_view,
            self._show_goals_view,
            self._show_stats_view
        )

        self._current_view.pack()

    def _show_journal_view(self):
        self._hide_current_view()

        self._current_view = JournalView(
            self._root,
            self._show_main_view,
            self._show_journal_list_view
        )

        self._current_view.pack()

    def _show_journal_list_view(self):
        self._hide_current_view()

        self._current_view = JournalListView(
            self._root,
            self._show_main_view
        )

        self._current_view.pack()

    def _show_goals_view(self):
        self._hide_current_view()

        self._current_view = GoalsView(
            self._root,
            self._show_main_view
        )

        self._current_view.pack()

    def _show_stats_view(self):
        self._hide_current_view()

        self._current_view = StatsView(
            self._root,
            self._show_main_view
        )

        self._current_view.pack()
