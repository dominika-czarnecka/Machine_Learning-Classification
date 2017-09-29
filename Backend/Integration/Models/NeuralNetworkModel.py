from Backend.Integration.Models.ClassificatorModel import ClassificatorModel


class NeuralNetworkModel(ClassificatorModel):

    def __init__(self, name, path, gradient, steps, target, vocabulary_len):
        self.name = name
        self.path = path
        self.gradient = gradient
        self.steps = steps
        self.target = target
        self.vocabulary_len = vocabulary_len

    def display(self):
        return 'name: {}\n' \
               'path: {}\n' \
               'gradient: {}\n' \
               'steps: {}\n' \
               'target: {}\n' \
               'vocabulary len: {}\n'.format(self.name, self.path, self.gradient, self.steps, self.target, self.vocabulary_len)


    @classmethod
    def fromJSON(cls, json_data):
        fromJSON = cls(json_data['name'], json_data['path'], json_data['gradient'], json_data['steps'], json_data['target'], json_data['vocabulary_len'])
        return fromJSON
