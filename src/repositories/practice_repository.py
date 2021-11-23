class PracticeRepository:

    def __init__(self):
        pass

    def create(self, practice):
        self._write(practice)

    def get_all(self):
        return(self._read())

    def delete_all(self):
        with open("trainingjournal.txt", "w") as file:
            file.write("")

    def _write(self, practice):
        with open("trainingjournal.txt", "a") as file:
            file.write(f"{practice}\n")

    def _read(self):
        practices = []
        with open("trainingjournal.txt") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                date = parts[0]
                start = parts[1]
                end = parts[2]
                notes = parts[3]

                practices.append(f"{date}, from {start} to {end}, {notes}")

        return practices

practice_repository = PracticeRepository()