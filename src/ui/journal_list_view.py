from tkinter import ttk, constants
from services.entry_service import entry_service


class JournalItemView:
    def __init__(self, root, entries, handle_delete):
        self._root = root
        self._entries = entries
        self._handle_delete = handle_delete
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        for entry in self._entries:
            self._initialize_entry(entry)

    def _initialize_entry(self, entry):
        entry_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=entry_frame, text=str(entry))

        delete_button = ttk.Button(
            master=entry_frame,
            text="Delete",
            command=lambda: self._handle_delete(entry.id)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.EW)
        delete_button.grid(row=0, column=1, padx=5,
                           pady=5, sticky=constants.EW)

        entry_frame.grid_columnconfigure(0, weight=1, minsize=400)
        entry_frame.pack(fill=constants.X)


class JournalListView:
    def __init__(self, root, handle_main):
        self._root = root
        self._handle_main = handle_main
        self._frame = None
        self._journal_list_frame = None
        self._journal_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_delete_entry(self, entry_id):
        entry_service.delete_entry(entry_id)
        self._initialize_entry_list()

    def _initialize_entry_list(self):
        if self._journal_list_view:
            self._journal_list_view.destroy()

        entries = entry_service.list_all()

        self._journal_list_view = JournalItemView(
            self._journal_list_frame,
            entries,
            self._handle_delete_entry
        )

        self._journal_list_view.pack()

    def _initialize_header(self):
        header_label = ttk.Label(
            master=self._frame, text="Training journal", font=20
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
            row=0, column=1, padx=5, pady=10, sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._journal_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_entry_list()

        self._journal_list_frame.grid(
            row=1,
            column=0,
            columnspan=2
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0, minsize=100)
