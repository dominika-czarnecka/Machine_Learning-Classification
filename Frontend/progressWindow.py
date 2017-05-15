from tkinter import *
from tkinter import ttk

class progressWindow:
    def __init__(self, title, desc=""):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification Progress")
        self.tk.minsize(width=400,height=100)

        self.titleLabel = Label(self.tk, text=title)
        self.titleLabel.pack()
        self.progressbar = ttk.Progressbar(self.tk, orient="horizontal", length=200, mode="determinate")
        self.progressbar.pack()
        self.descLabel = Label(self.tk, text=desc)
        self.descLabel.pack()
        self.setProgressValue(72)

        self.tk.mainloop()

    def setProgressValue(self,value):
        self.progressbar["value"] = value
        self.titleLabel["text"] = "{0} %".format(value)