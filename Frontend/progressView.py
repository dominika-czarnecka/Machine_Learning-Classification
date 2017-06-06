from tkinter import *
from tkinter import ttk

class progressView:
    def __init__(self, tk):
        # self.mainFrame = Frame(tk)
        self.mainFrame = Frame(tk,padx=5,pady=5)
        self.titleLabel = Label(self.mainFrame, text="")

        self.titleLabel.pack()
        self.progressbar = ttk.Progressbar(self.mainFrame, orient="horizontal", length=200, mode="determinate")
        self.progressbar.pack(fill=X)
        self.descLabel = Label(self.mainFrame, text="")
        self.descLabel.pack()

        self.hide()



    def setProgressValue(self,value):
        self.progressbar["value"] = value
        self.titleLabel["text"] = "{0} %".format(value)

    def show(self):
        self.mainFrame.pack(anchor=S, fill=X)

    def hide(self):
        self.mainFrame.pack_forget()









