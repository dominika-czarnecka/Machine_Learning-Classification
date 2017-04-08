class ClassificatorInterface(object):
    def __init__(self):
        pass

    def train(self, args, count):
        raise Exception("NotImplementedException")

    def classify(self, document):
        raise Exception("NotImplementedException")