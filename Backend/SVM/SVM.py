from sklearn import svm

class ClassificatorInterface(object):
    dict = {}
    dict_rev = []

    def __init__(self, corpus):
        self.clf = svm.SVC(kernel='linear')
        self.corpus = corpus

    def train(self, args, count):
        i = 0
        for word in corpus.get_unique_words():
            


    def classify(self, document):
        vec = self.doc2vec(document)
        return self.clf.predict(vec)

    def doc2vec(self, document):
        raise Exception("NotImplementedException")