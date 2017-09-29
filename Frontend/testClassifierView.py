from nltk.corpus import reuters

import Frontend.errorWindow as error
import tkinter.filedialog
from tkinter import *

from Backend.Integration.ClassificatorEnum import ClassificatorEnum
from Frontend.errorWindow import errorWindow as error
from Frontend.notificationWindow import notificationWindow as notification

errorMessage = "Something went wrong."


class testClassifierView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()
        self.clEnum = ClassificatorEnum.SVM

    def initComponents(self):
        self.mainFrame = Frame(self.tk, padx=2, pady=5)
        self.mainFrame.pack()

        B = Button(self.mainFrame, text='Back', command=self.onClickBack)
        B.pack(anchor=NW)

        self.lebelClassifier = Label(self.mainFrame, text="Choose Classifier Options:")
        self.lebelClassifier.pack(anchor=CENTER, pady=10)

        self.selectedClassifier = StringVar()
        self.selectedClassifier.set("Choose option")

        names = self.mv.cp.names()
        if len(names) == 0:
            self.onClickBack()
            error("Please create at least one classifier!")

        self.dropDownNames = OptionMenu(self.mainFrame, self.selectedClassifier, *names)
        self.dropDownNames.config(width=25, padx=50)
        self.dropDownNames.pack(pady=10)

        self.lebelTestDocuments = Label(self.mainFrame, text="Documents for testing:")
        self.lebelTestDocuments.pack(anchor=CENTER)

        self.selectedDocumentForTest = StringVar(self.tk)
        self.selectedDocumentForTest.set("Reuters")

        self.dropDown = OptionMenu(self.mainFrame, self.selectedDocumentForTest, "Reuters")
        self.dropDown.config(width=25, padx=50)
        self.dropDown.pack(pady=20)

        # self.labelFrame_3 = LabelFrame(self.mainFrame, text="Document for testing:", padx=5, pady=5)
        # self.checkboxDocumentsForTesting = Checkbutton(self.labelFrame_3, text="from file", command=self.onOpen)
        # self.checkboxDocumentsForTesting.pack(side=LEFT)
        # self.labelFrame_3.pack(anchor=W, fill=X)
        #
        # self.labelFrame_3 = LabelFrame(self.mainFrame)
        # self.txt = Text(self.labelFrame_3, width=70, height=10)
        # self.txt.pack(anchor=W, fill=X)
        # self.labelFrame_3.pack(anchor=W, fill=X)

        self.testButton = Button(self.mainFrame, width=70, height=2, text='Test', command=self.onClickTest)
        self.testButton.pack(anchor=SE, pady=20)

    def onClickBack(self):
        self.hide()
        self.mv.show()
        self.mv.cp.toFile()


    def onClickTest(self):
        name = self.selectedClassifier.get()
        type, c = self.mv.cp.find(name)
        args = self.resolveArgs(type, c)
        result = self.mv.classifierManager.test(False, 'reuters', args, name, type)
        if len(result) != 0:
            notification("Result: \n", result)
        else:
            error(errorMessage)

    def resolveArgs(self, type, classifier):
        args = {}
        if type == ClassificatorEnum.NeuralNetwork:
            args = {"target": classifier.target,
                 "vocabulary_len": classifier.vocabulary_len}
        elif type == ClassificatorEnum.Word2Vec:
            args = {
                "categories": reuters.categories,
                "threshold": 1,
                "name": classifier.name,
                "path": classifier.path,
                "size": classifier.size,
                "iter": classifier.iter,
                "min_count": classifier.min_count,
                "window": classifier.window
            }
        return args

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack()

    # def onOpen(self):
    #     ftypes = [('Binary files', '*.bin'), ('All files', '*')]
    #     dlg = tkinter.filedialog.Open(self.tk, filetypes=ftypes)
    #     fl = dlg.show()
    #
    #     if fl != '':
    #         text = self.readFile(fl)
    #         self.txt.insert(END, text)
