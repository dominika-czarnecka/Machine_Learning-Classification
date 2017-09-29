from Backend.Integration.Models.ClassificatorModel import ClassificatorModel


class SVMModel(ClassificatorModel):
    def __init__(self, name, path, c, kernel, degree, gamma, coef0, shrinking, tol, max_iter):
        self.name = name
        self.path = path
        self.c = c
        self.kernel = kernel
        self.degree = degree
        self.gamma = gamma
        self.coef0 = coef0
        self.shrinking = shrinking
        self.tol = tol
        self.max_iter = max_iter

    def display(self):
        return "name: {}\n" \
               "path: {}\n" \
               "c: {}\n" \
               "kernel: {}\n" \
               "degree: {}\n" \
               "gamma: {}\n" \
               "coef0: {}\n" \
               "shrinking: {}\n" \
               "tol: {}\n" \
               "max iter: {}\n".format(self.name, self.path, self.c, self.kernel, self.degree, self.gamma,
                                       self.coef0, self.shrinking, self.tol, self.max_iter)

    @classmethod
    def fromJSON(cls, json_data):
        fromJSON = cls(json_data['name'],
                       json_data['path'],
                       json_data['c'],
                       json_data['kernel'],
                       json_data['degree'],
                       json_data['gamma'],
                       json_data['coef0'],
                       json_data['shrinking'],
                       json_data['tol'],
                       json_data['max_iter'])
        return fromJSON
