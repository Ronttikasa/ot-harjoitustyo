from tkinter import Tk
from ui.gui import GUI


def main():
    window = Tk()
    window.title("Training journal")

    app_ui = GUI(window)
    app_ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
