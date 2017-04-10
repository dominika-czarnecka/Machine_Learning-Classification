from sklearn import svm

class ClassificatorInterface(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self._dict = {}
        self._dict_rev = []
        self.kernel_type = 'linear'

    def train(self, args, count):
        self.create_dictionary()

        xs = []
        ys = []
        for doc in corpus.docs():
            xs.append(self.doc2vec(doc))
            ys.append(doc.category)

        self.clf = svm.SVC(self.kernel)
        self.clf.fit(xs, ys)

    def create_dictionary(self):
        i = 0
        for word in corpus.get_unique_words():
            self._dict[word] = i
            self._dict_rev[i] = word
            i += 1

    def classify(self, document):
        vec = self.doc2vec(document)
        return self.clf.predict(vec)

    def doc2vec(self, document):
        vect = []

        for word in document:
            if self._dict.has_key(word):
                i = self[word]
                vect[i] = 1

        return vect