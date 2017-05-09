from tkinter import *
import tkinter.messagebox

class errorWindow:
    def __init__(self, message):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification ERROR!")
        errorMessage = Label(self.tk,text=message)
        errorMessage.pack(anchor=CENTER)


        button = Button (self.tk, text="OK", width="5")
        button.pack(anchor=CENTER)
        self.tk.mainloop()