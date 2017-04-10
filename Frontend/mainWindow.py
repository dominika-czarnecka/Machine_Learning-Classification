from tkinter import *

class mainWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification")

        self.initComponents()

        self.tk.mainloop()

    def initComponents(self):
        self.mainFrame = Frame(self.tk,padx=5,pady=5)
        self.mainFrame.pack(fill=Y)

        #classifierChooser
        self.labelFrame_1 = LabelFrame(self.mainFrame,text="Select a classifier:",width=10)

        self.selectedClassifier = IntVar()
        R1 = Radiobutton(self.labelFrame_1, text="SVM", variable=self.selectedClassifier, value=1, command=self.onChoseClassifier)
        R1.grid(row=0,column=0)

        R2 = Radiobutton(self.labelFrame_1, text="Word2vec", variable=self.selectedClassifier, value=2, command=self.onChoseClassifier)
        R2.grid(row=0,column=1)

        R3 = Radiobutton(self.labelFrame_1, text="Neural networks", variable=self.selectedClassifier, value=3, command=self.onChoseClassifier)
        R3.grid(row=0,column=2)

        self.labelFrame_1.pack(anchor=W,fill=X)

        #classifierOptions
        self.labelFrame_2 = LabelFrame(self.mainFrame,text="Classifier options:")

        self.label_1 = Label(self.labelFrame_2)
        self.label_1.pack(anchor=W)

        self.labelFrame_2.pack(anchor=W,fill=X)

        #document for classification
        self.labelFrame_3 = LabelFrame(self.mainFrame,text="Document for classification:",padx=5,pady=5)
        self.textField_1 = Text(self.labelFrame_3,width=70,height=30)
        self.textField_1.pack(anchor=W,fill=X)
        self.labelFrame_3.pack(anchor=W,fill=X)

        self.classifyButton = Button(self.mainFrame,text='Classify')
        self.classifyButton.pack(anchor=SE)

        #svm parameters
        self.svmParametersFrame = Frame(self.labelFrame_2)

        self.svmCountOfLayersLabel = Label(self.svmParametersFrame,text="Count of features")
        self.svmCountOfLayersLabel.grid(row=0,column=0)
        self.svmCountOfLayers = Spinbox(self.svmParametersFrame,width=5,from_=1,to=10)
        self.svmCountOfLayers.grid(row=0,column=1)

        self.svmCountOfLayersLabel = Label(self.svmParametersFrame,text="Count of layers")
        self.svmCountOfLayersLabel.grid(row=0,column=2)
        self.svmCountOfLayers = Spinbox(self.svmParametersFrame,width=5,from_=1,to=10)
        self.svmCountOfLayers.grid(row=0,column=3)


    def onChoseClassifier(self):
        selection = "Radiobutton value: " + str(self.selectedClassifier.get())
        if self.selectedClassifier.get() is 1:
            self.svmParametersFrame.pack(anchor=W)
        else:
            self.svmParametersFrame.pack_forget()
        self.label_1.config(text = selection)





if __name__ == '__main__':
    mw = mainWindow()