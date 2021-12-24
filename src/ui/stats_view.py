from os import stat
from tkinter import ttk, constants
from services.stats_service import stats_service


class StatsView:
    def __init__(self, root, handle_main):
        self._root = root
        self._handle_main = handle_main
        self._stats_service = stats_service

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        header_label = ttk.Label(
            master=self._frame,
            text="Training stats",
            font=20
        )

        header_back_button = ttk.Button(
            master=self._frame,
            text="Main menu ->",
            command=self._handle_main
        )

        header_label.grid(
            row=0, column=0, padx=5, pady=10
        )

        header_back_button.grid(
            row=0, column=1, padx=5, pady=10,
            sticky=constants.EW
        )

    def _initialize_body(self):
        total_label = ttk.Label(
            master=self._frame,
            text=f"Total hours spent practicing: {self._stats_service.total_hours()}"
        )

        mean_label = ttk.Label(
            master=self._frame,
            text=f"Training session average length: {self._stats_service.average_duration()}"
        )

        total_label.grid(
            padx=5, pady=5, sticky=constants.EW
        )

        mean_label.grid(
            padx=5, pady=5, sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_body()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0, minsize=100)
