from tkinter import *
# import Frontend.errorWindow as error
# import Frontend.progressWindow as progress


class testClassifierView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()

    def initComponents(self):
        self.mainFrame = Frame(self.tk, padx=2,pady=5)
        self.mainFrame.pack(fill=X)


        B = Button(self.mainFrame, text='Back', command=self.onClickBack)
        B.pack(anchor=NW)

        self.lebelClassifier = Label(self.mainFrame, text="Choose Classifier Options:")
        self.lebelClassifier.pack(anchor=CENTER, pady=10)

        self.selectedClassifier = StringVar()
        self.selectedClassifier.set("Choose option")

        self.dropDown = OptionMenu(self.mainFrame, self.selectedClassifier, "SVM", "Word2Vec", "Neuron")
        self.dropDown.config(width=25,padx=50)
        self.dropDown.pack(pady=10)

        self.lebelTestDocuments = Label(self.mainFrame, text="Documents for testing:")
        self.lebelTestDocuments.pack(anchor=CENTER)

        self.selectedDocumentForTest = StringVar()
        self.selectedDocumentForTest.set("Choose option")

        self.dropDown = OptionMenu(self.mainFrame, self.selectedDocumentForTest, "Reuters")
        self.dropDown.config(width=25,padx=50)
        self.dropDown.pack(pady=20)

        self.testButton = Button(self.mainFrame, width=70, height= 5, text='Test', command=self.onClickTest)
        self.testButton.pack(anchor=N, pady=30)

    def onClickBack(self):
        self.hide()
        self.mv.show()

    def onClickTest(self):
        # p = progress.progressWindow()
        return

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack()











