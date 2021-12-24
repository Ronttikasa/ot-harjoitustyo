from tkinter import ttk, constants


class MainView:
    def __init__(self, root, handle_journal, handle_goals, handle_stats):
        self._root = root
        self._handle_journal = handle_journal
        self._handle_goals = handle_goals
        self._handle_stats = handle_stats
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Welcome to your training journal!",
            font=25
        )

        button_journal = ttk.Button(
            master=self._frame,
            text="Journal",
            command=self._handle_journal
        )
        button_goals = ttk.Button(
            master=self._frame,
            text="Goals",
            command=self._handle_goals
        )
        button_stats = ttk.Button(
            master=self._frame,
            text="Stats",
            command=self._handle_stats
        )

        label.grid(row=0, column=0, padx=5, pady=5)
        button_journal.grid(row=1, column=0, padx=5, pady=5)
        button_goals.grid(row=2, column=0, padx=5, pady=5)
        button_stats.grid(row=3, column=0, padx=5, pady=5)
        self._frame.grid_columnconfigure(0, weight=1, minsize=500)
