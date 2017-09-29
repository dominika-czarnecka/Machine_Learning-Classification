from tkinter import *


class helpView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()

    def initComponents(self):
        self.mainFrame = Frame(self.tk, padx=5, pady=5)
        self.mainFrame.pack(fill=X)

        self.backButton = Button(self.mainFrame, text='Back', command=self.onClickBack)
        self.backButton.pack(anchor=NW)

        self.newClassifierFrame = LabelFrame(self.mainFrame, text="New classifier:", width=200)
        self.newClassifierFrame.pack()
        text = Text(self.newClassifierFrame, height=8)
        text.insert(INSERT,
                    "From \"New classifier\" window you can train new classifiers "
                    "using given methods: SVM, Neural Networks and word2vec. "
                    "Each method is filled with default parameters. It is required "
                    "to insert a unique name for each classifier you want to train."
                    "Each method uses default training corpus, Reuters.")
        text.config(state=DISABLED)
        text.pack()
        self.testClassifierFrame = LabelFrame(self.mainFrame, text="Test classifier:", width=200)
        self.testClassifierFrame.pack()
        text = Text(self.testClassifierFrame, height=8)
        text.insert(INSERT, "From \"Test classifier\" window you can use trained classifiers to test them on "
                            "Reuters test corpus.")
        text.config(state=DISABLED)
        text.pack()
        self.classifySingleFrame = LabelFrame(self.mainFrame, text="Classify single document", width=200)
        self.classifySingleFrame.pack()
        text = Text(self.classifySingleFrame, height=8)
        text.insert(INSERT, "Using previously trained classifiers you can classify single document pasting its "
                            "text into text field. ")
        text.config(state=DISABLED)
        text.pack()
        self.manageClassifiersFrame = LabelFrame(self.mainFrame, text="Manage classifiers:", width=200)
        self.manageClassifiersFrame.pack()
        text = Text(self.manageClassifiersFrame, height=8)
        text.insert(INSERT, "You can manage your classifiers here. Delete them or preview its parameters.")
        text.config(state=DISABLED)
        text.pack()

    def onClickBack(self):
        self.hide()
        self.mv.show()
        self.mv.cp.toFile()

    def hide(self):
        self.mainFrame.pack_forget()

    def show(self):
        self.mainFrame.pack()
