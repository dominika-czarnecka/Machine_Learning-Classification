from Backend.Integration.Models.ClassificatorModel import ClassificatorModel


class NeuralNetworkModel(ClassificatorModel):
    def initValues(self, name, path, gradient, steps, target, vocabulary_len):
        self.name = name
        self.path = path
        self.gradient = gradient
        self.steps = steps
        self.target = target
        self.vocabulary_len = vocabulary_len


    def fromJSON(self, json_data):
        self.name = json_data['name']
        self.path = json_data['path']
        self.gradient = json_data['gradient']
        self.steps = json_data['steps']
        self.target = json_data['target']
        self.vocabulary_len = json_data['vocabulary_len']
