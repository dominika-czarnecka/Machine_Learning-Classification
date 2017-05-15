from tkinter import *
from tkinter import ttk

class resultWindow:
    def __init__(self, result):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification Result")

        mainFrame = Frame(self.tk, width=200, height=200)
        mainFrame.pack()
        self.resultLabel = Label(mainFrame, text=result)
        self.resultLabel.pack()

        self.tk.mainloop()