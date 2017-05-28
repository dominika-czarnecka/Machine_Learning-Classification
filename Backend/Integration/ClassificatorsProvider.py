import json
import os
from Backend.Integration.ClassificatorEnum import ClassificatorEnum
from Backend.Integration.Models.NeuralNetworkModel import NeuralNetworkModel
from Backend.Integration.Models.SVMModel import SVMModel
from Backend.Integration.Models.Word2VecModel import Word2VecModel


class ClassificatorsProvider:
    def __init__(self):
        self.SVMModels = []
        self.NeuralNetworkModels = []
        self.Word2VecModels = []
        self.fromFile()

    def __del__(self):
        self.toFile()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def toFile(self):
        with open('data.json', 'w') as outfile:
            json.dump(self.toJSON(), outfile)

    def fromFile(self):
        if not os.path.isfile('data.json'):
            return
        with open('data.json') as data_file:
            temp = json.load(data_file)
            data = json.loads(temp)
            self.SVMModels = data['SVMModels']
            self.NeuralNetworkModels = data['NeuralNetworkModels']
            self.Word2VecModels = data['Word2VecModels']

    def canAdd(self, classificatorType, classificator):
        if classificatorType == ClassificatorEnum.NeuralNetwork:
            for i in self.NeuralNetworkModels:
                temp = NeuralNetworkModel()
                temp.fromJSON(i)
                if classificator == temp:
                    return False
            return True
        elif classificatorType == ClassificatorEnum.SVM:
            for i in self.SVMModels:
                temp = SVMModel()
                temp.fromJSON(i)
                if classificator == temp:
                    return False
            return True
        elif classificatorType == ClassificatorEnum.Word2Vec:
            for i in self.Word2VecModels:
                temp = Word2VecModel()
                temp.fromJSON(i)
                if classificator == temp:
                    return False
            return True
        else:
            return False

# example
# svm = SVMModel()
# svm.initValues(name="test", path="ad", c=1.0, kernel="linear", degree=3, gamma="auto", coef0=0.0, shrinking=True,
#                probability=False, tol=1e-3, cache_size=200.0, verbose=False, max_iter=-1,
#                decision_function_shape="None", random_state=0)
# svm1 = SVMModel()
# svm1.initValues(name="test1", path="ad", c=1.0, kernel="linear", degree=3, gamma="auto", coef0=0.0, shrinking=True,
#                 probability=False, tol=1e-3, cache_size=200.0, verbose=False, max_iter=-1,
#                 decision_function_shape="None", random_state=0)
#
# nn = NeuralNetworkModel()
# nn.initValues(name="test", path="ad", gradient=1, steps=500, target="tf_idf", vocabulary_len=1500)
# cp = ClassificatorsProvider()
# if cp.canAdd(ClassificatorEnum.SVM, svm1):
#     cp.SVMModels.append(svm1)
# del cp