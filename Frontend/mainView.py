from tkinter import *
import Frontend.newClassifierView as ncv

class mainView:
    def __init__(self, tk):
        self.tk = tk
        self.mainFrame = Frame(tk)
        newClassifierButton = Button(self.mainFrame, width="50", height="2", text='New classifier',command=self.onClickNewClassifierButton)
        newClassifierButton.pack(anchor=CENTER)
        testClassifierButton = Button(self.mainFrame, width="50", height="2", text='Test classifier',command=self.onClickTestClassifierButton)
        testClassifierButton.pack(anchor=CENTER)
        classifyDocumentButton = Button(self.mainFrame, width="50", height="2", text='Classify document',command=self.onClickClassifyDocumentButton)
        classifyDocumentButton.pack(anchor=CENTER)
        manageClassifierButton = Button(self.mainFrame, width="50", height="2", text='Manage classifiers',command=self.onClickManageClassifierButton)
        manageClassifierButton.pack(anchor=CENTER)

    def show(self):
        self.mainFrame.pack()

    def hide(self):
        self.mainFrame.pack_forget()

    def onClickNewClassifierButton(self):
        self.mainFrame.pack_forget()
        ncV = ncv.newClassifierView(self.tk, self)
        ncV.show()

    def onClickTestClassifierButton(self):
        return

    def onClickClassifyDocumentButton(self):
        return

    def onClickManageClassifierButton(self):
        return


