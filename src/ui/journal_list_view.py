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
        self._frame = ttk.Frame(master=self._frame)
        for entry in self._entries:
            self._initialize_entry(entry)

    def _initialize_entry(self, entry):
        entry_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=self._frame, text=str(entry))

        delete_button = ttk.Button(
            master=self._frame,
            text="Delete",
            command=lambda: self._handle_delete(entry.id)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.EW)
        delete_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

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

