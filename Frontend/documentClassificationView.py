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
        self.mainFrame.pack(fill=Y)

        B = Button(self.mainFrame, text='Back', command=self.onClickBack)
        B.pack(anchor=NW)

        # classifierChooser
        self.labelFrame_1 = LabelFrame(self.mainFrame, text="Select a classifier:", width=10)

        self.selectedClassifier = IntVar()
        self.selectedClassifier.set(1)

        self.labelFrame_1.pack(anchor=W, fill=X)

        # classifierOptions
        self.classifierOptionsFrame = LabelFrame(self.mainFrame, text="Classifier options:")
        self.classifierOptionsFrame.pack(anchor=W, fill=X)

        # document for classification
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
        # p = progress.progressWindow()
        return

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack()




if __name__ == '__main__':

    mw = mainWindow()
    # error.errorWindow("Error !")







