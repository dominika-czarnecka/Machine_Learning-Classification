import json
import pickle
import os

class SavedClassifiersManager:

    @staticmethod
    def save(svm, name):
        pickle.dump(svm, open(name, 'wb'))

    @staticmethod
    def load(name):
        return pickle.load(open(name, 'rb'))