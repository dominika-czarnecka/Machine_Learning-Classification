from nltk.corpus import reuters


class Corpus:
    def __init__(self, name):
        self.train_docs_id = []
        self.test_docs_id = []
        self.train_docs = []
        self.test_docs = []
        self.train_labels = []
        self.test_labels = []

        self.get_documents(name)

    # Get all document from reuters
    def get_documents(self, name):
        if name=='reuters':
            corpus = reuters
        else:
            raise ValueError('corpus ' + name + ' not supported')

        documents = corpus.fileids()

        self.train_docs_id = list(filter(lambda doc: doc.startswith("train"), documents))
        self.test_docs_id = list(filter(lambda doc: doc.startswith("test"), documents))

        self.train_docs = [corpus.raw(doc_id) for doc_id in self.train_docs_id]
        self.test_docs = [corpus.raw(doc_id) for doc_id in self.test_docs_id]

        self.train_labels = [corpus.categories(doc_id) for doc_id in self.train_docs_id]
        self.test_labels = [corpus.categories(doc_id) for doc_id in self.test_docs_id]