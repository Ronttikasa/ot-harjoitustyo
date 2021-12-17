from tkinter import Tk

from ui.main_view import MainView
from ui.goals_view import GoalsView

class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

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
        pass

    def _show_goals_view(self):
        self._hide_current_view()

        self._current_view = GoalsView(
            self._root,
            self._show_main_view
        )

        self._current_view.pack()

    def _show_stats_view(self):
        pass
        


window = Tk()
window.title("Training journal")

gui = GUI(window)
gui.start()

window.mainloop()