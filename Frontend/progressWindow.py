from tkinter import *
from tkinter import ttk

class progressWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification Progress")

        self.progressLabel = Label(self.tk, text="")
        self.progressLabel.pack()
        self.progressbar = ttk.Progressbar(self.tk, orient="horizontal", length=200, mode="determinate")
        self.progressbar.pack()
        self.setProgressValue(72)

        self.tk.mainloop()

    def setProgressValue(self,value):
        self.progressbar["value"] = value
        self.progressLabel["text"] = value