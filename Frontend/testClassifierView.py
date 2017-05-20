from tkinter import *
# import Frontend.errorWindow as error
# import Frontend.progressWindow as progress


class testClassifierView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.tk = tk
        self.initComponents()

    def initComponents(self):
        self.mainFrame = Frame(self.tk, padx=5, pady=5)
        self.mainFrame.pack(fill=X)

        B = Button(self.mainFrame, text='Back', command=self.onClickBack)
        B.pack(anchor=NW)



        self.testButton = Button(self.mainFrame, text='Test', command=self.onClickTest)
        self.testButton.pack(anchor=SE)

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











