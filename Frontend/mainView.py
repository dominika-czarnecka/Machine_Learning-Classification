from tkinter import *
import Frontend.newClassifierView as ncv
import Frontend.manageClassifiersView as mcv
import Frontend.documentClassificationView as dcv
import Frontend.testClassifierView as tcv
from Backend.Integration.ClassificatorsProvider import ClassificatorsProvider
from Backend.Integration.ClassifierManager import ClassifierManager

class mainView:

    def __init__(self, tk):
        self.tk = tk
        self.classifierManager = ClassifierManager()
        self.cp = ClassificatorsProvider()
        self.mainFrame = Frame(tk)
        buttonPadding = 5
        newClassifierButton = Button(self.mainFrame, width="50", height="2",  text='New classifier',command=self.onClickNewClassifierButton)
        newClassifierButton.pack(anchor=CENTER, pady=buttonPadding)
        testClassifierButton = Button(self.mainFrame, width="50", height="2", text='Test classifier',command=self.onClickTestClassifierButton)
        testClassifierButton.pack(anchor=CENTER, pady=buttonPadding)
        # classifyDocumentButton = Button(self.mainFrame, width="50", height="2", text='Classify document',command=self.onClickClassifyDocumentButton)
        # classifyDocumentButton.pack(anchor=CENTER, pady=buttonPadding)
        manageClassifierButton = Button(self.mainFrame, width="50", height="2", text='Manage classifiers',command=self.onClickManageClassifierButton)
        manageClassifierButton.pack(anchor=CENTER, pady=buttonPadding)

    def show(self):
        self.mainFrame.pack(expand=True)

    def hide(self):
        self.mainFrame.pack_forget()

    def onClickNewClassifierButton(self):
        self.mainFrame.pack_forget()
        ncV = ncv.newClassifierView(self.tk, self)
        ncV.show()

    def onClickTestClassifierButton(self):
        self.hide()
        tcV = tcv.testClassifierView(self.tk, self)
        tcV.show()
        return

    def onClickClassifyDocumentButton(self):
        self.hide()
        dcV = dcv.documentClassificationView(self.tk, self)
        dcV.show()
        return

    def onClickManageClassifierButton(self):
        self.hide()
        mcV = mcv.manageClassifiersView(self.tk, self)
        mcV.show()


