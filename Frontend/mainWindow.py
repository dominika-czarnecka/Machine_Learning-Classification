from tkinter import *
import Frontend.errorWindow as error
import Frontend.progressWindow as progress
import Frontend.resultWindow as result
import Frontend.mainView as mv


class mainWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Machine Learning - Classification")

        mV = mv.mainView(self.tk)
        mV.show()
        # self.initComponents()

        # ncV = ncv.newClassifierView(self.tk, mV)
        # ncV.show()



        self.tk.mainloop()

    def initComponents(self):
        self.mainFrame = Frame(self.tk,padx=5,pady=5)
        self.mainFrame.pack(fill=Y)

        #classifierChooser
        self.labelFrame_1 = LabelFrame(self.mainFrame,text="Select a classifier:",width=10)

        self.selectedClassifier = IntVar()
        self.selectedClassifier.set(1)
        R1 = Radiobutton(self.labelFrame_1, text="SVM", variable=self.selectedClassifier, value=1, command=self.onChoseClassifier)
        R1.grid(row=0,column=0)

        R2 = Radiobutton(self.labelFrame_1, text="Word2vec", variable=self.selectedClassifier, value=2, command=self.onChoseClassifier)
        R2.grid(row=0,column=1)

        R3 = Radiobutton(self.labelFrame_1, text="Neural networks", variable=self.selectedClassifier, value=3, command=self.onChoseClassifier)
        R3.grid(row=0,column=2)

        self.labelFrame_1.pack(anchor=W,fill=X)

        #classifierOptions
        self.classifierOptionsFrame = LabelFrame(self.mainFrame,text="Classifier options:")
        self.classifierOptionsFrame.pack(anchor=W,fill=X)

        #document for classification
        self.labelFrame_3 = LabelFrame(self.mainFrame,text="Document for classification:",padx=5,pady=5)
        self.textField_1 = Text(self.labelFrame_3,width=70,height=30)
        self.textField_1.pack(anchor=W,fill=X)
        self.labelFrame_3.pack(anchor=W,fill=X)

        self.classifyButton = Button(self.mainFrame,text='Classify',command=self.onClickClassify)
        self.classifyButton.pack(anchor=SE)

        #classifiers objects
        self.nn_classifier = NeuralNetworksClassifier(self.classifierOptionsFrame)
        self.w2v_classifier = Word2VecClassifier(self.classifierOptionsFrame)
        self.svm_classifier = SVMClassifier(self.classifierOptionsFrame)


    def onChoseClassifier(self):
        if self.selectedClassifier.get() is 3:
            self.nn_classifier.showParameters()
        else:
            self.nn_classifier.hideParameters()

        if self.selectedClassifier.get() is 2:
            self.w2v_classifier.showParameters()
        else:
            self.w2v_classifier.hideParameters()

        if self.selectedClassifier.get() is 1:
            self.svm_classifier.showParameters()
        else:
            self.svm_classifier.hideParameters()

    def onClickClassify(self):
        p = progress.progressWindow()



class NeuralNetworksClassifier:
    def __init__(self,frame):
        self.parametersFrame = Frame(frame)

        parameter1Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter1Frame,text="Count of features: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter1Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter1Frame.pack(anchor=W)

        parameter2Frame = Frame(self.parametersFrame)
        self.varParameter2 = StringVar()
        self.varParameter2.set("entrophy")
        self.Parameter2Label = Label(parameter2Frame ,text="Vocabulary:")
        self.Parameter2Label.pack(side=LEFT)
        self.Parameter2R1 = Radiobutton(parameter2Frame ,text="Entrophy", variable=self.varParameter2, value="entrophy")
        self.Parameter2R1.pack(side=LEFT)
        self.Parameter2R2 = Radiobutton(parameter2Frame ,text="Frequency", variable=self.varParameter2, value="frequency")
        self.Parameter2R2.pack(side=LEFT)
        self.Parameter2R3 = Radiobutton(parameter2Frame ,text="TF-IDF", variable=self.varParameter2, value="tf_idf")
        self.Parameter2R3.pack(side=LEFT)
        parameter2Frame.pack(anchor=W)

        parameter3Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter3Frame,text="Neural network step: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter3Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter3Frame.pack(anchor=W)

        parameter4Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter4Frame,text="Train step: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter4Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter4Frame.pack(anchor=W)

    def showParameters(self):
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def execute(self):
        return

class SVMClassifier:
    def __init__(self,frame):
        self.parametersFrame = Frame(frame)
        l = Label(self.parametersFrame,text="")
        l.pack()

    def showParameters(self):
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def execute(self):
        return

class Word2VecClassifier:
    def __init__(self,frame):
        self.parametersFrame = Frame(frame)
        l = Label(self.parametersFrame,text="")
        l.pack()

    def showParameters(self):
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def execute(self):
        return


if __name__ == '__main__':
    # result.resultWindow("Result")
    mw = mainWindow()
    # error.errorWindow("Error !")







