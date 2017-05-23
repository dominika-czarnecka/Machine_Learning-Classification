from abc import ABCMeta, abstractmethod

class ClassificatorInterface(object):
    __metaclass__ = ABCMeta

    @classmethod
    def __init__(self):
        pass

    @abstractmethod
    def train(self, from_file, input, args, name):
        raise Exception("NotImplementedException")

    @abstractmethod
    def test(self, from_file, input, args, classificator):
        raise Exception("NotImplementedException")

    @abstractmethod
    def single(self, text, args):
        raise Exception("NotImplementedException")