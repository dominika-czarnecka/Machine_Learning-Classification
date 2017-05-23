from tkinter import *
# import Frontend.errorWindow as error
# import Frontend.progressWindow as progress


class documentClassificationView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()

    def initComponents(self):
        self.mainFrame = Frame(self.tk, padx=5, pady=5)
        self.mainFrame.pack(fill=X)

        self.backButton = Button(self.mainFrame, text='Back', command=self.onClickBack)
        self.backButton.pack(anchor=NW)

        self.selectedClassifier = StringVar(self.tk)
        self.selectedClassifier.set("Choose Classifier")

        self.dropDown = OptionMenu(self.mainFrame, self.selectedClassifier, "SVM", "Word2Vec", "Neuron")
        self.dropDown.config(width=15)
        self.dropDown.pack(anchor=W, fill=X)

        self.labelFrame_3 = LabelFrame(self.mainFrame, text="Document:", padx=5, pady=5)
        self.textField_1 = Text(self.labelFrame_3, width=70, height=30)
        self.textField_1.pack(anchor=W, fill=X)
        self.labelFrame_3.pack(anchor=W, fill=X)

        self.classifyButton = Button(self.mainFrame, text='Classify', command=self.onClickClassify)
        self.classifyButton.pack(anchor=SE)

    def onClickBack(self):
        self.hide()
        self.mv.show()

    def onClickClassify(self):
        return

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack()











