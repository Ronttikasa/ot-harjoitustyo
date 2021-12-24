from tkinter import ttk, constants

from services.goal_service import goal_service


class GoalsListView:
    def __init__(self, root, goals, handle_set_goal_reached):
        self._root = root
        self._goals = goals
        self._handle_set_goal_reached = handle_set_goal_reached
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_goal(self, goal):
        goal_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=goal_frame, text=goal.content)

        set_goal_reached_button = ttk.Button(
            master=goal_frame,
            text="Reached!",
            command=lambda: self._handle_set_goal_reached(goal.id)
        )

        label.grid(
            row=0, column=0, padx=5, pady=5, sticky=constants.EW
        )
        set_goal_reached_button.grid(
            row=0, column=1, padx=5, pady=5, sticky=constants.EW
        )

        goal_frame.grid_columnconfigure(0, weight=1, minsize=400)
        goal_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for goal in self._goals:
            self._initialize_goal(goal)


class GoalsView:
    def __init__(self, root, handle_main):
        self._root = root
        self._handle_main = handle_main
        self._create_goal_entry = None
        self._frame = None
        self._goals_list_frame = None
        self._goals_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_set_goal_reached(self, goal_id):
        goal_service.mark_done(goal_id)
        self._initialize_goal_list()

    def _initialize_goal_list(self):
        if self._goals_list_view:
            self._goals_list_view.destroy()

        goals = goal_service.list_all_unreached()

        self._goals_list_view = GoalsListView(
            self._goals_list_frame,
            goals,
            self._handle_set_goal_reached
        )

        self._goals_list_view.pack()

    def _initialize_header(self):
        header_label = ttk.Label(
            master=self._frame, text="Your figure skating goals", font=20)

        header_back_button = ttk.Button(
            master=self._frame,
            text="Main menu ->",
            command=self._handle_main
        )

        header_label.grid(
            row=0, column=0, padx=5, pady=10
        )

        header_back_button.grid(
            row=0, column=1, padx=5, pady=10, sticky=constants.EW
        )

    def _initialize_footer(self):
        self._create_goal_entry = ttk.Entry(master=self._frame)

        create_goal_button = ttk.Button(
            master=self._frame,
            text="Set new goal",
            command=self._handle_create_goal
        )

        self._create_goal_entry.grid(
            row=2, column=0, padx=5, pady=5, sticky=constants.EW
        )

        create_goal_button.grid(
            row=2, column=1, padx=5, pady=5, sticky=constants.EW
        )

    def _handle_create_goal(self):
        goal_content = self._create_goal_entry.get()

        if goal_content:
            goal_service.add_goal(goal_content)
            self._initialize_goal_list()
            self._create_goal_entry.delete(0, constants.END)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._goals_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_goal_list()
        self._initialize_footer()

        self._goals_list_frame.grid(
            row=1,
            column=0,
            columnspan=2
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0, minsize=100)
