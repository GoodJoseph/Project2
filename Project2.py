from projectGUI import *

def main():
    """The Function that runs the entire program and sets the specifics for the widget"""
    window = Tk()
    window.title("Project 1")
    window.geometry("250x300")
    window.resizable(False, False)
    Grades(window)
    window.mainloop()


if __name__ == "__main__":
    main()