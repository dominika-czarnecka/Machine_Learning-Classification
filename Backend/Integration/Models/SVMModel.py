from Backend.Integration.Models.ClassificatorModel import ClassificatorModel


class SVMModel(ClassificatorModel):
    def initValues(self, name, path, c, kernel, degree, gamma, coef0, shrinking, probability, tol, cache_size, verbose,
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

    def fromJSON(self, json_data):
        self.name = json_data['name']
        self.path = json_data['path']
        self.c = json_data['c']
        self.kernel = json_data['kernel']
        self.degree = json_data['degree']
        self.gamma = json_data['gamma']
        self.coef0 = json_data['coef0']
        self.shrinking = json_data['shrinking']
        self.probability = json_data['probability']
        self.tol = json_data['tol']
        self.cache_size = json_data['cache_size']
        self.verbose = json_data['verbose']
        self.max_iter = json_data['max_iter']
        self.decision_function_shape = json_data['decision_function_shape']
        self.random_state = json_data['random_state']
