from tkinter import *
# import Frontend.errorWindow as error
# import Frontend.progressWindow as progress
import tkinter.filedialog

from Backend.Integration.ClassificatorEnum import ClassificatorEnum


class testClassifierView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()
        self.clEnum = ClassificatorEnum.SVM

    def initComponents(self):
        self.mainFrame = Frame(self.tk, padx=2,pady=5)
        self.mainFrame.pack()

        B = Button(self.mainFrame, text='Back', command=self.onClickBack)
        B.pack(anchor=NW)

        self.lebelClassifier = Label(self.mainFrame, text="Choose Classifier Options:")
        self.lebelClassifier.pack(anchor=CENTER, pady=10)

        self.selectedClassifier = StringVar(self.tk)
        self.selectedClassifier.set("Choose option")

        self.dropDown = OptionMenu(self.mainFrame, self.selectedClassifier, *self.mv.cp.names())
        self.dropDown.config(width=25,padx=50)
        self.dropDown.pack(pady=10)

        self.lebelTestDocuments = Label(self.mainFrame, text="Documents for testing:")
        self.lebelTestDocuments.pack(anchor=CENTER)

        self.selectedDocumentForTest = StringVar(self.tk)
        self.selectedDocumentForTest.set("Choose option")

        self.dropDown = OptionMenu(self.mainFrame, self.selectedDocumentForTest, "Reuters")
        self.dropDown.config(width=25,padx=50)
        self.dropDown.pack(pady=20)

        self.labelFrame_3 = LabelFrame(self.mainFrame, text="Document for testing:", padx=5, pady=5)
        self.checkboxDocumentsForTesting = Checkbutton(self.labelFrame_3, text="from file",  command=self.onOpen)
        self.checkboxDocumentsForTesting.pack(side=LEFT)
        self.labelFrame_3.pack(anchor=W, fill=X)

        self.labelFrame_3 = LabelFrame(self.mainFrame)
        self.txt = Text(self.labelFrame_3, width=70, height=10)
        self.txt.pack(anchor=W, fill=X)
        self.labelFrame_3.pack(anchor=W, fill=X)

        self.testButton = Button(self.mainFrame, width=70, height= 2, text='Test',command=self.onClickTest)
        self.testButton.pack(anchor=SE, pady=20)

    def onClickBack(self):
        self.hide()
        self.mv.show()
        self.mv.cp.toFile()

    def onClickTest(self):
        fromfile = False
        input = "input"
        args = self.getArgs()
        name = ""
        type = self.clEnum

        self.mv.classifierManager.Test(fromfile,input,args, name, type)

    def getArgs(self):
        args = {"classifier":"",
                "...":"..."}
        return args

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack()

    def onOpen(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tkinter.filedialog.Open(self.tk, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)











