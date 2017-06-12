from Backend.Integration.ClassificatorsProvider import ClassificatorsProvider
from Backend.SVM.SVM import SVM
from Backend.NeutralNetwork.NeuralNetwork import NeuralNetwork
from Backend.Word2Vec.Doc2Vec import Doc2Vec
from .ClassificatorEnum import ClassificatorEnum


# type:
#     1 = NN
#     2 = W2V
#     3 = SVM
class ClassifierManager:
    def __init__(self):
        self.clsEnum = ClassificatorEnum
        self.clsProv = ClassificatorsProvider()
        self.nnClassifier = NeuralNetwork()
        self.svmClassifier = SVM()
        self.w2vClassifier = Doc2Vec()
        ##wczytanie listy plikow, sprawdzenie czy istnieje dany klasyfikator

    def train(self, fromfile, input, args, output, type):
        if type == self.clsEnum.NeuralNetwork:
            self.nnClassifier.Train(fromfile, input, args, output)
        elif type == self.clsEnum.Word2Vec:
            self.w2vClassifier.train(fromfile, input, args, output)
        elif type == self.clsEnum.SVM:
            self.svmClassifier.train(fromfile, input, args, output)

    def test(self, fromfile, input, args, name, type):
        if type == self.clsEnum.NeuralNetwork:
            self.nnClassifier.Test(fromfile, input, args, name)
        elif type == self.clsEnum.Word2Vec:
            self.w2vClassifier.test(fromfile, input, args, name)
        elif type == self.clsEnum.SVM:
            self.svmClassifier.test(fromfile, input, args, name)
