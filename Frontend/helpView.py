from tkinter import *
# import Frontend.errorWindow as error
# import Frontend.progressWindow as progress
import tkinter.filedialog

from Backend.Integration.ClassificatorEnum import ClassificatorEnum


class helpView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()

    def initComponents(self):
        self.mainFrame = Frame(self.tk, padx=5, pady=5)
        self.mainFrame.pack(fill=X)

        self.backButton = Button(self.mainFrame, text='Back', command=self.onClickBack)
        self.backButton.pack(anchor=NW)

        self.labelFrame_1 = LabelFrame(self.mainFrame,text="New classifier:",width=200)
        self.labelFrame_1.pack()
        text = Text(self.labelFrame_1,height=8)
        text.insert(INSERT, "New classifier description here...")
        text.config(state=DISABLED)
        text.pack()
        self.labelFrame_2 = LabelFrame(self.mainFrame,text="Test classifier:",width=200)
        self.labelFrame_2.pack()
        text = Text(self.labelFrame_2,height=8)
        text.insert(INSERT, "Test classifier description here...")
        text.config(state=DISABLED)
        text.pack()
        self.labelFrame_3 = LabelFrame(self.mainFrame,text="Classify single document",width=200)
        self.labelFrame_3.pack()
        text = Text(self.labelFrame_3,height=8)
        text.insert(INSERT, "Classify single document description here...")
        text.config(state=DISABLED)
        text.pack()
        self.labelFrame_4 = LabelFrame(self.mainFrame,text="Manage classifiers:",width=200)
        self.labelFrame_4.pack()
        text = Text(self.labelFrame_4,height=8)
        text.insert(INSERT, "Manage classifiers description here...")
        text.config(state=DISABLED)
        text.pack()



    def onClickBack(self):
        self.hide()
        self.mv.show()
        self.mv.cp.toFile()



    def getArgs(self):
        args = {"classifier":"",
                "...":"..."}
        return args

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack()













