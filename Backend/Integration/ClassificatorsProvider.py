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

    def find(self, name):
        for i in self.SVMModels:
            if i.name == name:
                return i
        for i in self.NeuralNetworkModels:
            if i.name == name:
                return i
        for i in self.Word2VecModels:
            if i.name == name:
                return i
        return False

    def remove(self, classificatorType, classificator):
        if classificatorType == ClassificatorEnum.NeuralNetwork:
            self.NeuralNetworkModels.remove(classificator)
        elif classificatorType == ClassificatorEnum.SVM:
            self.SVMModels.remove(classificator)
        elif classificatorType == ClassificatorEnum.Word2Vec:
            self.Word2VecModels.remove(classificator)

# example
svm = SVMModel.initValues(name="test", path="ad", c=1.0, kernel="linear", degree=3, gamma="auto", coef0=0.0, shrinking=True,
               probability=False, tol=1e-4, cache_size=200.0, verbose=False, max_iter=-1,
               decision_function_shape="None", random_state=0)
print(svm)

cp = ClassificatorsProvider()
print(cp.SVMModels)
# cp.remove(classificatorType=ClassificatorEnum.SVM, classificator=svm)
# print(cp.SVMModels)
# cp.SVMModels.append(svm)
print(cp.SVMModels)
del cp

