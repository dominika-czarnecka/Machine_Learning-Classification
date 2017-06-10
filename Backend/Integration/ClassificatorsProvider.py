import json
import os
from Backend.Integration.ClassificatorEnum import ClassificatorEnum
from Backend.Integration.Models.NeuralNetworkModel import NeuralNetworkModel
from Backend.Integration.Models.SVMModel import SVMModel
from Backend.Integration.Models.Word2VecModel import Word2VecModel


class ClassificatorsProvider:
    package_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(package_dir, 'data.json')

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
        with open(self.file, 'w') as outfile:
            json.dump(self.toJSON(), outfile)

    def fromFile(self):
        if not os.path.isfile(self.file):
            return
        with open(self.file) as data_file:
            temp = json.load(data_file)
            data = json.loads(temp)
            for i in data['SVMModels']:
                self.SVMModels.append(SVMModel.fromJSON(json_data=i))
            for i in data['NeuralNetworkModels']:
                self.NeuralNetworkModels.append(SVMModel.fromJSON(json_data=i))
            for i in data['Word2VecModels']:
                self.Word2VecModels.append(SVMModel.fromJSON(json_data=i))

    def canAdd(self, classificatorType, classificator):
        if self.exist(classificator.name):
            return False

        if classificatorType == ClassificatorEnum.NeuralNetwork:
            for i in self.NeuralNetworkModels:
                if classificator == i:
                    return False
            return True
        elif classificatorType == ClassificatorEnum.SVM:
            for i in self.SVMModels:
                if classificator == i:
                    return False
            return True
        elif classificatorType == ClassificatorEnum.Word2Vec:
            for i in self.Word2VecModels:
                if classificator == i:
                    return False
            return True
        else:
            return False

    def add(self, classificatorType, classificator):
        if not self.canAdd(classificatorType=classificatorType, classificator=classificator):
            return False
        if classificatorType == ClassificatorEnum.NeuralNetwork:
            self.NeuralNetworkModels.append(classificator)
            return True
        elif classificatorType == ClassificatorEnum.SVM:
            self.SVMModels.append(classificator)
            return True
        elif classificatorType == ClassificatorEnum.Word2Vec:
            self.Word2VecModels.append(classificator)
            return True

    def exist(self, name):
        for i in self.SVMModels:
            if i.name == name:
                return True
        for i in self.NeuralNetworkModels:
            if i.name == name:
                return True
        for i in self.Word2VecModels:
            if i.name == name:
                return True
        return False

    def find(self, name):
        if not self.exist(name):
            return False
        for i in self.SVMModels:
            if i.name == name:
                return ClassificatorEnum.SVM, i
        for i in self.NeuralNetworkModels:
            if i.name == name:
                return ClassificatorEnum.NeuralNetwork, i
        for i in self.Word2VecModels:
            if i.name == name:
                return ClassificatorEnum.Word2Vec, i

    def remove(self, classificatorType, classificator):
        if not self.exist(name=classificator.name):
            return False
        if classificatorType == ClassificatorEnum.NeuralNetwork:
            self.NeuralNetworkModels.remove(classificator)
            return True
        elif classificatorType == ClassificatorEnum.SVM:
            self.SVMModels.remove(classificator)
            return True
        elif classificatorType == ClassificatorEnum.Word2Vec:
            self.Word2VecModels.remove(classificator)
        return True

# example
# svm = SVMModel(name="test", path="ad", c=1.0, kernel="linear", degree=3, gamma="auto", coef0=0.0, shrinking=True,
#                probability=False, tol=1e-4, cache_size=200.0, verbose=False, max_iter=-1,
#                decision_function_shape="None", random_state=0)
# svm1 = SVMModel(name="test1", path="ad", c=1.0, kernel="linear", degree=31, gamma="auto", coef0=0.0, shrinking=True,
#                probability=False, tol=1e-4, cache_size=200.0, verbose=False, max_iter=-1,
#                decision_function_shape="None", random_state=0)
# print(svm)

# cp = ClassificatorsProvider()
# print(cp.SVMModels)
# print(cp.add(classificatorType=ClassificatorEnum.SVM, classificator=svm))
# print(cp.add(classificatorType=ClassificatorEnum.SVM, classificator=svm1))
# print(cp.remove(classificatorType=ClassificatorEnum.SVM, classificator=svm))
# print(cp.remove(classificatorType=ClassificatorEnum.SVM, classificator=svm))
# print(cp.add(classificatorType=ClassificatorEnum.SVM, classificator=svm))
# type, c = cp.find(name='test')
# c.path = '112test'
# del cp
# cp = ClassificatorsProvider()
# type, c = cp.find(name='test')
# print(c.path)
# del cp

