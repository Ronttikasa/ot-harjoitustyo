from tkinter import ttk, constants
from tkcalendar import Calendar

from services.entry_service import entry_service

class JournalView:
    def __init__(self, root, handle_main):
        self._root = root
        self._handle_main = handle_main
        self._frame = None

        self._cal = None
        self._start_time_entry = None
        self._end_time_entry = None
        self._notes_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_body()

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

    def _initialize_body(self):
        previous_entries_button = ttk.Button(
            master=self._frame,
            text="View previous entries",
            # command= handle previous
        )

        create_label = ttk.Label(
            master=self._frame,
            text="Create a new journal entry:"
        )
        self._cal = Calendar(
            master=self._frame,
            selectmode="day",
            year=2021,
            month=12,
            day=1
        )

        start_time_label = ttk.Label(master=self._frame, text="Start time (hh:mm)")
        self._start_time_entry = ttk.Entry(master=self._frame)

        end_time_label = ttk.Label(master=self._frame, text="End time (hh:mm)")
        self._end_time_entry = ttk.Entry(master=self._frame)

        notes_label = ttk.Label(master=self._frame, text="Notes:")
        self._notes_entry = ttk.Entry(master=self._frame)

        create_entry_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._handle_create_entry
        )      

        previous_entries_button.grid(row=1, columnspan=2, padx=5, pady=5, sticky=constants.EW)
        create_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.EW)
        self._cal.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        start_time_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.EW)
        self._start_time_entry.grid(row=5, column=0, padx=5, pady=5, sticky=constants.EW)
        end_time_label.grid(row=4, column=1, padx=5, pady=5, sticky=constants.EW)
        self._end_time_entry.grid(row=5, column=1, padx=5, pady=5, sticky=constants.EW)
        notes_label.grid(row=6, padx=5, pady=5, sticky=constants.EW)
        self._notes_entry.grid(row=7, columnspan=2, padx=5, pady=5, sticky=constants.EW)
        create_entry_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _handle_create_entry(self):
        date = self._cal.get_date() # datetime.date
        start = self._start_time_entry.get()
        end = self._end_time_entry.get()
        notes = self._notes_entry.get()

        entry_service.add_entry_gui(date, start, end, notes)
        self._start_time_entry.delete(0, constants.END)
        self._end_time_entry.delete(0, constants.END)
        self._notes_entry.delete(0, constants.END)
    
    
