from tkinter import *
# import Frontend.errorWindow as error
# import Frontend.progressWindow as progress


class documentClassificationView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()
        self.hide()

    def initComponents(self):
        self.mainFrame = Frame(self.tk)
        self.mainFrame.pack(fill=X)

        self.backButton = Button(self.mainFrame, text='Back', width=5, command=self.onClickBack)
        self.backButton.pack(anchor=NW)

        self.lebelClassifier = LabelFrame(self.mainFrame, text="Choose Classifier:")
        self.lebelClassifier.pack(anchor=W, fill=X)

        self.selectedClassifier = StringVar()
        self.selectedClassifier.set("Choose Classifier")

        self.dropDown = OptionMenu(self.lebelClassifier,self.selectedClassifier,"SVM", "Word2Vec", "Neuron")
        self.dropDown.pack(fill=X)

        self.labelFrame_3 = LabelFrame(self.mainFrame, text="Document:")
        self.textField_1 = Text(self.labelFrame_3, width=70, height=30)
        self.textField_1.pack(anchor=W, fill=X)
        self.labelFrame_3.pack(anchor=W, fill=X)

        self.classifyButton = Button(self.mainFrame, text='Classify', command=self.onClickClassify, height=2)
        self.classifyButton.pack(fill=X,pady=5)

    def onClickBack(self):
        self.hide()
        self.mv.show()

    def onClickClassify(self):
        text = self.textField_1.get("1.0",END)
        # mv.classifierManager.Single(text,classifier)

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack(fill=X,padx=5,pady=5)











