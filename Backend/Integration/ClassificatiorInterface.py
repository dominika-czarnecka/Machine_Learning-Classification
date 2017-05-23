from abc import ABCMeta, abstractmethod

class ClassificatorInterface(object):
    __metaclass__ = ABCMeta

    @classmethod
    def __init__(self):
        pass

    @abstractmethod
    def train(self, args, count):
        raise Exception("NotImplementedException")

    @abstractmethod
    def classify(self, document):
        raise Exception("NotImplementedException")