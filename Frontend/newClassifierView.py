from tkinter import *

class newClassifierView:
    def __init__(self, tk, mv, ):
        self.mv = mv
        # self.mainFrame = Frame(tk)
        self.mainFrame = Frame(tk,padx=5,pady=5)

        #backButton
        backButton = Button(self.mainFrame, text="Back", width=5, command=self.onClickBackButton)
        backButton.pack(anchor=NW)

        self.initComponents()

    def show(self):
        self.mainFrame.pack(fill=X)

    def hide(self):
        self.mainFrame.pack_forget()

    def onClickBackButton(self):
        self.hide()
        self.mv.show()

    def initComponents(self):

        # self.mainFrame.pack(fill=Y)

        self.topFrame = Frame(self.mainFrame)
        self.topFrame.pack(fill=X)
        #classifiername
        classifierNameFrame = Frame(self.topFrame)
        self.classifierNameLabel = Label(classifierNameFrame, text="Classifier name")
        self.classifierNameLabel.pack(side=LEFT)
        self.classifierNameEntry = Entry(classifierNameFrame)
        classifierNameFrame.pack(anchor=W)

        self.classifierNameEntry.pack(side = RIGHT)

        #classifierChooser
        self.labelFrame_1 = LabelFrame(self.topFrame,text="Select a classifier:",width=200)

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
        self.classifierOptionsFrame = LabelFrame(self.topFrame,text="Classifier options:")
        self.classifierOptionsFrame.pack(anchor=W,fill=X)

        #documents for training
        self.labelFrame_3 = LabelFrame(self.topFrame,text="Documents for training:",padx=5,pady=5)
        self.from_file = BooleanVar()
        self.checkboxDocumentsForTraining = Checkbutton(self.labelFrame_3, offvalue=False, onvalue=True, text="from file", var=self.from_file)
        self.checkboxDocumentsForTraining.pack(side=LEFT)
        self.entryDocumentsForTraining = Entry(self.labelFrame_3, width=30)
        self.entryDocumentsForTraining.pack(side=LEFT)
        self.labelFrame_3.pack(anchor=W,fill=X)

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
            self.classifierOptionsFrame.pack_forget()
            # self.w2v_classifier.showParameters()
        else:
            self.classifierOptionsFrame.pack(anchor=W,fill=X)
            # self.w2v_classifier.hideParameters()

        if self.selectedClassifier.get() is 1:
            self.svm_classifier.showParameters()
        else:
            self.svm_classifier.hideParameters()

    def onClickClassify(self):
        args = {}
        if self.selectedClassifier.get() == "SVM":
            args = self.svm_classifier.getArgs()
        elif self.selectedClassifier.get() == "Word2vec":
            args = self.w2v_classifier.getArgs()
        elif self.selectedClassifier.get() == "Neural networks":
            args = self.nn_classifier.getArgs()
        from_file = self.from_file.get()
        input = self.entryDocumentsForTraining.get()
        args = self.getArgs();
        output = self.classifierNameEntry.get()




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
        self.NeuralNetworkStepLabel = Label(parameter3Frame,text="Neural network step: ")
        self.NeuralNetworkStepLabel.pack(side=LEFT)
        self.NeuralNetworkStep= Spinbox(parameter3Frame,width=5,from_=1,to=5000)
        self.NeuralNetworkStep.pack(side=LEFT)
        parameter3Frame.pack(anchor=W)

        parameter4Frame = Frame(self.parametersFrame)
        self.TrainStepLabel = Label(parameter4Frame,text="Train step: ")
        self.TrainStepLabel.pack(side=LEFT)
        self.TrainStep = Spinbox(parameter4Frame,width=5,from_=1,to=5000)
        self.TrainStep.pack(side=LEFT)
        parameter4Frame.pack(anchor=W)

    def showParameters(self):
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def getArgs(self):
        args = {"Count_of_features": self.CountOfFeatures.get(),
                "Vocabulary": self.varParameter2.get(),
                "Neural_network_step":self.NeuralNetworkStep.get(),
                "Train_step":self.TrainStep.get()}
        return args

