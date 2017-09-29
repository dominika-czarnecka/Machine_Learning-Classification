from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC

from .Corpus import Corpus
from .DataTransformer import DataTransformer
from .ResultDataTransformer import ResultDataTransformer
from .SavedClassifiersManager import SavedClassifiersManager


class SVM:
    def __init__(self):
        self.clf = any
        self.dataTransformer = DataTransformer()

    def get_trained_classifier(self, c, kernel, degree, gamma, coef0, shrinking, tol, max_iter, v_train_docs,
                               b_train_labels):
        clas = OneVsRestClassifier(SVC(C=c, kernel=kernel, degree=degree, gamma=gamma, coef0=coef0,
                                       shrinking=shrinking, tol=tol, max_iter=max_iter))
        clas.fit(v_train_docs, b_train_labels)
        return clas

    def train(self, fromFile, input, args, name):
        if fromFile:
            raise NotImplementedError
        else:
            corpus = Corpus(input)

        # ParametersParser.assert_args(args)

        svm = SVM()

        v_train_docs = svm.dataTransformer.vectorizer.fit_transform(corpus.train_docs)
        b_train_labels = svm.dataTransformer.mlb.fit_transform(corpus.train_labels)

        svm.clf = SVM.get_trained_classifier(self, args['c'], args['kernel'], args['degree'], args['gamma'], args['coef0'],
                                             args['shrinking'], args['tol'], args['max_iter'],
                                             v_train_docs, b_train_labels)

        SavedClassifiersManager.save(svm, name)

    def test(self, fromFile, input, name):
        if fromFile:
            raise NotImplementedError
        else:
            corpus = Corpus(input)

        svm = SavedClassifiersManager.load(name)
        if svm is None:
            raise FileNotFoundError

        v_test_docs = svm.dataTransformer.vectorizer.transform(corpus.test_docs)
        b_test_labels = svm.dataTransformer.mlb.transform(corpus.test_labels)
        prediction = svm.clf.predict(v_test_docs)

        return ResultDataTransformer.transform_result_data(b_test_labels=b_test_labels, prediction=prediction)

    def single(text, name):
        svm = SavedClassifiersManager.load(name)
        if svm is None:
            raise FileNotFoundError

        v_document = svm.dataTransformer.vectorizer.transform([text])
        prediction = svm.clf.predict(v_document)

        return svm.dataTransformer.mlb.inverse_transform(prediction)
