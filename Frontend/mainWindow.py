from tkinter import *

class mainWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification")

        self.init_classifierChooser()
        self.init_classifierOptions()

        self.tk.mainloop()

    def init_classifierChooser(self):
        self.labelFrame_1 = LabelFrame(self.tk,text="Select a classifier:")

        self.var = IntVar()
        R1 = Radiobutton(self.labelFrame_1, text="SVM", variable=self.var, value=1, command=self.onChoseClassifier)
        R1.grid(row=0,column=0)

        R2 = Radiobutton(self.labelFrame_1, text="Word2vec", variable=self.var, value=2, command=self.onChoseClassifier)
        R2.grid(row=0,column=1)

        R3 = Radiobutton(self.labelFrame_1, text="Neural networks", variable=self.var, value=3, command=self.onChoseClassifier)
        R3.grid(row=0,column=2)

        self.labelFrame_1.pack(anchor=W)

    def init_classifierOptions(self):
        self.labelFrame_2 = LabelFrame(self.tk,text="Classifier options:")

        self.label_1 = Label(self.labelFrame_2)
        self.label_1.pack()

        self.labelFrame_2.pack(anchor=W)


    def onChoseClassifier(self):
        selection = "Radiobutton value: " + str(self.var.get())
        self.label_1.config(text = selection)



if __name__ == '__main__':
    mw = mainWindow()