import copy
from tkinter import *

import Frontend.errorWindow as error
from Backend.pathProvider import *
from Backend.Integration.ClassificatorEnum import ClassificatorEnum
from Backend.Integration.Models.NeuralNetworkModel import NeuralNetworkModel


# clsses for display classifiers parameters
class NeuralNetworksClassifier:
    def __init__(self, frame):
        self.parametersFrame = Frame(frame)

        self.targetFrame = Frame(self.parametersFrame)
        self.target = StringVar()
        self.target.set("entrophy")
        self.targetLabel = Label(self.targetFrame, text="Target: ")
        self.targetLabel.pack(side=LEFT)
        self.entrophy = Radiobutton(self.targetFrame, text="Entrophy", variable=self.target, value="entrophy")
        self.entrophy.pack(side=LEFT)
        self.frequency = Radiobutton(self.targetFrame, text="Frequency", variable=self.target, value="frequency")
        self.frequency.pack(side=LEFT)
        self.tf_idf = Radiobutton(self.targetFrame, text="TF-IDF", variable=self.target, value="tf_idf")
        self.tf_idf.pack(side=LEFT)
        self.targetFrame.pack(anchor=W)

        self.gradientFrame = Frame(self.parametersFrame)
        self.gradientLabel = Label(self.gradientFrame, text="Gradient: ")
        self.gradientLabel.pack(side=LEFT)
        self.defaultGradient = StringVar()
        self.defaultGradient.set(0.5)
        self.gradient = Spinbox(self.gradientFrame, width=5, from_=0, to=1, increment=0.01, format="%.2f",
                                textvariable=self.defaultGradient)
        self.gradient.pack(side=LEFT)
        self.gradientRangeLabel = Label(self.gradientFrame, text="Range (0-1)")
        self.gradientRangeLabel.pack(side=LEFT)
        self.gradientFrame.pack(anchor=W)

        self.stepsFrame = Frame(self.parametersFrame)
        self.stepsLabel = Label(self.stepsFrame, text="Step: ")
        self.stepsLabel.pack(side=LEFT)
        self.defaultsteps = StringVar()
        self.defaultsteps.set(1500)
        self.steps = Spinbox(self.stepsFrame, width=5, from_=1, to=10000, textvariable=self.defaultsteps)
        self.steps.pack(side=LEFT)
        self.stepsRangeLabel = Label(self.stepsFrame, text="Range (1-10000)")
        self.stepsRangeLabel.pack(side=LEFT)
        self.stepsFrame.pack(anchor=W)

        self.vocabularyLengthFrame = Frame(self.parametersFrame)
        self.vocabularyLengthLabel = Label(self.vocabularyLengthFrame, text="Vocabulary Len: ")
        self.vocabularyLengthLabel.pack(side=LEFT)
        self.defaultVocabularyLength = StringVar()
        self.defaultVocabularyLength.set(300)
        self.vocabularyLength = Spinbox(self.vocabularyLengthFrame, width=5, from_=1, to=5000,
                                        textvariable=self.defaultVocabularyLength)
        self.vocabularyLength.pack(side=LEFT)
        self.vocabularyLengthRangeLabel = Label(self.vocabularyLengthFrame, text="Range (1-5000)")
        self.vocabularyLengthRangeLabel.pack(side=LEFT)
        self.vocabularyLengthFrame.pack(anchor=W)

    def showParameters(self):
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def getArgs(self):
        args = {"vocabulary_len": int(self.vocabularyLength.get()),
                "target": self.target.get(),
                "steps": int(self.steps.get()),
                "gradient": float(self.gradient.get())}
        return args