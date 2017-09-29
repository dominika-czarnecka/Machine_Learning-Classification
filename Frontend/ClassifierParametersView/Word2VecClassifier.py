import copy
from tkinter import *

import Frontend.errorWindow as error
from Backend.pathProvider import *
from Backend.Integration.ClassificatorEnum import ClassificatorEnum
from Backend.Integration.Models.Word2VecModel import Word2VecModel

class Word2VecClassifier:
    def __init__(self,frame):
        self.parametersFrame = Frame(frame)

        sizeFrame = Frame(self.parametersFrame)
        sizeLabel = Label(sizeFrame,text="Size: ")
        sizeLabel.pack(side=LEFT)
        self.varSize = StringVar()
        size = Spinbox(sizeFrame,width=5,from_=0,to=5000, textvariable=self.varSize)
        self.varSize.set(100)
        size.pack(side=LEFT)
        sizeRangeLabel = Label(sizeFrame, text="Range (1-5000)")
        sizeRangeLabel.pack(side=LEFT)
        sizeFrame.pack(anchor=W)

        iterFrame = Frame(self.parametersFrame)
        iterLabel = Label(iterFrame,text="Iter: ")
        iterLabel.pack(side=LEFT)
        self.varIter = StringVar()
        iter = Spinbox(iterFrame,width=5,from_=0,to=5000, textvariable=self.varIter)
        self.varIter.set(55)
        iter.pack(side=LEFT)
        iterRangeLabel = Label(iterFrame, text="Range (1-5000)")
        iterRangeLabel.pack(side=LEFT)
        iterFrame.pack(anchor=W)

        min_countFrame = Frame(self.parametersFrame)
        min_countLabel = Label(min_countFrame,text="Min-count: ")
        min_countLabel.pack(side=LEFT)
        self.varMin_count = StringVar()
        min_count = Spinbox(min_countFrame,width=5,from_=0,to=5000, textvariable=self.varMin_count)
        self.varMin_count.set(6)
        min_count.pack(side=LEFT)
        min_countRangeLabel = Label(min_countFrame, text="Range (1-5000)")
        min_countRangeLabel.pack(side=LEFT)
        min_countFrame.pack(anchor=W)

        windowFrame = Frame(self.parametersFrame)
        windowLabel = Label(windowFrame,text="Window: ")
        windowLabel.pack(side=LEFT)
        self.varWindow = StringVar()
        window = Spinbox(windowFrame,width=5, from_=0,to=5000, textvariable=self.varWindow)
        self.varWindow.set(1)
        window.pack(side=LEFT)
        windowRangeLabel = Label(windowFrame, text="Range (1-5000)")
        windowRangeLabel.pack(side=LEFT)
        windowFrame.pack(anchor=W)

    def showParameters(self):
        self.parametersFrame.pack(anchor=W)

    def hideParameters(self):
        self.parametersFrame.pack_forget()

    def getArgs(self):
        args = {"size": int(self.varSize.get()),
                "iter": int(self.varIter.get()),
                "min-count": int(self.varMin_count.get()),
                "window": int(self.varWindow.get())}
        return args

