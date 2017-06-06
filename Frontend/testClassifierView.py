from tkinter import *
# import Frontend.errorWindow as error
# import Frontend.progressWindow as progress
import tkinter.filedialog


class testClassifierView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()
        self.hide()

    def initComponents(self):
        self.mainFrame = Frame(self.tk)
        self.mainFrame.pack(anchor=W,fill=X)

        B = Button(self.mainFrame, text='Back',width=5, command=self.onClickBack)
        B.pack(anchor=NW)

        self.lebelClassifier = LabelFrame(self.mainFrame, text="Choose Classifier:")
        self.lebelClassifier.pack(anchor=W, fill=X)

        self.selectedClassifier = StringVar()
        self.selectedClassifier.set("Choose Classifier")

        self.dropDown = OptionMenu(self.lebelClassifier,self.selectedClassifier,"SVM", "Word2Vec", "Neuron")
        self.dropDown.pack(fill=X)

        # self.lebelTestDocuments = Label(self.mainFrame, text="Documents for testing:")
        # self.lebelTestDocuments.pack(anchor=CENTER)
        #
        # self.selectedDocumentForTest = StringVar(self.tk)
        # self.selectedDocumentForTest.set("Choose option")
        #
        # self.dropDown = OptionMenu(self.mainFrame, self.selectedDocumentForTest, "Reuters")
        # self.dropDown.config(width=25,padx=50)
        # self.dropDown.pack(pady=20)

        # self.labelFrame_3 = LabelFrame(self.mainFrame, text="Document for testing:", padx=5, pady=5)
        # self.checkboxDocumentsForTesting = Checkbutton(self.labelFrame_3, text="from file",  command=self.onOpen)
        # self.checkboxDocumentsForTesting.pack(side=LEFT)
        # self.labelFrame_3.pack(anchor=W, fill=X)
        #
        # self.labelFrame_3 = LabelFrame(self.mainFrame)
        # self.txt = Text(self.labelFrame_3, width=70, height=10)
        # self.txt.pack(anchor=W, fill=X)
        # self.labelFrame_3.pack(anchor=W, fill=X)

        #documents for training
        self.labelFrame_3 = LabelFrame(self.mainFrame,text="Documents for training:",padx=5,pady=5)
        self.from_file = BooleanVar()
        self.checkboxDocumentsForTraining = Checkbutton(self.labelFrame_3, offvalue=False, onvalue=True, text="from file", var=self.from_file)
        self.checkboxDocumentsForTraining.pack(side=LEFT)
        self.entryDocumentsForTraining = Entry(self.labelFrame_3, width=30)
        self.entryDocumentsForTraining.pack(side=LEFT)
        self.labelFrame_3.pack(anchor=W,fill=X)

        self.testButton = Button(self.mainFrame, width=70, height=2, text='Test',command=self.onClickTest)
        self.testButton.pack(pady=5,fill=X)

    def onClickBack(self):
        self.hide()
        self.mv.show()

    def onClickTest(self):
        fromfile = False
        input = "input"
        args = self.getArgs()

        # self.mv.classifierManager.Test(fromfile,input,args)

    def getArgs(self):
        args = {"classifier":"",
                "...":"..."}
        return args

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack(fill=X,padx=5,pady=5)

    def onOpen(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tkinter.filedialog.Open(self.tk, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)











