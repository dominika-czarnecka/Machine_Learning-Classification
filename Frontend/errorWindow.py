from tkinter import *
import tkinter.messagebox

class errorWindow:
    def __init__(self, message):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification ERROR!")
        self.tk.minsize(width=400,height=100)
        errorMessage = Label(self.tk,text=message)
        errorMessage.pack(anchor=CENTER)


        button = Button (self.tk, text="OK", width="5", command=self.onCilckOkButton)
        button.pack(anchor=CENTER)
        self.tk.mainloop()

    def onCilckOkButton(self):
        self.tk.destroy()