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
        # self.mainFrame.grid()

        self.labelFrame_1 = LabelFrame(self.mainFrame)
        self.labelFrame_1.grid(sticky=W)
        self.labelFrame_2 = LabelFrame(self.mainFrame, height=70, width=100)
        self.labelFrame_2.grid(sticky=E)

        self.labelFrame_3 = LabelFrame(self.mainFrame, height=70, width=100)
        self.labelFrame_3.grid(sticky=SE)

        self.backButton = Button(self.labelFrame_1, text="Back", command=self.onClickBackButton)
        self.backButton.grid(row=0, column=0, sticky=W)

        self.classifierTypeText = Label(self.labelFrame_2, text="Classifiers")
        self.classifierTypeText.grid(row=1, column=0, sticky=N)

        self.selectClassifier = Listbox(self.labelFrame_2)
        self.selectClassifier.grid(row=2, column=0, sticky=N)

        self.classifierTypeText = Label(self.labelFrame_2, text="Information about Classifier")
        self.classifierTypeText.grid(row=1, column=1, sticky=N)

        self.classifierInformation = Text(self.labelFrame_2, width=40)
        self.classifierInformation.grid(row=2, column=1, sticky=E)

        self.selectAction = Listbox(self.labelFrame_3, height=1, width=20)
        self.selectAction.grid(row=0, column=0)

        self.selectAction.insert(END, "Remove")
        self.selectAction.insert(END, "Add")

        self.executeButton = Button(self.labelFrame_3, text="Execute")
        self.executeButton.grid(row=0, column=1)

        self.labelFrame_1.grid()
        self.labelFrame_2.grid()
        self.labelFrame_3.grid()

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack()

    def onClickBackButton(self):
        self.hide()
        self.mv.show()

# if __name__ == '__main__':
#     mw = manageClassifiersView()

