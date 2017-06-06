from tkinter import *
from tkinter import ttk

class resultWindow:
    def __init__(self, result):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification Result")
        self.tk.minsize(width=400,height=100)
        mainFrame = Frame(self.tk)
        mainFrame.pack(expand=True,anchor=CENTER)
        self.resultLabel = Label(mainFrame, text=result)
        self.resultLabel.pack(fill=X)

        button = Button (self.tk, text="OK", width="5", command=self.onCilckOkButton)
        button.pack(side=BOTTOM, pady=5)
        self.tk.mainloop()

    def onCilckOkButton(self):
        self.tk.destroy()


resultWindow("Result")