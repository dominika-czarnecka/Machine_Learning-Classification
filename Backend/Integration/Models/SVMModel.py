from Backend.Integration.Models.ClassificatorModel import ClassificatorModel


class SVMModel(ClassificatorModel):
    def __init__(self, name, path, c, kernel, degree, gamma, coef0, shrinking, probability, tol, cache_size, verbose,
                   max_iter, decision_function_shape, random_state):
        self.name = name
        self.path = path
        self.c = c
        self.kernel = kernel
        self.degree = degree
        self.gamma = gamma
        self.coef0 = coef0
        self.shrinking = shrinking
        self.probability = probability
        self.tol = tol
        self.cache_size = cache_size
        self.verbose = verbose
        self.max_iter = max_iter
        self.decision_function_shape = decision_function_shape
        self.random_state = random_state

    def display(self):
        return "name: " + self.name + "\npath: " + self.path

    @classmethod
    def fromJSON(cls, json_data):
        fromJSON = cls(json_data['name'], json_data['path'], json_data['c'],json_data['kernel'], json_data['degree'],
        json_data['gamma'], json_data['coef0'], json_data['shrinking'], json_data['probability'], json_data['tol'],
        json_data['cache_size'], json_data['verbose'], json_data['max_iter'], json_data['decision_function_shape'],
        json_data['random_state'])
        return fromJSON