from nltk.corpus import reuters

from Backend.Integration.Interfaces.CorpusInterface import ICorpus


class Corpus(ICorpus):

    train_docs = []
    test_docs = []

    def __init__(self):
        for doc_id in reuters.fileids():
            if doc_id.startswith("train"):
                self.train_docs.append(reuters.raw(doc_id))
            else:
                self.test_docs.append(reuters.raw(doc_id))

    def get_test_documents(self):
        return self.test_docs

    def get_train_documents(self):
        return self.train_docs