from abc import ABCMeta, abstractmethod

class DocumentInteface(object):
    __metaclass__ = ABCMeta

    @classmethod
    def __init__(self):
        pass

    @abstractmethod
    def preprocessing(self):
        raise Exception("NotImplementedException")

    @abstractmethod
    def get_unique_words(self):
        raise Exception("NotImplementedException")