from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from DataTransformer import DataTransformer
from ReutersCorpus import ReutersCorpus
from ResultDataTransformer import ResultDataTransformer
from ParametersParser import ParametersParser
from nltk.corpus import reuters


class SVM:
    def __init__(self):
        self.is_classifier_trained = False

        # Trained classifier
        self.clf = any

        self.reutersCorpus = ReutersCorpus()
        self.dataTransformer = DataTransformer()

        # Vectorized documents
        self.v_train_docs = any
        self.v_test_docs = any

        # Binarized labels
        self.b_train_labels = any
        self.b_test_labels = any

    # Method creates and return classifier. Using OneVsRestClassifier
    def classify(self, c, kernel, degree, gamma, coef0, shrinking, probability, tol, cache_size, verbose, max_iter,
                 decision_function_shape, random_state):
        return OneVsRestClassifier(SVC(C=c, kernel=kernel, degree=degree, gamma=gamma, coef0=coef0,
                                       shrinking=shrinking, probability=probability, tol=tol, cache_size=cache_size,
                                       verbose=verbose, max_iter=max_iter,
                                       decision_function_shape=decision_function_shape, random_state=random_state))\
            .fit(self.v_train_docs, self.b_train_labels)

    # Method train created classifier with all train documents from corpus reuters
    def train_svm(self, c=1.0, kernel='rbf', degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False,
                  tol=1e-3, cache_size=200.0, verbose=False, max_iter=-1, decision_function_shape=None,
                  random_state=None):
        state, messages = ParametersParser.parse_params(c=c, kernel=kernel, degree=degree, gamma=gamma, coef0=coef0,
                                                        shrinking=shrinking, probability=probability, tol=tol,
                                                        cache_size=cache_size, verbose=verbose, max_iter=max_iter,
                                                        decision_function_shape=decision_function_shape,
                                                        random_state=random_state)
        if not state:
            return False, messages

        self.reutersCorpus.get_documents()
        self.v_train_docs, self.v_test_docs = self.dataTransformer.transform_documents(self.reutersCorpus.train_docs,
                                                                                       self.reutersCorpus.test_docs)
        self.b_train_labels, self.b_test_labels = self.dataTransformer.transform_labels(self.reutersCorpus.train_labels,
                                                                                        self.reutersCorpus.test_labels)

        self.clf = self.classify(c, kernel, degree, gamma, coef0, shrinking, probability, tol, cache_size, verbose,
                                 max_iter, decision_function_shape, random_state)

        if self.clf:
            self.is_classifier_trained = True
            return True, any

    # Method for test trained classifier with all test documents from corpus reuters.
    # Return array with f1_weighted, f1_macro, f1_micro
    def test_svm(self):
        if not self.is_classifier_trained:
            return ['Classifier is not trained']

        prediction = self.clf.predict(self.v_test_docs)

        return ResultDataTransformer.transform_result_data(b_test_labels=self.b_test_labels, prediction=prediction)

    def classify_single_document(self, document, true_labels=None):
        if not self.is_classifier_trained:
            return ['Classifier is not trained']

        v_document = self.dataTransformer.vectorizer.transform([document])
        prediction = self.clf.predict(v_document)

        if true_labels is not None:
            b_true_labels = self.dataTransformer.mlb.transform([true_labels])
            return [self.dataTransformer.mlb.inverse_transform(prediction), self.clf.score(v_document, b_true_labels)]

        return self.dataTransformer.mlb.inverse_transform(prediction)
