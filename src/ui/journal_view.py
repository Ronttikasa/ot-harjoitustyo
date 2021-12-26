from tkinter import StringVar, ttk, constants
from tkcalendar import Calendar
from datetime import datetime
from services.entry_service import entry_service, InvalidTimeEntryError


class JournalView:
    def __init__(self, root, handle_main, handle_previous):
        self._root = root
        self._handle_main = handle_main
        self._handle_show_previous = handle_previous
        self._frame = None

        self._cal = None
        self._start_time_entry = None
        self._end_time_entry = None
        self._notes_entry = None
        self._error_msg = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_msg = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_msg,
            foreground="red"
        )
        self._error_label.grid(row=8, padx=5, pady=5)

        self._initialize_header()
        self._initialize_body()

        self._frame.grid_columnconfigure(0, weight=1, minsize=250)
        self._frame.grid_columnconfigure(1, weight=1, minsize=250)

    def _initialize_header(self):
        header_label = ttk.Label(
            master=self._frame,
            text="Your training journal",
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

        self._hide_error()

    def _initialize_body(self):
        previous_entries_button = ttk.Button(
            master=self._frame,
            text="View previous entries",
            command=self._handle_show_previous
        )

        create_label = ttk.Label(
            master=self._frame,
            text="Create a new journal entry:"
        )
        current_date = datetime.now()
        self._cal = Calendar(
            master=self._frame,
            selectmode="day",
            date_pattern="dd/mm/yy",
            year=current_date.year,
            month=current_date.month,
            day=current_date.day
        )

        start_time_label = ttk.Label(
            master=self._frame, text="Start time (hh:mm)")
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

        previous_entries_button.grid(
            row=1, columnspan=2, padx=5, pady=5, sticky=constants.EW
        )
        create_label.grid(
            row=2, column=0, padx=5, pady=5, sticky=constants.EW
        )
        self._cal.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5
        )
        start_time_label.grid(
            row=4, column=0, padx=5, pady=5, sticky=constants.EW
        )
        end_time_label.grid(
            row=4, column=1, padx=5, pady=5, sticky=constants.EW
        )
        self._start_time_entry.grid(
            row=5, column=0, padx=5, pady=5, sticky=constants.EW
        )
        self._end_time_entry.grid(
            row=5, column=1, padx=5, pady=5, sticky=constants.EW
        )
        notes_label.grid(
            row=6, padx=5, pady=5, sticky=constants.EW
        )
        self._notes_entry.grid(
            row=7, columnspan=2, padx=5, pady=5, sticky=constants.EW
        )
        create_entry_button.grid(
            row=9, columnspan=2, padx=5, pady=5, sticky=constants.EW
        )

    def _handle_create_entry(self):
        entry_date = datetime.strptime(self._cal.get_date(), "%d/%m/%y")
        start = self._start_time_entry.get()
        end = self._end_time_entry.get()
        notes = self._notes_entry.get()

        try:
            entry_service.add_entry(entry_date, start, end, notes)
            self._start_time_entry.delete(0, constants.END)
            self._end_time_entry.delete(0, constants.END)
            self._notes_entry.delete(0, constants.END)
            self._hide_error()
        except InvalidTimeEntryError:
            self._show_error(f"Check that times are in hh:mm format")

    def _show_error(self, message):
        self._error_msg.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()
