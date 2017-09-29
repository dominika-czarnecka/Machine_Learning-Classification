from tkinter import *


class notificationWindow:
    def __init__(self, title, message):
        self.tk = Tk()
        self.tk.title(title)
        self.tk.minsize(width=400, height=100)
        notificationMessage = Label(self.tk, text=message)
        notificationMessage.pack(anchor=CENTER)

        button = Button(self.tk, text="OK", width="5", command=self.onCilckOkButton)
        button.pack(anchor=CENTER)
        self.tk.mainloop()

    def onCilckOkButton(self):
        self.tk.destroy()
