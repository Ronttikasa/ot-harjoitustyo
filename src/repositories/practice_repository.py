from entities.practice import Practice

# luokka tallentaa tietoa toistaiseksi kovakoodattuun tiedostoon trainingjournal.txt,
# tämä on tarkoitus muuttaa myöhemmin


class PracticeRepository:
    """The class responsible for the database operations of practice journal entries.
    """

    def __init__(self):
        pass

    def create(self, entry: Practice):
        """Adds a new practice entry to the database.

        Args:
            entry (Practice): The entry to be added to the database.
        """

        self._write([entry])

    def list_all(self):
        """Returns all the practice journal entries.

        Returns:
            A list of Practice objects.
        """

        return self._read()

    def list_all_with_number(self):
        """Prints all the entries with an identifying number
        """

        for index, entry in enumerate(self.list_all()):
            print(index+1, entry)

    def delete_all(self):
        """Deletes all the entries in the database.
        """

        with open("trainingjournal.txt", "w", encoding="utf-8") as file:
            file.write("")

    def delete_entry(self, tbd_id):
        """Deletes a practice journal entry.

        Args:
            tbd_id: Id of the entry to be deleted
        """
        entries = self._read()
        entries = [entry for entry in entries if entry.id != tbd_id]
        self.delete_all()
        self._write(entries)

    def _write(self, entries: list):
        with open("trainingjournal.txt", "a", encoding="utf-8") as file:
            for entry in entries:
                row = f"{entry.id};{entry.date};{entry.start};{entry.end};{entry.notes}"
                file.write(f"{row}\n")

    def _read(self):
        entries = []
        with open("trainingjournal.txt", encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                if row == "":
                    continue
                parts = row.split(";")

                prac_id = parts[0]
                date = parts[1]
                start = parts[2]
                end = parts[3]
                notes = parts[4]

                entries.append(
                    Practice(date, start, end, notes, prac_id))

        return entries


practice_repository = PracticeRepository()
