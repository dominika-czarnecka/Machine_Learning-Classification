from tkinter import *

class manageClassifiersView:
    def __init__(self, tk, mv):
        self.tk = tk
        self.mv = mv
        # self.tk.title("Manage Classifiers")
        self.initComponents()
        # self.tk.mainloop()

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
        self.initClassifierList()
#        self.selectClassifier.bind("<Button-1>", self.click)

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
    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack(fill=X)

    def onClickBackButton(self):
        self.hide()
        self.mv.show()

    def initClassifierList(self):
        self.selectClassifier.insert(END, "Klasyfikator 1")
        self.selectClassifier.insert(END, "Klasyfikator 2")

    def onClickExecuteButton(self):
        selected = self.selectClassifier.curselection()
        self.selectClassifier.delete(selected)

   # def click(self, event):
#        widget = event.widget
 #       selected = widget.curselection()
        #value = widget.get(selected[0])
  #      self.classifierInformation.insert("0.0", widget.get(selected[0]))


# if __name__ == '__main__':
#     mw = manageClassifiersView()

