from abc import ABCMeta, abstractmethod

class ICorpus:
    __metaclass__ = ABCMeta

    @classmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_document(self):
        raise NotImplemented

    @abstractmethod
    def get_train_documents(self):
        raise NotImplemented

    @abstractmethod
    def get_test_documents(self):
        raise NotImplemented

