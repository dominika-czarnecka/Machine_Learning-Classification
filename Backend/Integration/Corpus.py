from Backend.Integration.CorpusInterface import CorpusInteface
from nltk.corpus import reuters


class Corpus(CorpusInteface):

    train_docs = []
    test_docs = []

    def __init__(self):
        for doc_id in reuters.fileids():
            if doc_id.startswith("train"):
                self.train_docs.append(reuters.raw(doc_id))
            else:
                self.test_docs.append(reuters.raw(doc_id))

    def getTestDocuments(self):
        return self.test_docs

    def getTrainDocuments(self):
        return self.train_docs