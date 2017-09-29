import copy
from tkinter import *

import Frontend.errorWindow as error
from Backend.pathProvider import *
from Backend.Integration.ClassificatorEnum import ClassificatorEnum
from Backend.Integration.Models.NeuralNetworkModel import NeuralNetworkModel
from Backend.Integration.Models.SVMModel import SVMModel
from Backend.Integration.Models.Word2VecModel import Word2VecModel
from Frontend.ClassifierParametersView.NeuralNetworkClassifier import NeuralNetworksClassifier
from Frontend.ClassifierParametersView.SVMClassifier import SVMClassifier
from Frontend.ClassifierParametersView.Word2VecClassifier import Word2VecClassifier


class newClassifierView:
    def __init__(self, tk, mv):
        self.mv = mv
        self.mainFrame = Frame(tk, padx=5, pady=5)
        # backButton
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
        self.mv.cp.toFile()

    def initComponents(self):
        self.topFrame = Frame(self.mainFrame)
        self.topFrame.pack(fill=X)
        # classifiername
        classifierNameFrame = Frame(self.topFrame)
        self.classifierNameLabel = Label(classifierNameFrame, text="Classifier name")
        self.classifierNameLabel.pack(side=LEFT)
        self.classifierNameEntry = Entry(classifierNameFrame)
        classifierNameFrame.pack(anchor=W)

        self.classifierNameEntry.pack(side=RIGHT)

        # classifierChooser
        self.labelFrame_1 = LabelFrame(self.topFrame, text="Select a classifier:", width=200)

        self.selectedClassifier = IntVar()
        self.selectedClassifier.set(1)
        R1 = Radiobutton(self.labelFrame_1, text="SVM", variable=self.selectedClassifier, value=1,
                         command=self.onChoseClassifier)
        R1.grid(row=0, column=0)

        R2 = Radiobutton(self.labelFrame_1, text="Word2vec", variable=self.selectedClassifier, value=2,
                         command=self.onChoseClassifier)
        R2.grid(row=0, column=1)

        R3 = Radiobutton(self.labelFrame_1, text="Neural networks", variable=self.selectedClassifier, value=3,
                         command=self.onChoseClassifier)
        R3.grid(row=0, column=2)

        self.labelFrame_1.pack(anchor=W, fill=X)

        # classifierOptions
        self.classifierOptionsFrame = LabelFrame(self.topFrame, text="Classifier options:")
        self.classifierOptionsFrame.pack(anchor=W, fill=X)

        # documents for training
        # self.labelFrame_3 = LabelFrame(self.topFrame,text="Documents for training:",padx=5,pady=5)
        # self.from_file = BooleanVar()
        # self.checkboxDocumentsForTraining = Checkbutton(self.labelFrame_3, offvalue=False, onvalue=True, text="from file", var=self.from_file)
        # self.checkboxDocumentsForTraining.pack(side=LEFT)
        # self.entryDocumentsForTraining = Entry(self.labelFrame_3, width=30)
        # self.entryDocumentsForTraining.pack(side=LEFT)
        # self.labelFrame_3.pack(anchor=W,fill=X)

        self.classifyButton = Button(self.mainFrame, text='Train classifier', command=self.onClickClassify)
        self.classifyButton.pack(anchor=SE)

        # classifiers objects
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
        args = {}
        type = ClassificatorEnum.SVM
        classificator = None
        if self.selectedClassifier.get() == 1:
            args = self.svm_classifier.getArgs()
            type = ClassificatorEnum.SVM
        elif self.selectedClassifier.get() == 2:
            args = self.w2v_classifier.getArgs()
            type = ClassificatorEnum.Word2Vec
        elif self.selectedClassifier.get() == 3:
            args = self.nn_classifier.getArgs()
            type = ClassificatorEnum.NeuralNetwork
        fromfile = False
        input = 'reuters'
        output = self.classifierNameEntry.get()

        if len(output) == 0:
            error.errorWindow("Please enter classificator name !")
            return

        tempArgs = copy.copy(args)
        tempArgs['name'] = output
        tempArgs['path'] = getPathToModels(output)

        if type == ClassificatorEnum.SVM:
            temp = SVMModel.fromJSON(tempArgs)
        elif type == ClassificatorEnum.Word2Vec:
            temp = Word2VecModel.fromJSON(tempArgs)
        elif type == ClassificatorEnum.NeuralNetwork:
            temp = NeuralNetworkModel.fromJSON(tempArgs)

        if self.mv.cp.add(classificatorType=type, classificator=temp):
            self.mv.classifierManager.train(fromfile, input, args, output, type)
        else:
            error.errorWindow("Couldn't create classificator!")
