from nltk.corpus import reuters


class ReutersCorpus:
    def __init__(self):
        self.train_docs_id = []
        self.test_docs_id = []
        self.train_docs = []
        self.test_docs = []
        self.train_labels = []
        self.test_labels = []

    # Get all document from reuters
    def get_documents(self):
        documents = reuters.fileids()

        self.train_docs_id = list(filter(lambda doc: doc.startswith("train"), documents))
        self.test_docs_id = list(filter(lambda doc: doc.startswith("test"), documents))

        self.train_docs = [reuters.raw(doc_id) for doc_id in self.train_docs_id]
        self.test_docs = [reuters.raw(doc_id) for doc_id in self.test_docs_id]

        self.train_labels = [reuters.categories(doc_id) for doc_id in self.train_docs_id]
        self.test_labels = [reuters.categories(doc_id) for doc_id in self.test_docs_id]