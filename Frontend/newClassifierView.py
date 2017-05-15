from tkinter import *

class newClassifierView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.mainFrame = Frame(tk)
        self.mainFrame = Frame(tk,padx=5,pady=5)

        #backButton
        backButton = Button(self.mainFrame, text="Back", width=5, command=self.onClickBackButton)
        backButton.pack(anchor=NW)

        self.initComponents()

    def show(self):
        self.mainFrame.pack()

    def hide(self):
        self.mainFrame.pack_forget()

    def onClickBackButton(self):
        self.hide()
        self.mv.show()

    def initComponents(self):

        # self.mainFrame.pack(fill=Y)

        #classifiername
        classifierNameFrame = Frame(self.mainFrame)
        self.classifierNameLabel = Label(classifierNameFrame, text="Classifier name")
        self.classifierNameLabel.pack(side=LEFT)
        self.classifierNameEntry = Entry(classifierNameFrame)
        classifierNameFrame.pack(anchor=W)

        self.classifierNameEntry.pack(side = RIGHT)

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
        # self.labelFrame_3 = LabelFrame(self.mainFrame,text="Document for classification:",padx=5,pady=5)
        # self.textField_1 = Text(self.labelFrame_3,width=70,height=30)
        # self.textField_1.pack(anchor=W,fill=X)
        # self.labelFrame_3.pack(anchor=W,fill=X)

        self.classifyButton = Button(self.mainFrame,text='Train classifier',command=self.onClickClassify)
        self.classifyButton.pack(anchor=SE)

        #classifiers objects
        self.nn_classifier = NeuralNetworksClassifier(self.classifierOptionsFrame)
        self.w2v_classifier = Word2VecClassifier(self.classifierOptionsFrame)
        self.svm_classifier = SVMClassifier(self.classifierOptionsFrame)

        self.svm_classifier.showParameters()

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
        # p = progress.progressWindow()
        return



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

        parameter1Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter1Frame,text="C: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter1Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter1Frame.pack(anchor=W)

        parameter2Frame = Frame(self.parametersFrame)
        self.varParameter2 = StringVar()
        self.varParameter2.set("entrophy")
        self.Parameter2Label = Label(parameter2Frame ,text="kernel:")
        self.Parameter2Label.pack(side=LEFT)
        self.Parameter2R1 = Radiobutton(parameter2Frame ,text="Entrophy", variable=self.varParameter2, value="entrophy")
        self.Parameter2R1.pack(side=LEFT)
        self.Parameter2R2 = Radiobutton(parameter2Frame ,text="Frequency", variable=self.varParameter2, value="frequency")
        self.Parameter2R2.pack(side=LEFT)
        self.Parameter2R3 = Radiobutton(parameter2Frame ,text="TF-IDF", variable=self.varParameter2, value="tf_idf")
        self.Parameter2R3.pack(side=LEFT)
        parameter2Frame.pack(anchor=W)

        parameter3Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter3Frame,text="degree: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter3Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter3Frame.pack(anchor=W)

        parameter4Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter4Frame,text="gamma: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter4Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter4Frame.pack(anchor=W)

        parameter5Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter5Frame,text="coef0: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter5Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter5Frame.pack(anchor=W)

        parameter6Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter6Frame,text="shrinking: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter6Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter6Frame.pack(anchor=W)

        parameter7Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter7Frame,text="probability: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter7Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter7Frame.pack(anchor=W)

        parameter8Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter8Frame,text="tol: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter8Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter8Frame.pack(anchor=W)

        parameter9Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter9Frame,text="cache_size: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter9Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter9Frame.pack(anchor=W)

        parameter10Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter10Frame,text="class_weight: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter10Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter10Frame.pack(anchor=W)

        parameter11Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter11Frame,text="verbose: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter11Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter11Frame.pack(anchor=W)

        parameter12Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter12Frame,text="max_iter: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter12Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter12Frame.pack(anchor=W)

        parameter13Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter13Frame,text="decision_function_shape: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter13Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter13Frame.pack(anchor=W)

        parameter14Frame = Frame(self.parametersFrame)
        self.CountOfFeaturesLabel = Label(parameter14Frame,text="random_state: ")
        self.CountOfFeaturesLabel.pack(side=LEFT)
        self.CountOfFeatures = Spinbox(parameter14Frame,width=5,from_=1,to=5000)
        self.CountOfFeatures.pack(side=LEFT)
        parameter14Frame.pack(anchor=W)

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