class SVMClassifier:
    def __init__(self,frame):
        self.parametersFrame = Frame(frame)

        parameter1Frame = Frame(self.parametersFrame)
        self.cLabel = Label(parameter1Frame,text="C: ")
        self.cLabel.pack(side=LEFT)
        varC = DoubleVar()
        varC.set(1.0)
        self.c = Spinbox(parameter1Frame,width=5,from_=0,to=5000,increment=0.1, format="%.1f", textvariable=varC)
        self.c.pack(side=LEFT)
        parameter1Frame.pack(anchor=W)

        parameter2Frame = Frame(self.parametersFrame)
        self.varKernel = StringVar()
        self.varKernel.set("rbf")
        self.kernelLabel = Label(parameter2Frame ,text="kernel:")
        self.kernelLabel.pack(side=LEFT)
        self.kernelR1 = Radiobutton(parameter2Frame ,text="rbf", variable=self.varKernel, value="rbf", command=self.parametersForRbf)
        self.kernelR1.pack(side=LEFT)
        self.kernelR2 = Radiobutton(parameter2Frame ,text="sigmoid", variable=self.varKernel, value="sigmoid", command=self.parametersForSigmoid)
        self.kernelR2.pack(side=LEFT)
        self.kernelR3 = Radiobutton(parameter2Frame ,text="linear", variable=self.varKernel, value="linear", command=self.parametersForLinear)
        self.kernelR3.pack(side=LEFT)
        self.kernelR3 = Radiobutton(parameter2Frame ,text="poly", variable=self.varKernel, value="poly", command=self.parametersForPoly)
        self.kernelR3.pack(side=LEFT)
        parameter2Frame.pack(anchor=W)

        self.parameter3Frame = Frame(self.parametersFrame)
        self.degreeLabel = Label(self.parameter3Frame,text="degree: ")
        self.degreeLabel.pack(side=LEFT)
        self.degree = Spinbox(self.parameter3Frame,width=5,from_=0,to=5000)
        self.degree.pack(side=LEFT)
        # parameter3Frame.pack(anchor=W)

        self.parameter4Frame = Frame(self.parametersFrame)
        self.gammaLabel = Label(self.parameter4Frame,text="gamma: ")
        self.gammaLabel.pack(side=LEFT)
        self.varGamma = StringVar()
        self.gamma = Spinbox(self.parameter4Frame,width=5,from_=0,to=5000, increment=0.1, format="%.1f", textvariable=self.varGamma)
        # self.gamma.pack(side=LEFT)
        self.varGamma.set("true")
        self.gammaAuto = Checkbutton(self.parameter4Frame ,text="auto", variable=self.varGamma, onvalue="true", offvalue="false", command=self.onCheckGammaAuto)
        self.gammaAuto.pack(side=LEFT)
        self.parameter4Frame.pack(anchor=W)

        self.parameter5Frame = Frame(self.parametersFrame)
        self.coef0Label = Label(self.parameter5Frame,text="coef0: ")
        self.coef0Label.pack(side=LEFT)
        self.coef0 = Spinbox(self.parameter5Frame,width=5,from_=0.0,to=5000.0, increment=0.1, format="%.1f")
        self.coef0.pack(side=LEFT)
        # parameter5Frame.pack(anchor=W)

        parameter6Frame = Frame(self.parametersFrame)
        self.shrinkingLabel = Label(parameter6Frame,text="shrinking: ")
        self.shrinkingLabel.pack(side=LEFT)
        self.shrinking = Spinbox(parameter6Frame,width=5,values=("true","false"))
        self.shrinking.pack(side=LEFT)
        parameter6Frame.pack(anchor=W)

        parameter7Frame = Frame(self.parametersFrame)
        self.tolLabel = Label(parameter7Frame,text="tol: ")
        self.tolLabel.pack(side=LEFT)
        varTol = DoubleVar()
        varTol.set(1.0)
        self.tol = Spinbox(parameter7Frame,width=5, increment=0.1, format="%.1f", textvariable=varTol)
        self.tol.pack(side=LEFT)
        parameter7Frame.pack(anchor=W)

        parameter8Frame = Frame(self.parametersFrame)
        self.max_iterLabel = Label(parameter8Frame,text="max_iter: ")
        self.max_iterLabel.pack(side=LEFT)
        self.max_iter = Spinbox(parameter8Frame,width=5,from_=-1,to=5000)
        self.max_iter.pack(side=LEFT)
        parameter8Frame.pack(anchor=W)

    def hideKernelParameters(self):
        self.parameter3Frame.pack_forget()
        self.parameter4Frame.pack_forget()
        self.parameter5Frame.pack_forget()

    def parametersForRbf(self):
        self.hideKernelParameters()
        self.parameter4Frame.pack(anchor=W)

    def parametersForSigmoid(self):
        self.hideKernelParameters()
        self.parameter4Frame.pack(anchor=W)
        self.parameter5Frame.pack(anchor=W)

    def parametersForLinear(self):
        self.hideKernelParameters()

    def parametersForPoly(self):
        self.hideKernelParameters()
        self.parameter3Frame.pack(anchor=W)
        self.parameter4Frame.pack(anchor=W)
        self.parameter5Frame.pack(anchor=W)

    def showParameters(self):
        self.hideParameters()
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def onCheckGammaAuto(self):
        if(self.varGamma.get() == "true"):
            self.gamma.pack_forget()
        else:
            self.varGamma.set(0.0)
            self.gamma.pack(side=LEFT)

    def getArgs(self):
        args = {"C": self.c.get(),
                "kernel": self.varKernel.get(),
                "gamma":self.gamma.get(),
                "shrinking":self.shrinking.get(),
                "tol":self.tol.get(),
                "max_iter":self.max_iter.get(),
                "coef0":self.coef0.get()}
        return args

class Word2VecClassifier:
    def __init__(self,frame):
        self.parametersFrame = Frame(frame)
        l = Label(self.parametersFrame,text="")
        l.pack()

    def showParameters(self):
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def getArgs(self):
        return {}

