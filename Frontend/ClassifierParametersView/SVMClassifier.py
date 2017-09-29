import copy
from tkinter import *

import Frontend.errorWindow as error
from Backend.pathProvider import *
from Backend.Integration.ClassificatorEnum import ClassificatorEnum
from Backend.Integration.Models.SVMModel import SVMModel

class SVMClassifier:
    def __init__(self, frame):
        self.parametersFrame = Frame(frame)

        variableCFrame = Frame(self.parametersFrame)
        self.cLabel = Label(variableCFrame, text="C: ")
        self.cLabel.pack(side=LEFT)
        varC = DoubleVar()
        varC.set(1000.0)
        self.c = Spinbox(variableCFrame, width=5, from_=0, to=5000, increment=0.1, format="%.1f", textvariable=varC)
        self.c.pack(side=LEFT)
        variableCFrame.pack(anchor=W)

        kernelFrame = Frame(self.parametersFrame)
        self.varKernel = StringVar()
        self.varKernel.set("linear")
        self.kernelLabel = Label(kernelFrame, text="kernel:")
        self.kernelLabel.pack(side=LEFT)
        self.kernelR1 = Radiobutton(kernelFrame, text="rbf", variable=self.varKernel, value="rbf",
                                    command=self.parametersForRbf)
        self.kernelR1.pack(side=LEFT)
        self.kernelR2 = Radiobutton(kernelFrame, text="sigmoid", variable=self.varKernel, value="sigmoid",
                                    command=self.parametersForSigmoid)
        self.kernelR2.pack(side=LEFT)
        self.kernelR3 = Radiobutton(kernelFrame, text="linear", variable=self.varKernel, value="linear",
                                    command=self.parametersForLinear)
        self.kernelR3.pack(side=LEFT)
        self.kernelR3 = Radiobutton(kernelFrame, text="poly", variable=self.varKernel, value="poly",
                                    command=self.parametersForPoly)
        self.kernelR3.pack(side=LEFT)
        kernelFrame.pack(anchor=W)

        self.degreeFrame = Frame(self.parametersFrame)
        self.degreeLabel = Label(self.degreeFrame, text="degree: ")
        self.degreeLabel.pack(side=LEFT)
        degreeVar = IntVar()
        degreeVar.set(1)
        self.degree = Spinbox(self.degreeFrame, width=5, from_=0, to=5000, textvariable=degreeVar)
        self.degree.pack(side=LEFT)
        self.degreeRangeLabel = Label(self.degreeFrame, text="Range (0-5000)")
        self.degreeRangeLabel.pack(side=LEFT)

        self.gammaFrame = Frame(self.parametersFrame)
        self.gammaLabel = Label(self.gammaFrame, text="gamma: ")
        self.gammaLabel.pack(side=LEFT)
        self.varGamma = StringVar()
        self.varGamma.set(1)
        self.gamma = Spinbox(self.gammaFrame, width=5, from_=0, to=5000, increment=0.1, format="%.1f",
                             textvariable=self.varGamma)
        self.varGamma.set("true")
        self.gammaAuto = Checkbutton(self.gammaFrame, text="auto", variable=self.varGamma, onvalue="true",
                                     offvalue="false", command=self.onCheckGammaAuto)
        self.gammaAuto.pack(side=LEFT)
        self.gammaFrame.pack(anchor=W)
        self.gammaRangeLabel = Label(self.gammaFrame, text="Range (0.0-5000.0)")
        self.gammaRangeLabel.pack(side=LEFT)

        self.coef0Frame = Frame(self.parametersFrame)
        self.coef0Label = Label(self.coef0Frame, text="coef0: ")
        self.coef0Label.pack(side=LEFT)
        coef0Var = DoubleVar()
        coef0Var.set(1.0)
        self.coef0 = Spinbox(self.coef0Frame, width=5, from_=0.0, to=5000.0, increment=0.1, format="%.1f",
                             textvariable=coef0Var)
        self.coef0.pack(side=LEFT)
        self.coef0RangeLabel = Label(self.coef0Frame, text="Range (0.0-5000.0)")
        self.coef0RangeLabel.pack(side=LEFT)

        self.shrinkingFrame = Frame(self.parametersFrame)
        self.shrinkingLabel = Label(self.shrinkingFrame, text="shrinking: ")
        self.shrinkingLabel.pack(side=LEFT)
        self.shrinking = Spinbox(self.shrinkingFrame, width=5, values=(True, False))
        self.shrinking.pack(side=LEFT)
        self.shrinkingFrame.pack(anchor=W)

        tolFrame = Frame(self.parametersFrame)
        self.tolLabel = Label(tolFrame, text="tol: ")
        self.tolLabel.pack(side=LEFT)
        varTol = DoubleVar()
        varTol.set(0.0001)
        self.tol = Spinbox(tolFrame, width=5, increment=0.1, format="%.1f", textvariable=varTol)
        self.tol.pack(side=LEFT)
        tolFrame.pack(anchor=W)

        maxIterFrame = Frame(self.parametersFrame)
        self.max_iterLabel = Label(maxIterFrame, text="max_iter: ")
        self.max_iterLabel.pack(side=LEFT)
        maxIterVar = IntVar()
        maxIterVar.set(-1)
        self.max_iter = Spinbox(maxIterFrame, width=5, from_=-1, to=5000, textvariable=maxIterVar)
        self.max_iter.pack(side=LEFT)
        maxIterFrame.pack(anchor=W)
        self.maxIterRangeLabel = Label(maxIterFrame, text="Range (-1 - 5000)")
        self.maxIterRangeLabel.pack(side=LEFT)

    def hideKernelParameters(self):
        self.degreeFrame.pack_forget()
        self.gammaFrame.pack_forget()
        self.coef0Frame.pack_forget()

    def parametersForRbf(self):
        self.hideKernelParameters()
        self.gammaFrame.pack(anchor=W)

    def parametersForSigmoid(self):
        self.hideKernelParameters()
        self.gammaFrame.pack(anchor=W)
        self.coef0Frame.pack(anchor=W)

    def parametersForLinear(self):
        self.hideKernelParameters()

    def parametersForPoly(self):
        self.hideKernelParameters()
        self.degreeFrame.pack(anchor=W)
        self.gammaFrame.pack(anchor=W)
        self.coef0Frame.pack(anchor=W)

    def showParameters(self):
        self.hideParameters()
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def onCheckGammaAuto(self):
        if (self.varGamma.get() == "true"):
            self.gamma.pack_forget()
        else:
            self.varGamma.set(0.0)
            self.gamma.pack(side=LEFT)

    def getArgs(self):
        shrinking = False
        if self.shrinking.get() == 'True':
            shrinking = True
        args = {"c": self.c.get(),
                "kernel": self.varKernel.get(),
                "degree": self.degree.get(),
                "gamma": self.gamma.get(),
                "shrinking": shrinking,
                "tol": self.tol.get(),
                "max_iter": self.max_iter.get(),
                "coef0":self.coef0.get()}
        return args
