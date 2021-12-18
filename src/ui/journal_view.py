from tkinter import ttk, constants
from tkcalendar import Calendar

from services.entry_service import entry_service

class JournalView:
    def __init__(self, root, handle_main):
        self._root = root
        self._handle_main = handle_main
        self._frame = None
        self._entries_list_frame = None
        self._entries_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_footer()

    def _initialize_header(self):
        header_label = ttk.Label(
            master=self._frame,
            text="Your training journal"
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

    def _initialize_footer(self):
        footer_label = ttk.Label(
            master=self._frame,
            text="Create a new journal entry"
        )
        cal = Calendar(
            master=self._frame,
            selectmode="day",
            year=2021,
            month=12,
            day=1
        )

        start_time_label = ttk.Label(master=self._frame, text="start time (hh:mm)")
        start_time_entry = ttk.Entry(master=self._frame)

        end_time_label = ttk.Label(master=self._frame, text="end time (hh:mm)")
        end_time_entry = ttk.Entry(master=self._frame)        


        footer_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.EW)
        cal.grid(row=3, column=0, padx=5, pady=5)

    def handle_create_entry(self):
        date = cal.get_date() # datetime.date
