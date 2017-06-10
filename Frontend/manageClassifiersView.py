from tkinter import *
import os, os.path
from Backend.Integration.ClassificatorEnum import ClassificatorEnum
from Backend.Integration.ClassificatorsProvider import ClassificatorsProvider


class manageClassifiersView:
    def __init__(self, tk, mv):
        self.tk = tk
        self.mv = mv
        # self.pathWithClassifiers = "test/"
        self.listOfFiles = self.mv.cp.names()#[name for name in os.listdir(self.pathWithClassifiers) if os.path.isfile(os.path.join(self.pathWithClassifiers, name))]
        self.initComponents()

    def initComponents(self):
        self.mainFrame = Frame(self.tk, padx=5, pady=5)

        self.backButton = Button(self.mainFrame, text="Back", command=self.onClickBackButton)
        self.backButton.pack(anchor=NW)

        self.labelFrame_1 = LabelFrame(self.mainFrame, height=70, width=100, text="Classifiers")
        self.labelFrame_1.pack(side=LEFT)
        self.labelFrame_2 = LabelFrame(self.mainFrame, height=70, width=100, text="Information about Classifier")
        self.labelFrame_2.pack(side=LEFT)

        self.selectClassifier = Listbox(self.labelFrame_1, height=25, width=40)
        self.selectClassifier.pack(anchor=N)
        self.selectClassifier.bind("<Double-Button-1>", self.onClickClassifier)

        self.classifierInformation = Text(self.labelFrame_2, height=25, width=40)
        self.classifierInformation.pack(anchor=N)

        self.labelFrame_3 = LabelFrame(self.labelFrame_2, height=10, width=40)
        self.labelFrame_3.pack(anchor=SE)

        self.selectAction = Listbox(self.labelFrame_3, height=1, width=40)
        self.selectAction.grid(column=0, row=0)

        self.selectAction.insert(END, "Remove")

        self.executeButton = Button(self.labelFrame_3, text="Execute", width=10, command=self.onClickExecuteButton)
        self.executeButton.grid(column=1, row=0)

        self.labelFrame_1.pack(fill=Y)
        self.labelFrame_2.pack(fill=X)

        self.initClassifierList()

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack(fill=X)

    def onClickBackButton(self):
        self.hide()
        self.mv.show()

    def initClassifierList(self):
        for i in self.listOfFiles:
            self.selectClassifier.insert(END, i)

    def onClickClassifier(self, event):
        self.classifierInformation.delete("1.0", END)
        widget = event.widget
        selection = widget.curselection()
        file_name = widget.get(selection[0])
        type, c = self.mv.cp.find(file_name)
        self.classifierInformation.insert(INSERT, c.display())

    def onClickExecuteButton(self):
        selection = self.selectClassifier.curselection()
        file_name = self.selectClassifier.get(selection[0])
        type, c = self.mv.cp.find(file_name)
        self.mv.cp.remove(classificatorType=type, classificator=c)
        self.classifierInformation.delete("1.0", END)
        self.selectClassifier.delete(selection)



